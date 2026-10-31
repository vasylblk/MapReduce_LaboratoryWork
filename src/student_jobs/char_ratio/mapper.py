import re
from src.core.job.mapper import Mapper

class CharRatioMapper(Mapper):
    VOWELS = set("aeiouyаеєиіїоуюя")

    def map(self, record, emit):
        words = re.findall(r"[a-zA-Zа-яА-ЯіІїЇєЄґҐ']+", str(record).lower())
        for word in words:
            clean_word = word.replace("'", "")
            length = len(clean_word)
            
            if length == 0:
                continue

            vowels = sum(1 for char in clean_word if char in self.VOWELS)
            consonants = length - vowels
            
            emit(length, (vowels, consonants))