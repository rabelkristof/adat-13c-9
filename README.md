# Bolyai Labs – Feladatkártya #2: A hívásnapló megtisztítása

> Adatelemzőként szeretném, hogy a hívásnapló tiszta és egységes legyen, hogy a következő blokkokban a modellek megbízható adatból tanuljanak.

## Elfogadási feltételek

- [ ] saját repó ebből a sablonból (név például `adat-13b-07`, láthatóság: Public)
- [ ] az `adattisztitas.ipynb` minden `TODO`-ja kitöltve, az önellenőrző cella hiba nélkül lefut
- [ ] a notebook visszamentve a repóba Colabból, a megadott commitüzenettel
- [ ] a CI-futás zöld (Actions fül)
- [ ] a repó linkje beadva a Teams-feladatba

**Határidő:** a 2. óra vége · **Érték:** 5 sprintpont (zöld build 2, határidő 1, commitüzenet 1, kilépőkérdések 1)

## Lépések

1. **Saját repó:** ezen az oldalon **Use this template → Create a new repository**. Név: `adat-` + osztálykód + sorszám (pl. `adat-13b-07`), **Public**.
2. **Megnyitás Colabban:** [colab.research.google.com](https://colab.research.google.com) → **File → Open notebook → GitHub** fül → keress rá a felhasználónevedre → válaszd a repódat és az `adattisztitas.ipynb`-t.
3. **Munka:** futtasd a cellákat sorban, töltsd ki a hét `TODO`-t (a–g), válaszolj a feltárási kérdésekre.
4. **Önellenőrzés:** a 3. részben lévő cella hiba nélkül fusson le.
5. **Mentés:** **File → Save a copy in GitHub** → a saját repód, `main` ág, fájlnév `adattisztitas.ipynb`, commitüzenet: `feat: hívásnapló tisztítása (feladatkártya #2)`. Az első mentésnél a Colab engedélyt kér a GitHubhoz: fogadd el.
6. **Zöld build és beadás:** a repód **Actions** fülén várd meg a futást, zöld build után add be a repó linkjét a Teams-feladatba.

A CI lefuttatja az egész notebookot, és a kimentett `data/hivasok_tiszta.csv` fájlt ellenőrzi.

## Ha elakadsz

| Tünet | Megoldás |
| --- | --- |
| `TypeError` vagy `AttributeError` egy `...` sornál | Az adott `TODO` még nincs kitöltve: a `...` helyére írd a megoldást |
| Az önellenőrzés „b) A modellnevek még nem egységesek” hibát ír | Először `.str.strip()`, utána `.str.lower()` |
| „c) A sikeres oszlopban nem csak 0 és 1 van” | Kisbetűsítés nélkül a `True`/`False` nem talál a szótárban |
| Piros build, „X sor maradt, Y kellene” | A lépések sorrendje számít: a–g sorrendben futtasd, a notebook elejétől (Runtime → Run all) |
| A Colab nem találja a repódat | A GitHub fülön jelentkezz be, és engedélyezd a Colabnak a hozzáférést |

## Két szabály egész évre

1. API-kulcs és személyes adat soha nem kerül commitba vagy promptba.
2. Az MI által írt kódot is érteni kell. Amit nem tudsz elmagyarázni, azt nem adod be.
