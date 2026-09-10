from math import sqrt

doc_cat = 'the cat sat on the mat the cat purred'
doc_dog = 'the dog sat on the rug the dog barked'
doc_pizza = 'I love pizza and I love pasta'

def build_vocab(docs):
  vocab = []
  for doc in docs:
    for word in doc.split():
      if word not in vocab:
        vocab.append(word)
  return vocab

def bag_of_words(doc, vocab):
  vector = [0] * len(vocab)
  for word in doc.split():
    if word in vocab:
      vector[vocab.index(word)] += 1
  return vector

def dot_product(vector1, vector2):
  # Multiply each pair of matching positions and sum the results
  total = 0
  for num_vec1, num_vec2 in zip(vector1, vector2):
    total += num_vec1 * num_vec2
  return total

def magnitude(vector):
  # Square each value, sum, then take the square root
  total = 0
  for x in vector:
    total += x * x
  return sqrt(total)

def cosine_similarity(vector1, vector2):
  # TODO: return the dot product divided by the product of the two magnitudes
  return dot_product(vector1, vector2)/(magnitude(vector1) * magnitude(vector2))

# Write code below 💖
docs = [doc_cat, doc_dog, doc_pizza]
vocab = build_vocab(docs)
vector_cat = bag_of_words(doc_cat, vocab)
vector_dog = bag_of_words(doc_dog, vocab)
vector_pizza = bag_of_words(doc_pizza, vocab)

total = dot_product(vector_cat, vector_dog)
sqrt_cat = magnitude(vector_cat)
sqrt_dog = magnitude(vector_dog)
sqrt_pizza = magnitude(vector_pizza)

print(cosine_similarity(vector_cat, vector_dog))
print(cosine_similarity(vector_cat, vector_pizza))
print(cosine_similarity(vector_dog, vector_pizza))
