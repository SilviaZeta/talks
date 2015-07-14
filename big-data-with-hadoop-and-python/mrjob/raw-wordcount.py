from mrjob import job, protocol

class MRWordCount(job.MRJob):
    INTERNAL_PROTOCOL = protocol.RawProtocol
    OUTPUT_PROTOCOL = protocol.RawProtocol

    def mapper(self, _, line):
        for word in line.strip().split(' '):
            yield word, '1'

    def combiner(self, word, counts):
        yield word, str(sum(int(c) for c in counts))

    def reducer(self, word, counts):
        yield word, str(sum(int(c) for c in counts))

if __name__ == '__main__':
    MRWordCount.run()
