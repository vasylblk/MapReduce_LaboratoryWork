from src.core.job.reducer import Reducer


class CleanWordCountReducer(Reducer):
    def reduce(self, key, values, emit):
        emit(key, sum(values))


