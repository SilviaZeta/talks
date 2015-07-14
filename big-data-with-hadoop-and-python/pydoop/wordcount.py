import os
import sys

sys.path = [os.getcwd()] + sys.path

import pydoop.mapreduce.api as api
import pydoop.mapreduce.pipes as pp

class Mapper(api.Mapper):
    def map(self, context):
        for word in context.value.split(' '):
            context.emit(word, 1)

class Reducer(api.Reducer):
    def reduce(self, context):
        context.emit(context.key, sum(context.values))

def __main__():
    pp.run_task(pp.Factory(
        mapper_class=Mapper,
        reducer_class=Reducer,
        combiner_class=Reducer
    ))
