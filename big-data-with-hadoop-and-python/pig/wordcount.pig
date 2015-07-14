SET default_parallel 98;

text   = LOAD '/input' AS (line:chararray);
words  = FOREACH text GENERATE FLATTEN(TOKENIZE(TRIM(line))) AS word;
groups = GROUP words BY word;
result = FOREACH groups GENERATE group, COUNT(words);

STORE result INTO '/output';
