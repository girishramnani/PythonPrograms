from nltk.corpus import stopwords

english_stop = set(stopwords.words("english"))
print(english_stop)
from nltk.corpus import wordnet
syn = wordnet.synsets('sex')
[print(synx.definition()) for synx in syn]