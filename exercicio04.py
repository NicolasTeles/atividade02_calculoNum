import sympy as sp
TOLERANCIA_X = 1e-5
TOLERANCIA_FUNCOES = 1e-7

def metodoNewtonRaphson(x, f, g):
    # print(f.subs(x, 0.5).evalf())   ~ -4.1
    # print(f.subs(x, 2).evalf())     ~ 2.4
    
    # portanto valor de x deve estar entre 0.5 e 2, por isso iniciando x com valor 1
    x_novo = 1
    derivada_f = sp.diff(f, x)
    
    x_antigo = x_novo
    iteracoes = 0
    
    while True:

        x_novo = sp.simplify(x_novo - f.subs(x, x_novo)/derivada_f.subs(x, x_novo))

        iteracoes += 1
        
        if abs(x_novo - x_antigo) < TOLERANCIA_X and abs(f.subs(x, x_novo)) < TOLERANCIA_FUNCOES:
            break
        x_antigo = x_novo
        
    print(f"valor da variavel: {x_novo}")
    print(f"valor da funcao: {f.subs(x, x_novo)}")
    print(f"{iteracoes} iteracoes para atingir a precisao da variavel e sua funcao da letra a")
    
    iteracoes = 0
    derivada_g = sp.diff(g, x)
    
    # print(g.subs(x, -2).evalf())   ~ -1.275
    # print(g.subs(x, -1).evalf())     ~ 4.4
    
    # portanto valor de x deve estar entre -2 e -1, por isso iniciando x com valor -1.5
    
    x_novo = -1.5
    x_antigo = x_novo
    
    while True:

        x_novo = sp.simplify(x_novo - g.subs(x, x_novo)/derivada_g.subs(x, x_novo)).evalf()

        iteracoes += 1
        
        if abs(x_novo - x_antigo) < TOLERANCIA_X and abs(g.subs(x, x_novo)) < TOLERANCIA_FUNCOES:
            break
        x_antigo = x_novo
        
    print(f"\nvalor da variavel: {x_novo}")
    print(f"valor da funcao: {g.subs(x, x_novo)}")
    print(f"{iteracoes} iteracoes para atingir a precisao da variavel e sua funcao da letra b")

def metodoSecante(x, f, g):
    # print(f.subs(x, 0.5).evalf())   ~ -4.1
    # print(f.subs(x, 2).evalf())     ~ 2.4
    
    # portanto valor de x deve estar entre 0.5 e 2, por isso iniciando os valores iniciais como os proprios 0.5 e 2
    valores_g = [0.5, 2]
    iteracoes = 0
    while True:
        xn = valores_g[iteracoes]
        xn_mais1 = valores_g[iteracoes+1]
        
        novo_x = sp.simplify(xn - f.subs(x, xn) * (xn - xn_mais1)/(f.subs(x, xn) - f.subs(x, xn_mais1))).evalf()
        valores_g.append(novo_x)
        iteracoes += 1
        
        if f.subs(x, novo_x) < TOLERANCIA_FUNCOES and abs(novo_x - xn_mais1) < TOLERANCIA_X:
            break
        print(novo_x)
    print(f"\nvalor da variavel: {valores_g[-1]}")
    print(f"valor da funcao: {f.subs(x, valores_g[-1])}")
    print(f"{iteracoes} iteracoes para atingir a precisao da variavel e sua funcao da letra a")
    
    # print(g.subs(x, -2).evalf())   ~ -1.275
    # print(g.subs(x, -1).evalf())     ~ 4.4
    
    # portanto valor de x deve estar entre -2 e -1, por isso tendo valores iniciais como os próprios -2 e -1
    
    iteracoes = 0
    valores_g = [-2, -1]
    iteracoes = 0
    while True:
        xn = valores_g[iteracoes]
        xn_mais1 = valores_g[iteracoes+1]
        
        novo_x = sp.simplify(xn - g.subs(x, xn) * (xn - xn_mais1)/(g.subs(x, xn) - g.subs(x, xn_mais1))).evalf()
        valores_g.append(novo_x)
        iteracoes += 1
        
        if g.subs(x, novo_x) < TOLERANCIA_FUNCOES and abs(novo_x - xn_mais1) < TOLERANCIA_X:
            break
    print(f"\nvalor da variavel: {valores_g[-1]}")
    print(f"valor da funcao: {g.subs(x, valores_g[-1])}")
    print(f"{iteracoes} iteracoes para atingir a precisao da variavel e sua funcao da letra b")

def metodoBissecao(x, f, g):
    # print(f.subs(x, 0.5).evalf())   ~ -4.1
    # print(f.subs(x, 2).evalf())     ~ 2.4
    
    # portanto valor de x deve estar entre 0.5 e 2, portanto os limites iniciais do intervalo serao 0.5 e 2
    
    limite_esq = 0.5
    limite_dir = 2
    array_pontos_medios = [0.5]
    iteracoes = 0
    while True:
        ponto_medio = (limite_esq + limite_dir)/2
        if(f.subs(x, ponto_medio).evalf() > 0):
            limite_dir = ponto_medio
        else:
            limite_esq = ponto_medio
        array_pontos_medios.append(ponto_medio)
        iteracoes += 1
        if f.subs(x, ponto_medio).evalf() < TOLERANCIA_FUNCOES and abs(ponto_medio - array_pontos_medios[-2]) < TOLERANCIA_X:
                break
    print(f"\nvalor da variavel: {array_pontos_medios[-1]}")
    print(f"valor da funcao: {f.subs(x, array_pontos_medios[-1])}")
    print(f"{iteracoes} iteracoes para atingir a precisao da variavel e sua funcao da letra a")
    
    # print(g.subs(x, -2).evalf())   ~ -1.275
    # print(g.subs(x, -1).evalf())     ~ 4.4
    
    # portanto valor de x deve estar entre -2 e -1, portanto os limites iniciais do intervalo serao os próprios -2 e -1
    
    limite_esq = -2
    limite_dir = -1
    array_pontos_medios = [-2]
    iteracoes = 0
    while True:
        ponto_medio = (limite_esq + limite_dir)/2
        if(g.subs(x, ponto_medio).evalf() > 0):
            limite_dir = ponto_medio
        else:
            limite_esq = ponto_medio
        array_pontos_medios.append(ponto_medio)
        iteracoes += 1
        if g.subs(x, ponto_medio).evalf() < TOLERANCIA_FUNCOES and abs(ponto_medio - array_pontos_medios[-2]) < TOLERANCIA_X:
                break
    print(f"\nvalor da variavel: {array_pontos_medios[-1]}")
    print(f"valor da funcao: {g.subs(x, array_pontos_medios[-1])}")
    print(f"{iteracoes} iteracoes para atingir a precisao da variavel e sua funcao da letra b")

x = sp.symbols('x')
f = 5*sp.ln(x) - 2 +0.4*x
g = x - ((x**5 - 26)/(5 * x**4))
print("====================================================")
print("METODO NEWTON-RAPHSON:")
metodoNewtonRaphson(x, f, g)
print("====================================================")
print("METODO DA SECANTE")
metodoSecante(x, f, g)
print("====================================================")
print("METODO DA BISSECAO")
metodoBissecao(x, f, g)
print("====================================================")
