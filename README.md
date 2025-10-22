
Complexidade em Algoritmos

 Pedro Miguel  





 Objetivo

Demonstrar, através de três algoritmos em Python, o comportamento da **complexidade de tempo** em diferentes níveis (O(1), O(n), O(n²)).  
Cada algoritmo é documentado, testado e explicado detalhadamente.
 Algoritmo 1 — Complexidade Constante O(1)
 Descrição
O tempo de execução **não depende** do tamanho da entrada.  
O algoritmo acessa o primeiro elemento de uma lista — uma operação direta e imediata.

Código

```python
def acesso_constante(lista):
    if lista:
        return lista[0]
    return None

# Teste
valores = [10, 20, 30, 40]
print("Primeiro elemento:", acesso_constante(valores))
```

### 📊 Análise
- **Complexidade de Tempo:** O(1)  
- **Complexidade de Espaço:** O(1)  
- **Explicação:** O acesso direto por índice é sempre constante, independentemente do tamanho da lista.

---

Algoritmo 2 — Complexidade Linear O(n)

Descrição
O tempo de execução **cresce proporcionalmente** ao tamanho da entrada.  
A função percorre toda a lista somando seus elementos.

### 💻 Código
python
def soma_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

# Teste
valores = [1, 2, 3, 4, 5, 6]
print("Soma da lista:", soma_lista(valores))
```

### 📊 Análise
- **Complexidade de Tempo:** O(n)  
- **Complexidade de Espaço:** O(1)  
- **Explicação:** Cada elemento é processado uma vez, logo o tempo cresce linearmente.

---

## 🔢 Algoritmo 3 — Complexidade Quadrática O(n²)

### 🧠 Descrição
O tempo de execução **cresce exponencialmente** conforme o tamanho da entrada.  
A função compara todos os pares de elementos da lista para verificar duplicidade.

### 💻 Código

```python
def possui_duplicados(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

# Testes
print("Lista [1, 2, 3, 4] tem duplicados?", possui_duplicados([1, 2, 3, 4]))
print("Lista [1, 2, 3, 1] tem duplicados?", possui_duplicados([1, 2, 3, 1]))
```
 Análise
- **Complexidade de Tempo:** O(n²)  
- **Complexidade de Espaço:** O(1)  
- **Explicação:** Cada elemento é comparado com todos os outros, criando crescimento quadrático.

---

Comparativo de Complexidades

| Algoritmo             | Descrição                      | Complexidade |
|-----------------------|--------------------------------|--------------|
| Acesso Constante      | Retorna o primeiro elemento    | O(1)         |
| Soma Linear           | Soma todos os elementos        | O(n)         |
| Comparação Quadrática | Verifica duplicados            | O(n²)        |



 Conclusão

Os exemplos demonstram que o **crescimento da complexidade** influencia diretamente o desempenho.  
Quanto maior a ordem de crescimento (por exemplo, O(n²)), mais lenta se torna a execução para grandes entradas.


 Dica:** Sempre que possível, escolha algoritmos com **menor complexidade** para lidar com grandes volumes de dados.
