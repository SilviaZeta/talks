import luigi
import luigi.contrib.hadoop
import luigi.contrib.hdfs

class InputText(luigi.ExternalTask):
    def output(self):
        return luigi.contrib.hdfs.HdfsTarget('/input')

class WordCount(luigi.contrib.hadoop.JobTask):
    n_reduce_tasks = 98

    def requires(self):
        return [InputText()]

    def output(self):
        return luigi.contrib.hdfs.HdfsTarget('/output')

    def mapper(self, line):
        for word in line.strip().split(' '):
            yield word, 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    luigi.run()
