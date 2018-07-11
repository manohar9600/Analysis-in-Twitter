# ----------------------------------------------- #

""" modules """

import wikipedia
import re


""" loading vocabulary """

with open('Data/vocabulary.txt', 'r', encoding='utf-8') as f:
    vocab = f.read().split()

dict_tel = {}
for i in range(len(vocab)):
    dict_tel[vocab[i]] = i + 1


""" Functions """

# dividing each sentence into words and converting words to positional numbers
def preprocess(content):
    global re
    global dict_tel
    content = re.sub('[a-zA-Z!@#$,%&*()-+{}=:;]', '', content)
    content = re.sub(r'\.{2,}', '', content)
    rows = content.split('\n')
    words = []

    for row in rows:
        temp = row.split('.')
        for sentence in temp:
            te = sentence.split()
            xe = []
            for word in te:
                try:
                    xe.append(dict_tel[word])
                except:
                    xe.append(0)
                    pass
            words.append(xe)

    data_word2vec(words)


# splitting data for feeding into word2vec
def data_word2vec(words):
    combi = []

    for sentence in words:
        for i in range(len(sentence)):
            te = []

            if i - 2 >= 0:
                te.append(sentence[i - 2])
            else:
                te.append(0)
            if i - 1 >= 0:
                te.append(sentence[i - 1])
            else:
                te.append(0)
            te.append(sentence[i])
            if i + 1 < len(sentence):
                te.append(sentence[i + 1])
            else:
                te.append(0)
            if i + 2 < len(sentence):
                te.append(sentence[i + 2])
            else:
                te.append(0)

            combi.append(te)

    write_todisk(combi)


def write_todisk(combi):
    f = open('word2vec/data.txt', 'a', encoding='utf-8')
    for te in combi:
        se = str(te[0]) + " " + str(te[1]) + " " + \
            str(te[2]) + " " + str(te[3]) + " " + str(te[4])
        f.write(se)
        f.write('\n')


""" Wikipedia """

wikipedia.set_lang('te')

f = open('word2vec/completed.txt', 'r', encoding='utf-8')
titles = f.read().split('\n')

for i in range(1300, 1400):
    title = titles[i]
    try:
        content = wikipedia.WikipediaPage(title=title).content
        preprocess(content)
        print(title)
    except:
        pass

print('completed')


""" news """

f = open('Data/telugu_txts/news.txt', 'r', encoding='utf-8')
preprocess(f.read())
f.close()


""" tweets """

f = open('Data/telugu_txts/tweets.txt', 'r', encoding='utf-8')
preprocess(f.read())
f.close()




    
