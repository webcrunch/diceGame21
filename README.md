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
