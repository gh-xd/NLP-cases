import urllib
from string import punctuation
import json
from pprint import pprint
import itertools

ENTITY_TYPES = ["human", "person", "company", "enterprise", "business", "geographic region",
                "human settlement", "geographic entity", "territorial entity type", "organization"]

# Load text
with open('input.txt', encoding='utf-8') as f:
    text = f.readlines()
    f.close()


# Function fetches entity linking results from wikifier.com API
def wikifier(text, lang="en", threshold=0.8):
    # Prepare URL
    data = urllib.parse.urlencode([
        ("text", text), ("lang", lang), ("userKey", "tgbdmkpmkluegqfbawcwjywieevmza"), ("pageRankSqThreshold", "%g"%threshold),
        ("applyPageRankSqThreshold", "true"), ("nTopDfValuesToIgnore", "100"), ("nWordsToIgnoreFromList", "100"),
        ("wikiDataClasses", "true"), ("wikiDataClassIds", "false"), ("support", "true"), ("ranges", "false"),
        ("minLinkFrequency", "2"), ("includeCosines", "flase"), ("maxMentionEntropy", "3")
    ])

    url = "http://www.wikifier.org/annotate-article"

    # Call Wikifier and read the response
    req = urllib.request.Request(url, data=data.encode("utf8"), method="POST")
    with urllib.request.urlopen(req, timeout=60) as f:
        response = f.read()
        response = json.loads(response.decode("utf8"))

    print(response)
    
    # Output the annotations
    results = list()
    for annotation in response["annotations"]:
        
        # Filter out desired entity classes
        if ('wikiDataClasses' in annotation) and (any([el['enLabel'] in ENTITY_TYPES for el in annotation['wikiDataClasses']])):

            # Specify entity label
            if any([el['enLabel'] in ["human", "person"] for el in annotation['wikiDataClasses']]):
                label = 'Person'
            elif any([el['enLabel'] in ["company", "enterprise", "business", "organization"] for el in annotation['wikiDataClasses']]):
                label = 'Organization'
            elif any([el['enLabel'] in ["geographic region", "human settlement", "geographic entity", "territorial entity type"] for el in annotation['wikiDataClasses']]):
                label = 'Location'
            else:
                label = None

            results.append({'title': annotation['title'], 'wikiId': annotation['wikiDataItemId'], 'label': label,
                            'characters': [(el['chFrom'], el['chTo']) for el in annotation['support']]})
    
    return results

entities = wikifier(text)

