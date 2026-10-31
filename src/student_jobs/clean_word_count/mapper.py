import re
from src.core.job.mapper import Mapper

class CleanWordCountMapper(Mapper):
    def map(self, record, emit):
        words = re.findall(r"[a-zA-Zа-яА-ЯіІїЇєЄґҐ']+", str(record).lower())
        for word in words:
            clean_word = word.strip("'\"`")
            if clean_word:
                emit(clean_word, 1) 