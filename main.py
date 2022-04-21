from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from snowballstemmer import stemmer
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tag import CRFTagger
from pprint import pprint
from nltk.corpus import wordnet as wn

sentences = [

    "A user with admin privileges shall be able to Add/Create a new user and associate the user with specified role(s) in the system",
    "The user shall be able to add additional roles manually while creating/adding a new user from a user template.",
    "Languages Stemming The system shall generate a standard confirmation message after saving data and warning/caution messages after the cancel or close button is clicked.",
]

stop_en = set(stopwords.words("english"))
#print(stop_en)

#Tokenizing (Pemisahan Kata)
print('Tokenizing (Pemisahan Kata)')
word_tokens = []
for sentences in sentences:
    word_tokens.append(word_tokenize(sentences))
pprint(word_tokens)

#Case Folding (Pembuatan huruf kecil semua)
print('Case Folding (Pembuatan huruf kecil semua)')
casefolded_sentence = []
for word_token in word_tokens:
    casefolded_sentence.append([word.casefold() for word in word_token])
    #casefolded_sentence.append([word.lower() for word in word_token])
pprint(casefolded_sentence)

#Stopword Removal (Proses menghilangkan kata penghubung)
print('Stopword Removal (Proses menghilangkan kata penghubung)')
filtered_sentence = []
for sent in casefolded_sentence:
    filtered_sentence.append([word for word in sent if word not in stop_en])
pprint(filtered_sentence)

#List of words to sentence (Pembuatan kalimat dari kata-kata)
print('List of words to sentence (Pembuatan kalimat dari kata-kata)')
sentences = []
for filtered_sent in filtered_sentence:
    sentences.append(' '.join(filtered_sent))
pprint(sentences)





