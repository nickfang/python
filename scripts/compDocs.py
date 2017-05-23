import gensim
from nltk.tokenize import word_tokenize

raw_documents = ["I'm taking the show on the road.",
					  "My socks are a force multiplieer.",
					  "I am the barber who cuts everyone's hair who doesn't cut their own.",
					  "Legend has it that the mind is a mad monkey.",
					  "I make my own fun."]

print("Number of documents: ", len(raw_documents))

gen_docs = [[w.lower() for w in word_tokenize(text)] for text in raw_documents]

print(gen_docs)