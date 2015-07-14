Big Data with Hadoop and Python
===============================

Here you can find code examples from my talk "Big Data with Hadoop and Python" that was given
on `EuroPython 2015 <https://ep2015.europython.eu/en/>`__, that were used to benchmark the
performance of different Python frameworks for Hadoop compared to `Java <https://www.java.com/en/>`_
and `Apache Pig <https://pig.apache.org>`_.

The examples are a simple wordcount implementation. I used a book by Mark Lutz - Learning Python, 3rd
edition as an input, multiplied 10000 times with the following simple bash script:

.. code-block:: bash

   #!/bin/bash

   IN="${1}"
   OUT="${2}"

   for i in {1..10000}; do
       echo "${IN}"
   done | xargs cat > "${OUT}"

Below are the brief instructions that will help you to recreate the benchmarks if needed.

Java
----

#. Download the ``WordCount.java`` and run the following command to compile it:

   .. code-block:: bash

      javac -classpath /path/to/hadoop-common.jar:/path/to/hadoop-mapreduce-client-core.jar:/path/to/hadoop-annotations.jar WordCount.java

#. Run the following command to create a Jar file from compiled class files:

   .. code-block:: bash

      jar -cvf WordCount.jar WordCount*.class

#. Finally run the following command to submit a job to the cluster:

   .. code-block:: bash

      hadoop jar WordCount.jar WordCount hdfs:///input hdfs:///output

Pig
---

#. Download the ``wordcount.pig``. Open it in your favourite text editor and set the ``input``
   and ``output`` directories inside HDFS.

#. Run the following command to submit a job to the cluster:

   .. code-block:: bash

      pig wordcount.pig

Streaming
---------

#. Download the ``mapper.py`` and ``reducer.py`` and change the first line if you want to
   run them under PyPy.

#. Run the following command to submit a job to the cluster:

   .. code-block:: bash

      hadoop jar /path/to/hadoop-streaming.jar \
          -Dmapreduce.job.reduces=98 \
          -file /path/to/mapper.py \
          -file /path/to/reducer.py \
          -mapper /path/to/mapper.py \
          -reducer /path/to/reducer.py \
          -combiner /path/to/reducer.py \
          -input hdfs:///input \
          -output hdfs:///output

MRJob
-----

#. Download the ``raw-wordcount.py`` and ``ujson-wordcount.py``. Keep in mind that you'll
   need to install ``ujson`` library to the whole cluster and you'll need MRJob >= 0.5.0
   for this to work.

#. Set path to Hadoop home with the following command:

   .. code-block:: bash

      export HADOOP_HOME=/path/to/hadoop/home/dir

#. Run the following command to submit a job to the cluster:

   .. code-block:: bash

      python raw-wordcount.py -r hadoop hdfs:///input --output-dir hdfs:///output --no-output --hadoop-streaming-jar /path/to/hadoop-streaming.jar --jobconf mapreduce.job.reduces=98

Luigi
-----

#. Download the ``client.cfg``, ``default-wordcount.py`` and ``json-wordcount.py``. Open them in
   your favourite text editor and set streaming jar path and the ``input`` / ``output`` directories
   inside HDFS.

#. Run the following command to submit a job to the cluster:

   .. code-block:: bash

      python default-wordcount.py WordCount --local-scheduler

Pydoop
------

#. Download the ``wordcount.py``.

#. Set path to Java home with the following commands:

   .. code-block:: bash

      export JAVA_HOME=/path/to/java/home/dir

#. Create the Pydoop archive with the following command (this is needed because Pydoop doesn't
   automatically uploads itself to a cluster):

   .. code-block:: bash

      tar -czf pydoop.tgz -C /path/to/pydoop .

#. Run the following command to submit a job to the cluster:

   .. code-block:: bash

      pydoop submit --upload-archive-to-cache pydoop.tgz --num-reducers 98 --upload-file-to-cache wordcount.py wordcount /input /output
