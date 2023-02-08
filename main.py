import nltk
from nltk.corpus import wordnet as wn


def download_nltk():
    nltk.download('wordnet')
    nltk.download('omw-1.4')


if __name__ == '__main__':
    # download_nltk()
    file = open('squirrel.txt', 'r')
    for line in file:
        print(line)
    file.close()
