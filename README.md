# Bulls and Cows Game
Druhý projekt v rámci Python Akademie od ENGETO.
## O projektu
Jedná se o jednoduchou konzolovou hru, během které uživatel - hráč hádá čtyřciferné číslo. V tomto čísle je každá číslice jedinečná a zároveň číslo nezačíná 0. Při každém pokusu hráči program vypíše:
- *bulls*: počet správných číslic na správných pozicích v rámci daného čísla
- *cows*: počet správných číslic na špatných pozicích v rámci daného čísla

Číslo zadávané uživatelem je kontrolováno, zdali:
- neobsahuje jiné znaky než číslice
- zdali neobsahuje duplicitní číslice
- je složeno ze správného počtu číslic
- zdali nezačíná 0

## Požadavky na spuštění
Projekt vyžaduje Python 3.x. Není třeba instalovat žádné knihovny; hra využívá pouze standardní knihovny `random` a `time`.

## Použití
Na začátku hry je vygenerováno náhodné čtyřciferné číslo. Hráč je vyzván k zadání svého tipu a program mu vypíše počet *bulls* (správné číslice na správné pozici) a počet *cows* (správné číslice, ale jiné pozice). Následně je hráči umožněno zadávat své další tipy tak dlouho, dokud neuhodne správné číslo (*bulls* = 4). Poté se vypíše statistika her, konkrétně:
- počet pokusů, které hráč potřeboval k uhodnutí daného čísla
- doba trvání hry

Následně je hráči umožněno začít novou hru (zadat svůj tip na nové číslo) či ukončit hru zadáním písmene `q`.

## Ukázka průběhu
```
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.

-----------------------------------------------
Enter a number:
-----------------------------------------------

3697
2 bulls, 1 cows.
2397 
3 bulls, 0 cows.
1397

Correct, you've guessed the right number
in 3 guesses!
Your time: 14 seconds
-----------------------------------------------
That's amazing!
-----------------------------------------------

Statistics (guesses / time (s)):
. . . . . . . . . . . . . . . .
    3 / 14

-----------------------------------------------
I've generated a new 4 digit number for you.
If you'd like to play again, enter a number.
Otherwise, press "q" to quit the game.
-----------------------------------------------
