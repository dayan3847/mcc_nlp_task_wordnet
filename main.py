from typing import List

import nltk
from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import Synset


class WordnetTest:

    def __init__(self):
        # self.file_name: str = 'squirrel.txt'
        self.file_name: str = 'test2.txt'
        self.tree: List[tuple[str, str]] = []

    def run(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                # Dividir la línea en palabras
                words = line.strip().split()
                for word in words:
                    # Buscar synset (conjunto de sinónimos) de la palabra
                    synsets: List[Synset] = wordnet.synsets(word)
                    for synset in synsets:
                        # Imprimir hiperónimos y hipónimos de cada synset
                        hypernyms: List[Synset] = synset.hypernyms()
                        for hypernym in hypernyms:
                            for lemma in hypernym.lemma_names():
                                self.tree.append((lemma, word))
                        hyponyms: List[Synset] = synset.hyponyms()
                        for hyponym in hyponyms:
                            for lemma in hyponym.lemma_names():
                                self.tree.append((word, lemma))

    def print_tree(self):
        for parent, child in self.tree:
            print(f'{parent} -> {child}')


if __name__ == '__main__':
    # nltk.download('wordnet')
    # nltk.download('omw-1.4')

    wordnet_test = WordnetTest()
    wordnet_test.run()
    wordnet_test.print_tree()
