# ---------------------------

import wikipedia
import re
from collections import defaultdict
import copy
import json


# functions
def process(content):
    vocabulary = []
    content = re.sub('[a-zA-Z!@#$.,%&*()-+{}=:;]', '', content)
    frequency = defaultdict(int)
    for word in content.split():
        vocabulary.append(word)
        frequency[word] += 1

    vocabulary = [word for word in vocabulary if frequency[word] > 1]
    write_todisk(vocabulary)


def write_todisk(vocabulary):
    f = open('Data/vocabulary.txt', 'a', encoding='utf-8')
    vocabulary = set(vocabulary)
    for word in vocabulary:
        f.write(word)
        f.write('\n')
    f.close()


def backup(word):
    f = open('backup.txt', 'a', encoding='utf-8')
    f.write(word)
    f.write('\n')
    f.close()


def tuneing_words():
    f = open('Data/vocabulary.txt', 'r', encoding='utf-8')
    vocab = f.read()
    vocab = re.sub('[\'\"]', '', vocab)
    vocab = vocab.split()
    vocab = set(vocab)
    f.close()
    f = open('Data/vocabulary.txt', 'w', encoding='utf-8')
    for word in vocab:
        f.write(word)
        f.write('\n')
    f.close()
    print('Tuned Words')


""" building telugu vocabulary """

wikipedia.set_lang('te')
head_title = 'ఆంధ్ర ప్రదేశ్'
completed = []
to_complete = []
to_complete.append(head_title)


def open_backup():
    global completed
    file_in = open('completed.txt', 'r', encoding='utf-8')
    completed = file_in.read().split()
    file_in.close()
    

while len(to_complete) != 0:
    to_add = []
    for title in to_complete:
        if title not in completed:
            try:
                article = wikipedia.WikipediaPage(title=title)
            except:
                pass
            completed.append(title)
            process(article.content)
            backup(title)

            for link in article.links:
                if link not in completed:
                    to_add.append(link)
            print(title)
    
    to_complete = []
    to_complete = copy.copy(to_add)
    
    tuneing_words()

# adding vocabulary from news and stories and tweets
f = open('Data/telugu_txts/news.txt', 'r', encoding='utf-8')
process(f.read())

f = open('Data/telugu_txts/stories.txt', 'r', encoding='utf-8')
process(f.read())

f = open('Data/telugu_txts/tweets.txt', 'r', encoding='utf-8')
process(f.read())

""" saving vocabulary as a dictionary """

f = open('Data/vocabulary.txt', 'r', encoding='utf-8')
telugu_words = f.read().split()
f.close()
dict = {}
i = 1

for word in telugu_words:
    dict[word] = i
    i = i + 1

# saving dict as json
with open('Data/vocab.json', 'w', encoding='utf-8') as vocab_dict:
    json.dump(dict, vocab_dict)


