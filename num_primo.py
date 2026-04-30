def is_prime(n: int) -> bool:
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
    if not isinstance(n, int):
        raise TypeError("O argumento deve ser um inteiro.")
    if n < 0:
        raise ValueError("O número deve ser não negativo.")

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    candidate_divisor = 5
    STEP = 6  # Incremento para pular múltiplos de 2 e 3
    while candidate_divisor * candidate_divisor <= n:
        if n % candidate_divisor == 0 or n % (candidate_divisor + 2) == 0:
            return False
        candidate_divisor += STEP
    return True


def run_tests():
    """Executa testes unitários para a função is_prime."""
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

    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    try:
        num = int(input("Digite um número inteiro não negativo: "))
        if is_prime(num):
            print(f"{num} é primo.")
        else:
            print(f"{num} não é primo.")
    except ValueError:
        print("Erro: Você deve digitar um número inteiro válido.")
