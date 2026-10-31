from src.core.job.reducer import Reducer

class CharRatioReducer(Reducer):
    def reduce(self, key, values, emit):
        total_vowels = 0
        total_consonants = 0

        for vowels, consonants in values:
            total_vowels += vowels
            total_consonants += consonants

        total_letters = total_vowels + total_consonants

        if total_letters > 0:
            v_pct = round((total_vowels / total_letters)*100, 2)
            c_pct = round((total_consonants/total_letters)* 100, 2)
            result = f"{v_pct}% vowels, {c_pct}% consonants"
        else: result = "NONE vowels, consonants"

        emit(f"length_{key}", result)