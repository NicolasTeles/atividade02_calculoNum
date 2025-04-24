import sympy as sp

def metodoNewtonRaphson(variavel: str):
    x = sp.symbols(variavel)
    f = 5*sp.ln(x) - 2 +0.4*x
    
    # print(f.subs(x, 0.5).evalf())   ~ -4.1
    # print(f.subs(x, 2).evalf())     ~ 2.4
    
    # portanto valor de x deve estar entre 0.5 e 2, por isso iniciando x com valor 1
    x_novo = 1
    derivada_f = sp.diff(f, x)
    
    tolerancia_x = 1e-5
    tolerancia_funcoes = 1e-7
    x_antigo = x_novo
    iteracoes = 0
    
    while True:

        x_novo = sp.simplify(x_novo - f.subs(x, x_novo)/derivada_f.subs(x, x_novo))

        iteracoes += 1
        
        if abs(x_novo - x_antigo) < tolerancia_x and abs(f.subs(x, x_novo)) < tolerancia_funcoes:
            break
        x_antigo = x_novo
        
    print(f"valor da variavel: {x_novo}")
    print(f"valor da funcao: {f.subs(x, x_novo)}")
    print(f"{iteracoes} iteracoes para atingir a precisao da variavel e sua funcao da letra a")
    
    iteracoes = 0
    g = x - ((x**5 - 26)/(5 * x**4))
    derivada_g = sp.diff(g, x)
    
    # print(g.subs(x, -2).evalf())   ~ -1.275
    # print(g.subs(x, -1).evalf())     ~ 4.4
    
    # portanto valor de x deve estar entre -2 e -1, por isso iniciando x com valor -1.5
    
    x_novo = -1.5
    x_antigo = x_novo
    
    while True:

        x_novo = sp.simplify(x_novo - g.subs(x, x_novo)/derivada_g.subs(x, x_novo))

        iteracoes += 1
        
        if abs(x_novo - x_antigo) < tolerancia_x and abs(g.subs(x, x_novo)) < tolerancia_funcoes:
            break
        x_antigo = x_novo
        
    print(f"\nvalor da variavel: {x_novo}")
    print(f"valor da funcao: {g.subs(x, x_novo)}")
    print(f"{iteracoes} iteracoes para atingir a precisao da variavel e sua funcao da letra b")

metodoNewtonRaphson('x')