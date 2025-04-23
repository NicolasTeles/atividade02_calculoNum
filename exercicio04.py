import sympy as sp

def metodoNewtonRaphson(variavel: str):
    x_iterativo = 10
    for i in range(10):
        x = sp.symbols(variavel)
        f = 5*sp.ln(x) - 2 +0.4*x
        derivada_f = sp.diff(f, x)

        x_iterativo = x_iterativo + f.subs(x, x_iterativo)/derivada_f.subs(x, x_iterativo)

        # g = x - ((x**5 - 26)/(5 * x**4))
        # derivada_g = sp.diff(g, x)
    print(f.subs(x, x_iterativo))
    
metodoNewtonRaphson('x')