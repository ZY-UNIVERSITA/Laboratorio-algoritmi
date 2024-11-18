## Lab `plotting` + `recursion` (2024-10-28): Grafici di funzioni ed esercizi sulla ricorsione

#### Parte `plotting`

Razionale/obiettivo: acquisire familiarità con funzioni di diverse classi di complessità, e imparare a graficare dati per ottenere rappresentazioni utili allo studio e all'indagine.

1. *[Tempo stimato: 45']* Si utilizzi `matplotlib` per costruire un'immagine simile a quella sottostante
    * Si faccia riferimento alle slide, al notebook in `notebooks/matplotlib.ipynb`, agli **esempi** inclusi in [code-python/mpl/](code-python/mpl/)
        * oltre che al [cheatsheet](https://matplotlib.org/cheatsheets/cheatsheets.pdf), alla [guida](https://matplotlib.org/stable/users/explain/quick_start.html), e alla [API Reference](https://matplotlib.org/stable/api/index.html) 
    * Alcune indicazioni:
        * Si può stabilire una lista di funzioni da graficare con: `functions = [float, math.log, lambda n: n*math.log(n), ...]`
        * Si può usare `x_points = np.linspace(...)` per individuare i valori dell'asse `x` da produrre
        * Si può produrre le ordinate dei punti da graficare per ogni funzione con qualcosa del tipo:
        `y_points = np.array([some_function(x) for x in x_points])`
        * Si può plottare con `plot(x_points, y_points)`
        * Si può voler limitare l'asse y mediante la funzione `ylim(min,max)`
        * Si può usare `Axes#xscale("log")` per impostare una scala logaritmica sull'asse x 
        * Si pul usare `Axes#text(x,y,s)` per posizionare un'etichetta con testo `s` al punto `(x,y)` del grafico
        * Si può usare `list(map(f,l))` per produrre una lista applicando `f` ad ogni elemento della lista `l`. Un'alternativa con NumPy potrebbe essere: usare `fvec = np.vectorize(f)` per ottenere una funzione `fvec` che usi `f` per lavorare su array in modo member-wise (cf. broadcasting).
        * Al posto della funzione fattoriale, si può considerare la funzione [gamma](https://en.wikipedia.org/wiki/Gamma_function), che è una generalizzazione del fattoriale su valori reali. In Python: `math.gamma()`
![](imgs/functions.png)

#### Parte `recursion`

Razionale/obiettivo: acquisire familiarità con la ricorsione.

2. [Tempo stimato: 30'] Studio sorgenti dati
    - `02-recursion-hanoi.py`: implementazione della soluzione ricorsiva al problema della Torre di Hanoi
    - `02-recursion-types.py`: implementazione di algoritmi ricorsivi per le tipologie di ricorsione viste a lezione
3. [Tempo stimato: 15'] Esercizi sulla ricorsione (NOTA: oltre all'implementazione della soluzione, prevedere una serie di test per verificarne la correttezza). Si possono creare nuovi file `.py`. Prevedere sia il codice della funzione sia un test minimale della funzionalità (ad es., con stampe in output per un set di input rappresentativo).
    - Implementare `sum_numbers(a,b)` (somma di tutti i numeri interi compresi tra `a` e `b`) in modo *ricorsivo*
    - Implementare `list_contains(lst,elem)` (funzione che restituisce `True` se `elem` è contenuto nella lista `lst` o `False` altrimenti) in modo *ricorsivo*