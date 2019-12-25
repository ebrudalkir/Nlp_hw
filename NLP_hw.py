import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt') #ingilizce için öğretilmiş belirteçler; cümlenin nerde bitmesi lazım fln
import pandas as pd
from nltk.util import ngrams
from nltk import tokenize
from nltk.tokenize import sent_tokenize, word_tokenize

file =open('Text_1.txt','r')
data_read=file.read()
data=data_read.lower() #bütün harfleri duyarlılık olduğu için küçük harfe çevirip işleme soktuk.

txt_data=data.split()
for i in txt_data:
    print(i)

#stopwords bağlaç tek başına anlam ifade etmeyen değerler
stop_words = set(stopwords.words('english'))
for x in stop_words:
    print(x)

''''bu kısım bigrams uygulayarak harf harf ayırmaktadır.
string_bigrams = list(nltk.bigrams(data))
for i in string_bigrams:
  print(i)'''

#stopwordslerden temizledik.
token = nltk.word_tokenize(data)
filtered_sentence = [w for w in token if not w in stop_words]
filtered_sentence = []
for w in token:
    if w not in stop_words:
        filtered_sentence.append(w)

print(token)
print(filtered_sentence)

n = 2  #bu kısmda kelime olarak ngram uygulamaktadır.
n_grams = ngrams(data.split(),n)
for grams in n_grams:
  print(grams)

#bu kısımda ngramların sayısını yazmaktasır.
n_grams = ngrams(filtered_sentence,n)
result=nltk.Counter(n_grams)
print(result)

