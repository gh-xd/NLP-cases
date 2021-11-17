# Text to Knowledge Graph

My notes:
1. It works but refers to too many NLP libararies or even API which needs network. It takes time to install different libraries.
2. Might need to find another way to realize *Information Retrieval*. Heard of BERT+(LSTM)+CRF? Find more.
3. Skip the *Relation Extraction* and *Knowledge Graph* part...

## 1. Pipeline and NLP Libraries
**Step 1 - Coreference resolution**
- Libraries: `SpaCy` and `Neuralcoref`
- Code: [coref-res](./coref-res.py)

**Step 2 - Named Entity Linking**
- Library: None, but `wikifier.com API`
- Code: [nel-re](./nel-re.py)

**Step 3 - Relationship Extraction**
- Library: `OpenNRE`
- Code: [nel-re](./nel-re.py)

**Step 4 - Knowledge Graph**
- Database: `Neo4j`


## 2. Installation Notes
- SpaCy and neuralcoref have version conflict: Using `SpaCy 2.1.0 and neuralcoref 4.0` can work.
- Before loading SpaCy model, it should be downloaded manually: `python -m spacy download en_core_web_sm`
- `OpenNRE` don't fit Windows. Both pip and conda installation don't work. Clone the project from [thunlp/OpenNRE](https://github.com/thunlp/OpenNRE) and follow the instruction to install.
- During installing `OpenNRE`, Linux command `wget` is required. Homebrew in MacOS didn't install it. It should be installed manually.

## 3. Reference
Source: [From Text to Knowledge: The Information Extraction Pipeline](https://towardsdatascience.com/from-text-to-knowledge-the-information-extraction-pipeline-b65e7e30273e)