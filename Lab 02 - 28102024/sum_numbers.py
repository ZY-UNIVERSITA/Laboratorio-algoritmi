# TEST FUNCTION
def gauss(a, b):
    return (a+b) * (b-a+1) / 2

test = [ (0, x, gauss(0, x)) for x in range(0, 100, 4) ]

# FUNCTION sum_numbers
def sum_numbers(a, b):
    if b == a:
        return a
    return b + sum_numbers(a, b-1)

# RUN TEST
for tuple in test:
    a = tuple[0]
    b = tuple[1]
    result = tuple[2]
    sumNumbersValue = sum_numbers(a, b)

    separatore = '-' * 100

    print(f"La somma dei valori da {a} a {b} è: {result}")
    print(f"La funzione sum_numbers restituisce {sumNumbersValue}")
    if sumNumbersValue == result:
        print(f"Va bene")
    else:
        print(f"Non va bene")
    
    print(separatore)