import matplotlib.pyplot as plt
import numpy as np
import re

with open("fileA-TimeMachine.txt", "r",encoding='utf-8') as file:
    data = file.read()

#A
def partA(data):
  words = [w.lower() for w in re.findall(r'\b\w+\b', data)]
  freq_words = {}
  for word in words:
    freq_words[word] = freq_words.get(word, 0) + 1
  return freq_words


freq_words = partA(data)
freq_words = dict(sorted(freq_words.items(), key=lambda item: item[1], reverse=False))
plt.hist(freq_words.values(), bins=40,color='black')
plt.xlabel('Frequency')
plt.ylabel('Number of Words')
plt.title('Frequency Distribution of Words')
plt.show()


#B
def partB(data):
  data = data.lower()
  data = re.sub(r'[^a-z]', '', data)
  pairFreq = {}
  for i in range(len(data) - 1):
    pair = data[i:i + 2]
    pairFreq[pair] = pairFreq.get(pair, 0) + 1
  totalPairs = sum(pairFreq.values())
  pairProb = {pair: freq / totalPairs for pair, freq in pairFreq.items()}
  return pairProb


pairProb = partB(data)
pairProb = dict(sorted(pairProb.items(), key=lambda item: item[1], reverse=True))
print('Top 10 ordered pairs of letters:')
for i, (pair, prob) in enumerate(pairProb.items()):
  if i == 10:
    break
  print(f'{pair}: {prob}')


#C
def partC(data):
  data = re.sub(r'[^a-z ]', '', data.lower())
  pairFreq = {}
  for i in range(len(data) - 1):
    pair = data[i:i + 2]
    pairFreq[pair] = pairFreq.get(pair, 0) + 1
  totalPairs = sum(pairFreq.values())
  pairProb = {pair: freq / totalPairs for pair, freq in pairFreq.items()}
  return pairProb


pairProb2 = partC(data)
pairProb2 = dict(sorted(pairProb2.items(), key=lambda item: item[1], reverse=True))
print('Top 10 ordered pairs of letters:')
for i, (pair, prob) in enumerate(pairProb2.items()):
  if i == 10:
    break
  print(f'{pair}: {prob}')
