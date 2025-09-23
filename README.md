# 🎲 Blackjack-inspirerat tärningsspel

Detta är ett enkelt tärningsspel för terminalen, inspirerat av Blackjack. Spelaren tävlar mot en datorstyrd dealer med målet att få en total poäng så nära 21 som möjligt utan att gå över. Projektet är byggt i Python och uppfyller kraven för en kursuppgift.

---

## 🧩 Funktioner

- **Spelar- och dealerlogik**: Spelet hanterar turer för både en mänsklig spelare och en datorstyrd dealer.
- **Highscore**: Antal vinster för spelare och dealer sparas i filen `scores.txt` mellan spelomgångar.
- **Modulär kod**: Koden är uppdelad i separata filer (`main.py`, `Player.py`, `Game.py`, `Utils.py`) för bättre struktur och underhållbarhet.
- **Testsvit**: Projektet inkluderar en testfil (`test_game.py`) som verifierar spelets kärnlogik.

---

## ▶️ Hur man kör spelet

1. Klona eller ladda ned projektet till din lokala maskin.
2. Navigera till projektkatalogen i din terminal.
3. Kör huvudfilen med följande kommando:

```bash
python main.py
```

---
## 🎮 Hur man spelar
Spelet guidar dig genom varje runda. Du kommer att få alternativet att antingen "rulla" tärningen för att öka din poäng, eller "stanna" när du är nöjd.

Vinn: Få högre poäng än dealern, utan att överstiga 21.

Förlora: Få en poäng som är högre än 21.

Oavgjort: Få samma poäng som dealern.


---
## 📁 Projektstruktur
Följande filer utgör projektet:

- main.py: Startpunkten för spelet.

- Player.py: Klass som representerar en spelare (både den mänskliga spelaren och dealern).

- Game.py: Klass som hanterar spelets huvudlogik och flöde.

- Utils.py: Fil med generella hjälpfunktioner, inklusive vinnarlogiken.

- scores.txt: Textfil för att spara highscore.

- test_game.py: Testfilen för att validera spelets funktionalitet.


---

## ✅ Tester
För att köra testerna, använd följande kommando i din terminal:

```bash
python -m unittest test_game.py
```

##### Detta är hur testerna kommer att se ut, :

Jag har lagt till ett felande test med. 

```bash
--- Scenario: Dealer-logik stannar vid 17+ ---
✅ Test 2: Dealerns poäng 20 är korrekt.
.
--- Scenario: Tärningskast är giltigt ---
✅ Test 1: Tärningskastet 5 är inom intervallet 1-6.
.
--- Scenario: Vinnare bestäms korrekt ---
Du vinner! Din poäng är närmare 21 än dealerns.
Du förlorar. Dealerns poäng är närmare 21 än din.
Du förlorade, eftersom din poäng är över 21.
Du vinner! Dealerns poäng är över 21.
Det blev oavgjort!
✅ Test 3: Vinnarbestämning fungerar i alla scenarion.
.
--- Scenario: Simulerar ett fallerande vinnartest ---
Du vinner! Din poäng är närmare 21 än dealerns.
❌ Simulerat fallerande test - misslyckades korrekt.
Förväntat: 'draw', men fick: 'player'
F
--- Scenario: Highscore kan läsas in från en fil ---
✅ Test: Inläsning av highscore från fil fungerar.
.
--- Scenario: Standardpoäng laddas om filen inte finns ---
✅ Test: Standardpoäng laddas när fil inte finns.
.
--- Scenario: Highscore kan sparas till en fil ---
✅ Test: Spara highscore till fil fungerar.
.
```
---





