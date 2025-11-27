import nltk
from nltk.util import ngrams
from collections import Counter
import random, math

# Train n-gram model
def train(text, n=2):
    words = ["<s>"]*(n-1) + text.lower().split() + ["</s>"]
    model = Counter(ngrams(words, n))
    context_counts = Counter(ngrams(words, n-1))
    return model, context_counts, set(words)

# Generate text
def generate(model, context_counts, vocab, n=2, length=20):
    context = ["<s>"]*(n-1)
    result = []

    for _ in range(length):
        candidates = [(w[-1], model[w]) for w in model if list(w[:-1]) == context]
        if not candidates: break

        words, freqs = zip(*candidates)
        word = random.choices(words, freqs)[0]

        if word == "</s>": break
        result.append(word)
        context = (context + [word])[1:]

    return " ".join(result)

text = input("Enter short sentence: ") 

model, ctx, vocab = train(text, n=2)
print("Generated:", generate(model, ctx, vocab) )
# print(len(generate(model, ctx, vocab)))
