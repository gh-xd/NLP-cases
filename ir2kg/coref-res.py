import spacy
import neuralcoref
from pprint import pprint

# Load SpaCy
nlp = spacy.load('en_core_web_sm')

# Add neuralcoref to SpaCy's pip
neuralcoref.add_to_pipe(nlp)

# Load text
with open('input.txt', encoding='utf-8') as f:
    text = f.readlines()
    f.close()

def coref_resolution(text):
    text = text[0]
    doc = nlp(text)

    # fetches tokens with whitespaces from spacy document
    token_list = list(token.text_with_ws for token in doc)

    # Clusters:
    # Elon Musk: [Elon Musk, He, He, He, Musk, Musk, He, He, he, He, He, his]
    # Pretoria: [Pretoria, Pretoria]
    # Queen's University: [Queen's University, the University of Pennsylvania, Stanford University]
    
    # That means, cluster in doc._.coref_clusters will show all identified coreference
    for cluster in doc._.coref_clusters:

        # get tokens from representative cluster name
        cluster_main_words = set(cluster.main.text.split(' '))

        # coref: means all identified elements (also pronoun)
        for coref in cluster:
            print(coref.text)
            # if coreference element is not the representative element of that cluster
            if coref != cluster.main:

                # if coreference element text and representative element text are not equal
                # and none of the coreference element words are in representative elements
                # this was done to handle nested coreference scenarios
                if coref.text != cluster.main.text and bool(set(coref.text.split(' ')).intersection(cluster_main_words)) == False:

                    token_list[coref.start] = cluster.main.text + doc[coref.end-1].whitespace_

                    for i in range(coref.start+1, coref.end):
                        token_list[i] = ""

    return "".join(token_list)


if __name__ == '__main__':
    text = coref_resolution(text)
    # pprint(text)