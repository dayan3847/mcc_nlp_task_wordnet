import nltk
import networkx as nx
from typing import List
from matplotlib import pyplot as plt
from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import Synset
import scipy as sp


class WordnetTest:

    @staticmethod
    def download_nltk_data():
        nltk.download('wordnet')
        nltk.download('omw-1.4')

    def __init__(self, file_name: str):
        self.file_name: str = file_name
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

    # graficar el arbol
    def plot_tree(self):
        # create directed graph
        graph = nx.DiGraph()
        graph.add_edges_from(self.tree)
        plt.figure(figsize=(10, 10))
        nx.draw(
            graph,
            with_labels=True,
            node_color='skyblue',
            node_size=1500,
            edge_cmap=plt.cm.Blues,
            font_size=8,
        )
        plt.show()


if __name__ == '__main__':
    file_name: str = 'squirrel.txt'
    # file_name: str = 'test2.txt'
    wordnet_test = WordnetTest(file_name)
    wordnet_test.run()
    wordnet_test.print_tree()
    # wordnet_test.plot_tree()
