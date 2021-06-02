
from collections import Counter

import collections
words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
string1 = 'tcabnihjs'
string4 = 'bbabylkkj'

def find_embedded_wordList2(words, string):
    counts = Counter(string)
    for word in words:
        word_count = Counter(word)
        if not (word_count - counts):
            return word
    return None
def find_embedded_wordList(words, string1):
  d = collections.Counter(string1)
  result = []

  for word in words:
    ls = collections.Counter(word)
    print('ls',ls)
    result.append(word)
    for k,v in ls.items():
      if k in d:
        if v <= d[k]:
          continue
        else:
          result.pop()
          break
      else:
        result.pop()
        break
  return None if  len(result)==0 else result[0]




#After catching your classroom students cheating before, you realize your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

#Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
	['c', 'c', 'c', 'a', 'r', 's'],
	['c', 'c', 'i', 't', 'n', 'b'],
	['a', 'c', 'n', 'n', 't', 'i'],
	['t', 'c', 'i', 'i', 'p', 't']
]

word1_1 = "catnip"

def find_embedded_wordsMatrix(words,strings):
    print('words',words)
    string_map = Counter(strings)
    result = []
    for word in words:
        cache_map = []
        for ch in word:
            if string_map.get(ch) :
                cache_map.append(ch)
                string_map[ch] -=1
            else:
                for c in cache_map:
                    string_map[c]=string_map.get(c,0)+1
                break

        if len(cache_map)==len(word):
            result.append(word)

    print('result',result)
    return result

result = find_embedded_wordsMatrix(words,string1)

# result_word = find_embedded_wordList(words,string1)
print(result)