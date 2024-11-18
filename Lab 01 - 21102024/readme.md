# Corso *Algoritmi e Strutture Dati*: Laboratorio

Gli esercizi di ogni laboratorio sono contenuti in  `asd-labs/<NOME-LAB>/`. 

## Lab `time` (2024-10-21): Misura dei tempi d'esecuzione di funzioni
<a name="lab-time"></a>

Consultando le slide sulla misura dei tempi d'esecuzione in Python, si svolgano i seguenti esercizi:

0. *[Tempo stimato: 15']* Riscaldamento (`pow.py`): Implementare `pow(a,n)` (elevamento a potenza) in modo *ricorsivo*
    - Considerare l'approccio divide-et-impera, basato su tre fasi (divide, impera, combine)
    - Per verificare la correttezza della soluzione, prevedere alcuni test automatici (riusando `math.pow` ed eventualmente `math.isclose` per gestire confronto fra numeri floating point)
    - Rispondere alla domanda: la funzione ricorsiva implementata di quale tipologia di ricorsione è? E' tail recursive?
    - Una lista di tuple rappresentanti diversi test case può essere generata comodamente come segue:
```
pow_tests = [((a, n), math.pow(a, n)) for a, n in [(0,5), (5,0), (3,3), (2,8), (2,-3)]]
```
1. *[Tempo stimato: 30']* Si consideri **`measure-fib.py`**. Si misuri e si confronti il tempo d'esecuzione di `fib` (Fibonacci in versione ricorsiva) e `fib_iter` (Fibonacci in versione iterativa). Si utilizzino i *millisecondi* come unità di misura.
    * Si definisca una funzione `measure_running_time(f)` che restituisca il tempo d'esecuzione della funzione `f` fornita in input e la si applichi a `fib` e `fib_iter` per input 10, 20, 30.
        * Si implementi la funzione in due varianti: una usando `time.perf_counter()` e l'altra usando `timeit.repeat`
    * DOMANDA: Quale tra `fib` e `fib_iter` dà luogo a tempi d'esecuzione minori?
    * Esempio di output del programma da implementare:
```
[perf_counter ] fib_rec(5) took 1.347306533716619e-06 sec 	 fib_iter(5) took 1.0011048289015888e-06 sec
[timeit.repeat] fib_rec(5) took 5.810987204313279e-07 sec 	 fib_iter(5) took 4.1349849198013546e-07 sec

[perf_counter ] fib_rec(10) took 7.195401121862233e-06 sec 	 fib_iter(10) took 7.672031642869115e-07 sec
[timeit.repeat] fib_rec(10) took 6.401899736374617e-06 sec 	 fib_iter(10) took 5.166017217561602e-07 sec

...
```
2. *[Tempo stimato: 15']* Si consideri **`profile-function.py`**. Si utilizzi `cProfile` per profilare `function_to_be_profiled()`
    * Qual è la parte più lenta di `function_to_be_profiled()`?
    * Dovresti ottenere un output simile al seguente:
```
### Profiling for n=1000 ###

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 cProfile.py:133(__exit__)
        1    0.000    0.000    0.000    0.000 profile-function-sol.py:17(create_list)
        1    0.000    0.000    0.056    0.056 profile-function-sol.py:20(function_to_be_profiled)
        1    0.056    0.056    0.056    0.056 profile-function-sol.py:4(selection_sort)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
3. *[Tempo stimato: 10']* Consultare la pagina [TimeComplexity (python.org)](https://wiki.python.org/moin/TimeComplexity) che documenta la complessità in tempo di varie operazioni su strutture dati nell'implementazione Python `CPython`. Ci si concentri in particulare sulle operazioni su `list`.
    - Si noti come sia importante per chi programma in un linguaggio conoscere la complessità delle funzioni che utilizza.
    - Più avanti nel corso vedremo queste strutture dati e capiremo da dove vengono fuori questi upper bound all'efficienza asintotica
4. *[Tempo stimato: 30']* Si legga la descrizione del progetto [`big-O`](https://pypi.org/project/big-O/)
    * Si rifletta sul problema generale: dedurre la forma/formula di una funzione a partire da punti (e.g., coppie (x,y)). Un approccio è quello della cosiddetta [regression analysis](https://en.wikipedia.org/wiki/Regression_analysis), dove si considera una certa forma di funzione (ad es `ax+b` per una retta), e si cerca di trovare i valori dei parametri `a` e `b` che meglio corrispondano ai dati (*regressione lineare*).
    * Completamento di **`bigo-fib.py`**: si provi, consultando la documentazione, ad applicare il modulo allo scopo di inferire il comportamento asintotico di Fibonacci in versione ricorsiva ed iterativa.
    * Esempio di output atteso:
```
FIB_REC:  Exponential: time = 3.5E-06 * 1.6^n (sec)
FIB_ITER:  Linear: time = -8.5E-05 + 3.6E-06*n (sec)
```



<!--

## Lab 02: Ricorsione in Python
<a name="lab02-recursion"></a>


1. [Tempo stimato: 60'] Studio sorgenti dati
    - `02-recursion-hanoi.py`: implementazione della soluzione ricorsiva al problema della Torre di Hanoi
    - `02-recursion-types.py`: implementazione di algoritmi ricorsivi per le tipologie di ricorsione viste a lezione
2. [Tempo stimato: 60'] Esercizi sulla ricorsione (NOTA: oltre all'implementazione della soluzione, prevedere una serie di test per verificarne la correttezza)
    - Implementare `sum_numbers(a,b)` (somma di tutti i numeri interi compresi tra `a` e `b`) in modo *ricorsivo*
    - Implementare `pow(a,n)` (elevamento a potenza) in modo *ricorsivo*
    - Implementare `list_contains(lst,elem)` (funzione che restituisce `True` se `elem` è contenuto nella lista `lst` o `False` altrimenti) in modo *ricorsivo*
    - Implementare `palindrome(string)` (funzione che restituisce `True` se `string` è una stringa palindroma) in modo *ricorsivo*
        - Un [palindromo](https://it.wikipedia.org/wiki/Palindromo) è una sequenza di caratteri che, letta al contrario, rimane invariata.  Esempio: `emme`, `siris`
    - Implementare `filter(lst,pred)` (funzione che restituisce una nuova lista con soli gli element idi `lst` che soddisfano la funzione predicato `pred`) in modo ricorsivo

<!--

## Lab 01: Semplici algoritmi in Python
<a name="lab01-simple-algorithms"></a>

ISTRUZIONI: leggere attentamente i passi seguenti. Completare ogni passo prima di passare al successivo.

1. [Tempo stimato: 45'] Studio sorgente `01-intro-algorithms.py` 
    - Questo sorgente include implementazioni di algoritmi molto semplici.
    - E' organizzato in modo tale da semplificare il testing di funzioni realizzate, sfruttando una funzion `test`.
    - COSA FARE:
        1. cercare di capire come si comporta il programma (PRIMA DI ESEGUIRE).
        2. eseguire lo script
        3. approfondire la comprensione dello script, consultando slide e/o documentazione
        4. prendere nota di tutti gli elementi nel codice che non sono chiari: 
    - DOMANDA: quale proprietà desiderata degli algoritmi si intende verificare con la funzione `test`?
2. [Tempo stimato: 45'] Estendere il sorgente dato implementando i seguenti algoritmi (con test):
    1. una funzione `fact(n)` per il calcolo del fattoriale di un numero `n` dato
    2. una funzione `compute_perimeter(shape,*kargs)` per il calcolo del perimetro di una forma `shape` sulla base di una sequenza di parametri `kargs` (da passare dipendentemente dalla forma)
        - lo si computi per rettangolo, quadrato, e cerchio
3. [Tempo stimato: 30'] Realizzare un nuovo script che implementi un algoritmo per il gioco `guess-a-number`
    - Di cosa si tratta: è un gioco che coinvolge un banco e un giocatore. Il banco sceglie casualmente un numero segreto da indovinare (ad es. 7). Il giocatore non conosce tale numero, e dispone di un certo numero di tentativi per indovinarlo. Il banco chiede ripetutamente al giocatore un tentativo, fino a vittoria (il giocatore ha indovinato il segreto) o sconfitta (il giocatore ha esaurito il numero di tentativi); ad ogni risposta errata del giocatore, il banco fornisce un indizio, ovvero l'indicazione se il numero tentativo proposto è più grande o più piccolo del segreto; il giocatore può dunque usare tale informazione per correggere il tentativo seguente.
    - Input:
        - range di valori `(min,max)` del gioco
        - numero max di tentativi ammessi
    - Output:
        - stampa in stdout della stringa `WON` in caso di vittoria e della stringa `LOSS` in caso di sconfitta
    - Consigli
        - si veda [`random.randint()`](https://docs.python.org/3/library/random.html?highlight=randint#random.randint)

-->