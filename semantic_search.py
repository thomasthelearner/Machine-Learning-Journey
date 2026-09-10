from math import sqrt

documents = [
  'the cat sat on the warm mat',
  'the dog chased a stick in the yard',
  'I love pizza and pasta for dinner',
  'the kitten purred while she slept',
  'my puppy loves to play with toys',
  'homemade lasagna is my favorite meal',
]

def build_vocab(texts):
  vocab_list = []
  for text in texts:
    for word in text.split():
      if word not in vocab_list:
        vocab_list.append(word)
  return vocab_list

def bag_of_words(text, vocab_list):
  vector = [0] * len(vocab_list)
  for word in text.split():
    if word in vocab_list:
      vector[vocab_list.index(word)] += 1
  return vector

def dot_product(vector1, vector2):
  total = 0
  for x, y in zip(vector1, vector2):
    total += x * y
  return total

def magnitude(vector):
  total = 0
  for x in vector:
    total += x * x
  return sqrt(total)

def cosine_similarity(vector1, vector2):
  return dot_product(vector1, vector2) / (magnitude(vector1) * magnitude(vector2))

def search(query, documents):
  # Build a shared vocabulary across the query and all documents
  vocab_list = build_vocab([query] + documents)
  query_vector = bag_of_words(query, vocab_list)

  results = []
  # TODO: for each document, turn it into a bag-of-words vector,
  # compute its cosine similarity with query_vector, and append
  # the (score, doc) tuple to results
  for doc in documents:
    doc_vector = bag_of_words(doc, vocab_list)
    score = cosine_similarity(query_vector, doc_vector)
    results.append((score, doc))

    #help to sort the results in descending order of similarity score
  results.sort(reverse=True)
  return results

# Write code below 💖
search_results = search("dog yard", documents)
print(search_results)


