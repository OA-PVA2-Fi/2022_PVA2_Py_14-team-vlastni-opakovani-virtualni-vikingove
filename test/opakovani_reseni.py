import json

# 1. Sestavte seznam studentu (jmeno, vek, trida), minimálně 3 (1 bod)
studenti = list()
studenti.append( {"jmeno": "Petr", "vek": 15, "trida": "1B" })
studenti.append( {"jmeno": "Sofie", "vek": 17, "trida": "1A" })
studenti.append( {"jmeno": "Alice", "vek": 18, "trida": "3A" })

# 2. Vypište seznam studentu do souboru studenti.json (2 body)
with open("studenti.json", "w", encoding="utf8") as file:
    file.write(json.dumps(studenti))
    
# 3. Načtení obsahu souboru tv-shows.json (1 bod)
with open("tv-shows.json", encoding='utf8') as file:
    data = json.load(file)

#4. Vypište série, které mají žánr Drama. (3 body)
# Výstup jedne série bude vypadat například takto: Under the Dome, jazyk: English, hodnocení: 6.5
for serie in data:
    zanry = serie["genres"]
    if "Drama" in zanry:
        jmeno = serie["name"]
        jazyk = serie["language"]
        hodnoceni = serie['rating']['average']
        print(f"{jmeno}, jazyk: {jazyk}, hodnocení: {hodnoceni}")
