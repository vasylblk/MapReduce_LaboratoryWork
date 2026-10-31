import re
from src.core.job.mapper import Mapper

class LongWordCountMapper(Mapper):
    def map(self, record, emit):
        words = re.findall(r"[a-zA-Zа-яА-ЯіІїЇєЄґҐ']+", str(record).lower())
        for word in words:
            clean_word = word.strip("'\"`")
            if len(clean_word) > 5:
                emit(clean_word, 1)