Probleme de satisfacere a constrângerilor
O problemă de satisfacere a constrângerilor (Constraint Satisfaction Problem):
- o mulțime de variabile X={X1,..., Xn}
- fiecare variabilă Xi poate lua valori dintr-un domeniu  Di
- o mulțime de constrângeri C={C1 ,..., Ct} care specifică combinațiile permise de valori.
O soluție pentru o astfel de problemă este o asignare de valori variabilelor a.î. toate constrângerile să fie satisfăcute.
În definiție nu se impune nici o condiție asupra tipului variabilelor. Acestea pot fi întregi, logice sau de orice alt tip. Nici modul de definire a constrângerilor nu este limitat. Constrângerile pot fi date atât explicit, prin specificarea tuplelor de valori permise, cât şi implicit, prin relații (ex: Xi > 2).
Graful restricțiilor: nodurile reprezintă variabilele, muchiile reprezintă restricțiile între variabile.
Exemplu: Problema colorării unei hărți
Considerăm o hartă cu n țări. Fiecare regiune/țară poate fi colorată cu o culoare dintr-o mulțime de culori asociate. Să se coloreze harta a.î. regiunile/țările vecine să fie colorate diferit.

Modelare: asignăm fiecărei regiuni/țări de pe hartă o variabilă; domeniul fiecărei variabile este o mulțime de culori specificată. Restricțiile sunt de forma: Xi ≠ Xj (două țări vecine au culori diferite). Obs: între două țări vecine în graful constrâns vom adăuga o muchie.

Metode de rezolvare:
- Algoritmul Backtracking: menține o soluție parțială (o mulțime de variabile instanțiate corect) pe care o extinde pas cu pas. Inițial, mulțimea este vidă. La fiecare pas se selectează următoarea variabilă din ordonare şi se încearcă asignarea variabilei cu o valoare consistentă cu instanțierea parțială. Dacă este găsită o astfel de valoare, algoritmul continuă procedeul cu următoarea variabilă din ordonare. În caz contrar, ne întoarcem la variabila anterioară şi îi asignăm o altă valoare consistentă. 

- Propagarea constrangerilor
Forward-checking: fiecare valoare aleasă trebuie să fie compatibilă cu cel puțin o valoare din domeniul variabilelor neasignate cu care au în comun o restricție. Se instanțiază variabila cu o valoare şi apoi se elimină valori din domeniul variabilelor viitoare care sunt în conflict cu instanțierea curentă. Dacă domeniul unei variabile viitoare devine vid, algoritmul consideră următoarea valoare posibilă pentru variabila curentă.

Ordonarea variabilelor
MRV (Minimum remaining values): alege variabila cu cele mai puține valori rămase în domeniu


Temă
Considerăm o tablă de dimensiune 9x9, parțial completată cu cifre de la 1 la 9. Fiecare linie, coloană sau regiune 3x3 conține toate valorile de la 1 la 9. Anumite căsuțe trebuie să conțină un număr par. Problema constă în identificarea numerelor lipsă.
Aplicați algoritmul Forward checking împreună cu o metodă de ordonare a variabilelor pentru a determina soluțiile unei instanțe date.

Exemplu: 

Soluția instanței de mai sus:


Etape
(0.3) 1. Modelarea problemei ca o problemă de satisfacere a  constrângerilor
identificarea variabilelor, domeniilor, restricțiilor 
inițializarea acestora pentru o instanță dată
(0.5) 2. Implementarea metodei Forward Checking
(0.2) 3. Implementarea metodei de ordonare a variabilelor (MRV
