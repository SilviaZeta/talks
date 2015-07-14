from mrjob import job, protocol

class MRWordCount(job.MRJob):
    INTERNAL_PROTOCOL = protocol.UltraJSONProtocol
    OUTPUT_PROTOCOL = protocol.UltraJSONProtocol

    def mapper(self, _, line):
        for word in line.strip().split(' '):
            yield word, 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()
