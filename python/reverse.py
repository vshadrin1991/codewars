txt: str = "letter than letter returns only will in spaces words will spaces more with letters name or the than Kata"

def spin_words(sentence: str):
    return ' '.join([s[::-1] if (len(s) > 5) else s for s in sentence.split(' ')])


print(spin_words(txt))

