import json

#1 - Načtení obsahu souboru data.json
with open("data.json", encoding='utf8') as file:
    data = json.load(file)

#2 - Výpis všech studentů z načteného souboru a jejich hodnoty ( jmeno, vek, trida)
print("Všichni studenti:")
for student in data:
    print(f"Jméno: {student['jmeno']}, Věk: {student['vek']}, Třída: {student['trida']}")

#3 - Vygenerování seznamu
# Vygenerujte seznam_jidel v kterém každý vstup bude mít druh, nazev_jidla, cena.
# Minimálně 5 jídel
# Například: druh: dezert, jidlo: Čokoladová zmrzlina, cena: 30
seznam_jidel = list()
seznam_jidel.append( {"druh": "dezert", "nazev_jidla": "Čokoladová zmrzlina", "cena": 30 })
seznam_jidel.append( {"druh": "snidane", "nazev_jidla": "Ovesné vločky s ovocem a mandlovým mlékem", "cena": 40 })
seznam_jidel.append( {"druh": "svacina", "nazev_jidla": "Čerstvé ovoce (výběr: hruška, jablko, banán)", "cena": 25})
seznam_jidel.append( {"druh": "obed", "nazev_jidla": "Kuřecí kari s kořenovou zeleninou a rýží", "cena": 80})
seznam_jidel.append( {"druh": "vecere", "nazev_jidla": "Grilovaný losos s brokolicí a bramborami", "cena": 120})

#4 - Uložení seznam_jidel do out.json
with open("out.json", "w", encoding="utf8") as file:
    file.write(json.dumps(seznam_jidel))
