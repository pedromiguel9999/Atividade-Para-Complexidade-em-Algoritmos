"""
Atividade — Complexidade em Algoritmos
======================================

Autor: Pedro Miguel
Data: 21/10/2025

Descrição:
Este arquivo contém três exemplos de algoritmos Python
com diferentes níveis de complexidade (Notação Big-O).
São eles:
1. O(1) — Acesso constante a um elemento;
2. O(n) — Soma linear de uma lista;
3. O(n²) — Verificação de duplicados com laços aninhados.
"""

# -------------------------------------------
# Algoritmo 1 — Complexidade Constante O(1)
# -------------------------------------------

def acesso_constante(lista):
    """
    Retorna o primeiro elemento da lista (O(1)).
    O tempo não depende do tamanho da lista.
    """
    if lista:
        return lista[0]
    return None


# Teste
if __name__ == "__main__":
    valores = [10, 20, 30, 40]
    print("Primeiro elemento:", acesso_constante(valores))


# -------------------------------------------
# Algoritmo 2 — Complexidade Linear O(n)
# -------------------------------------------

def soma_lista(lista):
    """
    Retorna a soma de todos os elementos da lista (O(n)).
    O tempo cresce linearmente com o tamanho da entrada.
    """
    soma = 0
    for numero in lista:
        soma += numero
    return soma


# Teste
if __name__ == "__main__":
    valores = [1, 2, 3, 4, 5, 6]
    print("Soma da lista:", soma_lista(valores))


# -------------------------------------------
# Algoritmo 3 — Complexidade Quadrática O(n²)
# -------------------------------------------

def possui_duplicados(lista):
    """
    Verifica se há elementos duplicados (O(n²)).
    Usa dois laços aninhados para comparar cada par.
    """
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False


# Testes
if __name__ == "__main__":
    print("Lista [1, 2, 3, 4] tem duplicados?", possui_duplicados([1, 2, 3, 4]))
    print("Lista [1, 2, 3, 1] tem duplicados?", possui_duplicados([1, 2, 3, 1]))
