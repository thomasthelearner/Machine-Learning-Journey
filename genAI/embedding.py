vocab = ['cat', 'dog', 'Tuesday', 'happy', 'sad']

def one_hot(word, vocab):
  vector = [0] * len(vocab)
  # TODO: flip the position of `word` in `vector` to 1
  vector[vocab.index(word)] = 1
  return vector

def hamming(v1, v2):
  # Counts the positions where two vectors differ
  count = 0
  for a, b in zip(v1, v2):
    if a != b:
      count += 1
  return count

# Write code below 💖
vec_cat = one_hot('cat', vocab)
vec_dog = one_hot('dog', vocab)
print(hamming(vec_cat, vec_dog))