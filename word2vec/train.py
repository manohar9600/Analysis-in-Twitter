### _--------__-----___--- #########

""" packages """

import gensim
from gensim.models import Word2Vec


""" loading vocabulary """

with open('Data/vocabulary.txt', 'r', encoding='utf-8') as f:
    vocab = f.read().split()

dict_tel = {}
for i in range(len(vocab)):
    dict_tel[vocab[i]] = i + 1


""" loading Data and converting it into words """

with open('word2vec/data.txt', 'r', encoding='utf-8') as f:
    data_num = f.read().split('\n')

data_txt = []

for row in data_num:
    sen = row.split()
    te = []
    for num in sen:
        if int(num) != 0:
            te.append(vocab[int(num) - 1])
        else:
            te.append('</unk>')
    data_txt.append(te)


""" training word2vec """

model = Word2Vec(data_txt, size=300, min_count=1)
        
model.most_similar(positive=['తెలుగు'], topn=10)

model.similarity('తెలుగు', 'తెలంగాణ')








