import string
import requests
import pickle

communist_manifesto = requests.get('http://www.gutenberg.org/cache/epub/61/pg61.txt').text
"""f = open('communist_manifesto.pickle','w')
pickle.dump(communist_manifesto,f)
f.close()
input_file = open('communist_manifesto.pickle','rb')
reloaded_copy_of_texts = pickle.load(input_file)"""


def get_word_list(file_name,n):
    dont_want = set(string.punctuation) #creating set so that the word list does not include puncutation
    words = ''.join(ch for ch in file_name if ch not in dont_want) # in order to create a list of words that are connected
    #f = open(file_name, 'r')
    start = words.index('MANIFESTO OF THE COMMUNIST PARTY') + 32 #starting it after MANIFESTO OF THE COMMUNIST PARTY
    words=words.lower()
    word=words[start]
    list_w= words.split() # every where there is a space will be split
    return get_top_n_words(list_w,n)


def get_top_n_words(word_list, n):
    inverse=dict()
    for word in (word_list):
        inverse[word] = inverse.get(word,0)+1 # everytime it sees the word it adds one to its value
    inverse = sorted(inverse, key=inverse.__getitem__) # sort it by the key so the frequency
    return inverse[-n:]

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(get_word_list(communist_manifesto,100))
