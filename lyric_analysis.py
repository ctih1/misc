import requests

data = [
  {
    "Sijoitus": "1.",
    "Kappaleen nimi": "Cha Cha Cha",
    "Artisti": "Käärijä",
    "Toistokerrat (28. tammikuuta  2026)": "192 235 134",
    "Lähde": "[3]"
  },
  {
    "Sijoitus": "2.",
    "Kappaleen nimi": "Ievan Polkka",
    "Artisti": "Korpiklaani",
    "Toistokerrat (28. tammikuuta  2026)": "41 892 458",
    "Lähde": "[4]"
  },
  {
    "Sijoitus": "3.",
    "Kappaleen nimi": "Timanttei",
    "Artisti": "Mirella",
    "Toistokerrat (28. tammikuuta  2026)": "40 004 396",
    "Lähde": "[5]"
  },
  {
    "Sijoitus": "4.",
    "Kappaleen nimi": "Ikuinen vappu",
    "Artisti": "JVG",
    "Toistokerrat (28. tammikuuta  2026)": "39 573 526",
    "Lähde": "[6]"
  },
  {
    "Sijoitus": "5.",
    "Kappaleen nimi": "Hei rakas",
    "Artisti": "Behm",
    "Toistokerrat (28. tammikuuta  2026)": "38 212 136",
    "Lähde": "[7]"
  },
  {
    "Sijoitus": "6.",
    "Kappaleen nimi": "Tarkenee",
    "Artisti": "JVG",
    "Toistokerrat (28. tammikuuta  2026)": "34 301 005",
    "Lähde": "[8]"
  },
  {
    "Sijoitus": "7.",
    "Kappaleen nimi": "Ylivoimainen",
    "Artisti": "Kuumaa",
    "Toistokerrat (28. tammikuuta  2026)": "32 125 689",
    "Lähde": "[9]"
  },
  {
    "Sijoitus": "8.",
    "Kappaleen nimi": "Tulipalo",
    "Artisti": "Kuumaa",
    "Toistokerrat (28. tammikuuta  2026)": "31 786 190",
    "Lähde": "[10]"
  },
  {
    "Sijoitus": "9.",
    "Kappaleen nimi": "Penelope",
    "Artisti": "William feat. Clever",
    "Toistokerrat (28. tammikuuta  2026)": "31 300 266",
    "Lähde": "[11]"
  },
  {
    "Sijoitus": "10.",
    "Kappaleen nimi": "Frida",
    "Artisti": "Behm",
    "Toistokerrat (28. tammikuuta  2026)": "31 260 154",
    "Lähde": "[12]"
  },
  {
    "Sijoitus": "11.",
    "Kappaleen nimi": "ICH KOMME",
    "Artisti": "Erika Vikman",
    "Toistokerrat (28. tammikuuta  2026)": "30 399 649",
    "Lähde": ""
  },
  {
    "Sijoitus": "12.",
    "Kappaleen nimi": "Shamppanjadieetillä",
    "Artisti": "Gettomasa feat. Van Hegen",
    "Toistokerrat (28. tammikuuta  2026)": "29 074 269",
    "Lähde": "[13]"
  },
  {
    "Sijoitus": "13.",
    "Kappaleen nimi": "Silmät",
    "Artisti": "Gettomasa",
    "Toistokerrat (28. tammikuuta  2026)": "28 855 490",
    "Lähde": "[14]"
  },
  {
    "Sijoitus": "14.",
    "Kappaleen nimi": "Timantit on ikuisia",
    "Artisti": "Cheek",
    "Toistokerrat (28. tammikuuta  2026)": "28 821 897",
    "Lähde": "[15]"
  },
  {
    "Sijoitus": "15.",
    "Kappaleen nimi": "BLONDINA",
    "Artisti": "Ibe",
    "Toistokerrat (28. tammikuuta  2026)": "28 732 576",
    "Lähde": "[16]"
  },
  {
    "Sijoitus": "16.",
    "Kappaleen nimi": "Beibi",
    "Artisti": "Haloo Helsinki!",
    "Toistokerrat (28. tammikuuta  2026)": "28 354 979",
    "Lähde": "[17]"
  },
  {
    "Sijoitus": "17.",
    "Kappaleen nimi": "Taulut",
    "Artisti": "Hugo feat. Costi",
    "Toistokerrat (28. tammikuuta  2026)": "28 279 383",
    "Lähde": "[18]"
  },
  {
    "Sijoitus": "18.",
    "Kappaleen nimi": "Häissä",
    "Artisti": "JVG feat. Märkä-Simo",
    "Toistokerrat (28. tammikuuta  2026)": "27 932 345",
    "Lähde": "[19]"
  },
  {
    "Sijoitus": "19.",
    "Kappaleen nimi": "Jättiläinen",
    "Artisti": "Pyhimys feat. Aksel Kankaanranta",
    "Toistokerrat (28. tammikuuta  2026)": "27 419 086",
    "Lähde": "[20]"
  },
  {
    "Sijoitus": "20.",
    "Kappaleen nimi": "Antaudun",
    "Artisti": "Reino Nordin",
    "Toistokerrat (28. tammikuuta  2026)": "26 974 931",
    "Lähde": "[21]"
  }
]


lyrics = []
for song in data:
    artist = song["Artisti"]
    name = song["Kappaleen nimi"]
    
    print(f"Fetching {artist}: {name}")
    r = requests.get("https://lrclib.net/api/search", params={
        "track_name": name.replace(" ", "+"),
        "artist_name": artist.replace(" ", "+")
    })

    for f_song in r.json():
        print(f"Found {f_song['artistName']}: {f_song['trackName']}")

        lyrics.append(f_song["plainLyrics"])
        break

with open("lyrics.json", "w") as f:
    import json
    json.dump(lyrics, f)
