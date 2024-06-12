def multiplicar_matriz(m1, m2):
    nova_matriz = []
    nova_linha = []
    produto = 0
    for linha_m1 in m1:
        contador1 = 0
        contador2 = 0
        for linha_m2 in m2:
            produto += linha_m1[contador1] * linha_m2[contador2]
            contador1 += 1
        nova_linha.append(produto)
        contador1 = 0
        contador2 += 1
        produto = 0
        for linha_m2 in m2:
            produto += linha_m1[contador1] * linha_m2[contador2]
            contador1 += 1
        nova_linha.append(produto)
        produto = 0
        nova_matriz.append(nova_linha)
        nova_linha = []
    for linha in nova_matriz:
        print(linha)
