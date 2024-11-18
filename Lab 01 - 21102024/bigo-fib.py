import big_o

def fib(n):
    if n <= 2: return n
    return fib(n-2) + fib(n-1)

def fib_iter(n):
    if n <= 2: return n
    a, b = 0, 1
    for i in range(0,n):
        a, b = b, a+b
    return b

# TODO: use big_o to analyse the complexity of `fib` and `fib_iter`
# crea 2 variabili dette best e others
# assegna a best il primo valore dell'array e a others tutti gli altri
# big_o.big_o = è un metodo della classe libreria big_o
# fib = funzione da analizzare
# big_o.datagen.n_ = generatore di sequenza di numeri di tipo intero
# min_n e max_n = è il range di valori che datagen.n_ usa per generare i valori
# n_repeats = la funzione "fib" viene eseguita usando come argomento la lista generata da datagen.n_ e questa funzione viene eseguita 20 volte per ottenere una media del tempo
best, others = big_o.big_o(fib, big_o.datagen.n_, n_repeats=20, min_n=2, max_n=25)
print(best)

best, others = big_o.big_o(fib_iter, big_o.datagen.n_, n_repeats=20, min_n=2, max_n=25)
print(best)