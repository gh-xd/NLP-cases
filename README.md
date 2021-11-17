# Introduction

# Introduction

# Information Extraction tasks
- Input: unstructured texts
- Extract:
    - Entity
    - Relation
    - Events
    - Sentiments
- Output: structured information

## 实体 Entities
### 命名实体识别 Named Entity Recognition (NER)
...

### 指代消解 Anaphora Resolution
Resolves what a pronoun or noun phrase refers to

### 共指消解 Coreference Resolution
Find **all expressions** that refer to the same entities in a text

所有代表一个词的词语


## 关系 Relations

### 关系抽取 Relation extraction
Identify relations between entity under a set of prespecified relation categories


## 知识图谱 Knowledge Graph

### 实体链接 Entity Linking
Determines the identify of entity mentioned from text

Related task: **实体规范化 Named entity normalization**

统一一个词语的表示

### 链接预测 Link prediction
Kowledge graph inference

## 事件 Events

### 事件侦测 Event Detection

- News event detection (first story detection)
- Event factuality prediction (predict the likelihood of event)
- Event time extraction (e.g. temporal ordering of events)
- Causality detection

- Event coreference resolution
- Script learning