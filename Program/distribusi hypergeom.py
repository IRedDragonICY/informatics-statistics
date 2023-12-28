from scipy.stats import hypergeom
from scipy.special import comb as C
from sympy import *
import math

subscript   = str.maketrans("0123456789()", "₀₁₂₃₄₅₆₇₈₉₍₎")
superscript = str.maketrans("0123456789()", "⁰¹²³⁴⁵⁶⁷⁸⁹⁽⁾")

N = 10
n = 5
k = 8
x = [i for i in range(0, 2+1)]
h = hypergeom(N, n, k)



def calculate_hypergeometric_distribution(x):
    probability = []
    for i in range(len(x)):
        # reset format

        print(f"x = {x[i]}")
        expr0 = Eq(Symbol(f"h(x;N,n,k)"), Symbol(f"C{str((k,x[i])).translate(subscript)} * C{str((N-k,n-x[i])).translate(subscript)} / C{str((N,n)).translate(subscript)}"))
        pprint(expr0)

        expr1 = Eq(Symbol(f"h({x[i]};{N},{n},{k})"), Symbol(f"C({k},{x[i]}) * C({N-k},{n-x[i]}) / C({N},{n})"))
        pprint(expr1) 

        expr3 = (Symbol(f"h({x[i]};{N},{n},{k}) = {C(k,x[i])} * {C(N-k,n-x[i])} / {C(N,n)}"))
        pprint(expr3)

        expr4 = Eq(Symbol(f"h({x[i]};{N},{n},{k})"), simplify(Rational(C(k, x[i]) * C(N - k, n - x[i]), C(N, n))))
        pprint(expr4)

        expr5 = Eq(Symbol(f"h({x[i]};{N},{n},{k})"), h.pmf(x[i]))
        pprint(expr5)

        probability.append(h.pmf(x[i]))
    # penjumlahan probabilitas
    print((f"probability₍ₓ₌{','.join([str(xi).translate(subscript) for xi in x])}₎ = {' + '.join(str(prob) for prob in probability)}"))
    return f"probability₍ₓ₌{','.join([str(xi).translate(subscript) for xi in x])}₎ = {sum(probability)}"


# def calculate_joint_probability(x):
#     probability = []
#     for i in range(len(x)):
#         expr0 = Eq(Symbol(f"h(x;N,n,k)"), Symbol(f"C(k,x[i]) * C(N-k,n-x[i]) / C(N,n)"))
#         pprint(expr0)

#         expr1 = Eq(Symbol(f"h({x[i]};{N},{n},{k})"), Symbol(f"C({k},{x[i]}) * C({N-k},{n-x[i]}) / C({N},{n})"))
#         pprint(expr1) 

#         expr3 = (Symbol(f"h({x[i]};{N},{n},{k}) = {C(k,x[i])} * {C(N-k,n-x[i])} / {C(N,n)}"))
#         pprint(expr3)

#         expr4 = Eq(Symbol(f"h({x[i]};{N},{n},{k})"), simplify(Rational(C(k, x[i]) * C(N - k, n - x[i]), C(N, n))))
#         pprint(expr4)  

#         expr5 = Eq(Symbol(f"h({x[i]};{N},{n},{k})"), h.pmf(x[i]))
#         pprint(expr5)

#         probability.append(h.pmf(x[i]))
#     return math.prod(probability)



print(calculate_hypergeometric_distribution(x))





