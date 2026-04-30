### Explicação Técnica e Didática do Código em num_primo.py (Versão Otimizada com Clean Code)

O código implementa uma função em Python chamada `is_prime` que verifica se um número inteiro é primo, aplicando princípios de clean code como nomes descritivos, docstrings detalhadas, constantes para valores mágicos, tratamento de erros e separação de responsabilidades. O algoritmo permanece otimizado (O(√n)), mas agora inclui validações robustas e uma função dedicada para testes. O código é dividido em três partes principais: a função `is_prime`, a função `run_tests` e o bloco de execução condicional.

#### 1. Definição da Função `is_prime`
```python
def is_prime(n: int) -> bool:
```
- **Linha 1**: Define a função `is_prime` com anotações de tipo para clareza. Recebe `n` (int) e retorna bool.

```python
    """
    Verifica se um número inteiro é primo.

    Um número primo é maior que 1 e não tem divisores positivos além de 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado. Deve ser um inteiro não negativo.

    Returns:
        bool: True se n for primo, False caso contrário.

    Raises:
        TypeError: Se n não for um inteiro.
        ValueError: Se n for negativo.
    """
```
- **Linhas 2-15**: Docstring detalhada seguindo o padrão Google/NumPy, explicando propósito, argumentos, retorno e exceções. Promove legibilidade e manutenção.

```python
    if not isinstance(n, int):
        raise TypeError("O argumento deve ser um inteiro.")
    if n < 0:
        raise ValueError("O número deve ser não negativo.")
```
- **Linhas 16-19**: Validações de entrada para robustez. Verifica tipo e valor, lançando exceções claras. Evita comportamentos inesperados e segue clean code (fail fast).

```python
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
```
- **Linhas 20-25**: Lógica inicial idêntica à versão anterior, tratando casos triviais e eliminando múltiplos de 2/3.

```python
    candidate_divisor = 5
    STEP = 6  # Incremento para pular múltiplos de 2 e 3
```
- **Linhas 26-27**: Inicializa `candidate_divisor` com nome descritivo (clean code: nomes expressivos). Define `STEP` como constante para evitar "números mágicos".

```python
    while candidate_divisor * candidate_divisor <= n:
        if n % candidate_divisor == 0 or n % (candidate_divisor + 2) == 0:
            return False
        candidate_divisor += STEP
    return True
```
- **Linhas 28-32**: Loop otimizado, usando a constante `STEP`. Retorna `True` se nenhum divisor for encontrado.

#### 2. Definição da Função `run_tests`
```python
def run_tests():
    """Executa testes unitários para a função is_prime."""
```
- **Linhas 35-36**: Função separada para testes, seguindo clean code (separação de responsabilidades). Docstring simples.

```python
    test_cases = [
        (-5, False),  # Negativo
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (19, True),
        (25, False),
        (97, True),
    ]
```
- **Linhas 37-48**: Lista renomeada para `test_cases` com comentários. Inclui casos edge e válidos.

```python
    for value, expected in test_cases:
        try:
            result = is_prime(value)
            print(f"n={value}: esperado={expected}, obtido={result}")
            assert result == expected, f"Falha no teste para {value}"
        except (TypeError, ValueError) as e:
            print(f"n={value}: Erro esperado - {e}")
            if expected is False:  # Para casos inválidos, esperamos False ou erro
                continue
            else:
                raise
```
- **Linhas 50-59**: Loop com tratamento de exceções. Testa entradas válidas e inválidas, imprimindo resultados. Usa `try-except` para capturar erros esperados.

```python
    print("Todos os testes passaram com sucesso!")
```
- **Linha 60**: Mensagem de sucesso se todos passarem.

#### 3. Bloco de Execução Condicional
```python
if __name__ == "__main__":
    try:
        num = int(input("Digite um número inteiro não negativo: "))
        if is_prime(num):
            print(f"{num} é primo.")
        else:
            print(f"{num} não é primo.")
    except ValueError:
        print("Erro: Você deve digitar um número inteiro válido.")
```
- **Linhas 63-70**: Solicita ao usuário um número inteiro não negativo via input, verifica se é primo usando a função `is_prime` e imprime o resultado. Inclui tratamento de erro para entradas inválidas, mantendo modularidade e robustez.

#### Considerações Técnicas Gerais
- **Clean Code Aplicado**: Nomes descritivos (`candidate_divisor` vs `i`), constantes (`STEP`), docstrings completas, validações de entrada, separação de funções e tratamento de erros.
- **Eficiência**: Mantém O(√n), com otimizações para múltiplos de 2/3.
- **Robustez**: Agora trata tipos incorretos e valores negativos, lançando exceções informativas.
- **Testes**: Melhorados com tratamento de erros, simulando testes unitários reais.
- **Melhorias Futuras**: Integrar com `unittest` ou `pytest` para testes mais avançados, ou usar `math.isqrt` para precisão.

Se precisar de mais ajustes, é só pedir!