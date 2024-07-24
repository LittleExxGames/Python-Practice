import requests

url = "https://api.datamuse.com/words?rel_jjb=land"

response = requests.get(url)

data = response.json()
words = [element["word"] for element in data]
words = ', '.join(words)
for item in data:
    print(item)
print ("There was some %s soil in the forest. However, the place was pretty %s." % (data[16]["word"], data[4]["word"]))
print ("The adjectives for the word 'land' are: %s." % words)