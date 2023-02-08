import nltk
from nltk.corpus import wordnet as wn


def download_nltk():
    nltk.download('wordnet')
    nltk.download('omw-1.4')


if __name__ == '__main__':
    download_nltk()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
