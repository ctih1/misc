import json

with open("lyrics.json", "r") as f:
    lyrics = json.load(f)


words = {}
for song in lyrics:
    for word in song.replace("\n", " ").split(" "):
        word = word.lower().replace("(", "").replace(")", "").replace("”", "").replace("”", "").replace("!", "").replace(",", "")
        if word not in words:
            words[word] = 0
        
        words[word] += 1


sorted = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
print(sorted)
