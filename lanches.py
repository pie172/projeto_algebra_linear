import numpy as np

print(10*'-', 'Lanchonete Tentação na Chapa', 10*'-')

linhas1 = int(input("Digite o número de lanches: "))  
colunas1 = int(input("Digite o número de ingredientes por lanche: "))  

linhas2 = colunas1  
colunas2 = int(input("Digite o número de mercados: "))  

if colunas1 != linhas2:
    print("Não foi possível multiplicar pois as colunas da primeira matriz devem ser iguais às linhas da segunda matriz.")
else:
    matriz1 = np.zeros((linhas1, colunas1))
    print("Insira a quantidade de ingredientes para cada lanche:")
    for i in range(linhas1):
        print(f"Lanche {i + 1}:")
        for j in range(colunas1):
            matriz1[i, j] = float(input(f"Ingrediente {j + 1}: "))

    matriz2 = np.zeros((linhas2, colunas2))
    print("Insira o preço de cada ingrediente em cada mercado:")
    for i in range(linhas2):
        print(f"Ingrediente {i + 1}:")
        for j in range(colunas2):
            matriz2[i, j] = float(input(f"Mercado {j + 1}: "))

    resultado = np.dot(matriz1, matriz2)  
    print("\nCusto total do lanche em cada mercado:")
    print(np.round(resultado, decimals=2))

    lucro = resultado * 1.5  
    print("\nPreço do lanche com lucro de 50%:")
    print(np.round(lucro, decimals=2))
