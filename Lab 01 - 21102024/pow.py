import math # cf. math.pow, math.isclose

def pow(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * pow(a, n-1)
    else:
        return 1/a * pow(a, n+1)
    pass


def test(f, tests):
    separatore = '-' * 100
    for i, t in enumerate(tests):
        print(f"Test {i}) Testing {f.__name__}({t[0]})")
        print(f"{t[0][0]} e {t[0][1]} deve essere uguale a {t[1]}")
        potenza = pow(t[0][0], t[0][1])
        potenzaCorretta = t[1]
        if (potenza  == potenzaCorretta):
            print(f"Tutto ok. {potenza} è uguale a {potenzaCorretta}")
        
        print(f"{separatore}")
    pass

pow_tests = [((a, n), math.pow(a, n)) for a, n in [(0,5), (5,0), (3,3), (2,8), (2,-3)]]
test(pow, pow_tests)