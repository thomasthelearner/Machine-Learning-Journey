import re

cinderella = """
Once upon a time there lived a gentleman who married for his second wife the
proudest and most haughty woman that was ever seen. She had two daughters of her
own who were indeed exactly like her in all things. He had likewise a young
daughter but of unparalleled goodness and sweetness of temper. The wedding was
scarcely over when the stepmother began to show herself in her true colors. She
could not bear the good qualities of this pretty girl and the less because they
made her own daughters appear the more mean. She employed her in the meanest
work of the house. The girl bore all patiently and dared not tell her father
who would have scolded her for his wife ruled him entirely. When the girl had
done her work she used to go into the chimney corner and sit down among cinders
and ashes which made her commonly be called Cinderwench. The younger sister who
was not so rude and uncivil as the elder called her Cinderella. However
Cinderella notwithstanding her mean apparel was a hundred times handsomer than
her sisters though they were always dressed very richly. It happened that the
king's son gave a ball and invited all persons of fashion to it. Our young
misses were also invited for they cut a very grand figure among the quality.
Cinderella was likewise consulted in all these matters for she had excellent
judgment and advised them always for the best. She offered her services to them
and they accepted them. The stepsisters mocked her and said you would only make
everyone laugh. Cinderella bore all their ill treatment patiently. At last the
happy day came. They went to court and Cinderella followed them with her eyes
as long as she could. When she lost sight of them she fell a crying. Her
godmother who saw her all in tears asked her what was the matter. I wish I
could I wish I could. She was not able to speak the rest being interrupted by
her tears and sobbing. Once upon a time a fairy godmother appeared and said do
not cry my dear child. You shall go to the ball. Once upon a time the princess
danced at the ball until midnight when she had to run away and she lost her
glass slipper on the steps.
""".strip()

def tokenize(text):
  return re.findall(r'\w+|[^\w\s]', text)

tokens = tokenize(cinderella.lower())

# Count the occurrences of each bigram and the next token that follows it
def count_next_tokens(tokens):
  counts = {}
  for i in range(len(tokens) -2):
    bigram = tokens[i] + ' ' + tokens[i+1]
    next_token = tokens[i+2]

    if bigram not in counts:
      counts[bigram] = {}  #output is a dictionary like counts = {bigram:{}}

    counts[bigram][next_token] = counts[bigram].get(next_token,0) + 1 #counts[bigram][next_token] will display like this: counts = {bigram (should be 2 words):{next_token}}

  return counts

counts = count_next_tokens(tokens)

# print(counts)

#Predict the next token based on the frequency of the next tokens that follow a given bigram
def predict_next_token(phrase):
  #take the last two words as a phrase (tokens) of the phrase as our context bigram
  phrase_tokens = tokenize(phrase.lower())
  if len(phrase_tokens) < 2:
    return None
  context = phrase_tokens[-2] + ' ' + phrase_tokens[-1] #take the last two words as a phrase (tokens) of the phrase as our context bigram

    #check if the context bigram exists in the counts dictionary
  if context not in counts:
    return None

  #find the next token with the highest frequency
  best_occured_token = None
  best_occured_count = 0
  for next_token, count in counts[context].items(): #item() method returns key-value pairs as tuples in a list
    if count > best_occured_count:
        best_occured_count = count
        best_occured_token = next_token
  return best_occured_token

print(predict_next_token("Once upon a"))  # Example usage

#autocomplete function that takes a phrase and predicts the next token based on the frequency of the next tokens that follow a given bigram with a limit of numbers of tokens to predict to avoid infinite loop or out of memory error
def autocomplete(phrase, num_tokens=20):
  result = phrase.lower()
  for _ in range(num_tokens):
    token = predict_next_token(result)
    if token is None:
      # We hit a context our predictor doesn't know... stop
      break
    result = result + ' ' + token
  return result

print(autocomplete("once upon"))  # Example usage
  


