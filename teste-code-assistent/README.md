# Teste Code Assistant - Projeto Educacional Python

Um projeto educacional focado em conceitos fundamentais de programação Python, incluindo debugging, algoritmos otimizados, testes unitários e refatoração de código seguindo boas práticas e Clean Code.

## 📋 Sobre o Projeto

Este projeto é um conjunto de exemplos práticos que demonstram:
- **Debugging**: Identificação e correção de erros de sintaxe
- **Algoritmos Otimizados**: Implementação eficiente de verificação de números primos
- **Clean Code**: Aplicação de princípios de código limpo e legível
- **Testes Unitários**: Cobertura de testes para validação de funcionalidades
- **Refatoração**: Transformação de código confuso em código profissional e manutenível

## 🗂️ Estrutura do Projeto

```
teste-code-assistent/
├── debug.py                      # Exemplo básico com erro de sintaxe e correção
├── explicação_debug.py           # Explicação detalhada do erro e solução
├── num_primo.py                  # Função otimizada para verificar números primos
├── explicação_num_primo.md       # Documentação técnica da função de primos
├── refatoração.py                # Código refatorado com boas práticas
├── explicação_refatoração.md     # Análise das mudanças de refatoração
└── README.md                     # Este arquivo
```

## 📝 Descrição dos Arquivos

### 1. **debug.py** e **explicação_debug.py**

**Objetivo**: Demonstrar um erro comum e sua correção.

**Conteúdo**: 
- Função simples `calcular_media()` que computa a média aritmética
- Exemplo de erro de sintaxe: falta de parêntese de fechamento
- Comentários inline explicando a lógica

**Conceitos abordados**:
- Estruturas de repetição (loops `for`)
- Funções básicas
- Tratamento de erros de sintaxe
- Comentários e documentação

**Como executar**:
```bash
python debug.py
# Entrada: Digite um número inteiro não negativo
# Saída: A média do aluno é: 8.5
```

### 2. **num_primo.py**

**Objetivo**: Implementar um verificador de números primos com otimização e Clean Code.

**Funcionalidades**:
- Função `is_prime(n)`: Verifica se um número é primo com complexidade O(√n)
- Validações robustas com tratamento de exceções
- Função `run_tests()`: Suite de testes unitários
- Docstring em padrão Google

**Recursos**:
- **Anotações de tipo**: Melhor legibilidade e detecção de erros
- **Tratamento de erros**: Valida entrada (tipo inteiro, não negativo)
- **Algoritmo otimizado**: Pula múltiplos de 2 e 3 automaticamente
- **Testes abrangentes**: Casos edge, valores válidos e inválidos

**Como executar**:
```bash
# Modo interativo
python num_primo.py
# Digite: 17
# Saída: 17 é primo.

# Ou execute os testes
# Descomente run_tests() no bloco __main__
```

**Complexidade**:
- Temporal: O(√n)
- Espacial: O(1)

**Exemplos**:
- `is_prime(2)` → `True`
- `is_prime(97)` → `True`
- `is_prime(100)` → `False`
- `is_prime(-5)` → Lança `ValueError`

### 3. **refatoração.py**

**Objetivo**: Demonstrar transformação de código confuso em código profissional.

**Função**: `calculate_statistics(numbers)`
- Calcula estatísticas sobre uma lista de números
- Retorna: total, média, valor máximo, valor mínimo

**Melhorias aplicadas**:
- ✅ Nomes descritivos (função: `c` → `calculate_statistics`)
- ✅ Variáveis significativas (`t` → `total`, `mx` → `max_value`)
- ✅ Loops idiomáticos (iteração direta em vez de índices)
- ✅ Operadores modernos (`+=` em vez de `t = t + l[i]`)
- ✅ Conformidade com PEP 8
- ✅ Legibilidade e manutenibilidade

**Como executar**:
```bash
python refatoração.py
# Saída:
# Total: 346
# Mean: 34.6
# Maximum: 89
# Minimum: 2
```

### 4. **explicação_num_primo.md**

Documentação técnica completa da função de números primos, incluindo:
- Explicação linha a linha do código
- Justificativa do algoritmo O(√n)
- Detalhes sobre a estratégia de validação
- Documentação da função `run_tests()`

### 5. **explicação_refatoração.md**

Análise detalhada das mudanças de refatoração:
- Comparação antes/depois
- Explicação de cada melhoria
- Aplicação de Clean Code
- Conformidade com PEP 8

## 🎓 Conceitos Ensinados

### Clean Code
- Nomes descritivos para variáveis, funções e constantes
- Separação de responsabilidades
- Documentação clara (docstrings)
- Tratamento adequado de erros

### Python Best Practices
- **PEP 8**: Convenções de estilo
- **Type Hints**: Anotações de tipo
- **Docstrings**: Documentação em padrão Google
- **Exception Handling**: Tratamento de exceções
- **Pythonic Code**: Loops idiomáticos, operadores modernos

### Algoritmos
- Verificação otimizada de números primos (O(√n))
- Cálculo de estatísticas
- Média aritmética

### Testes
- Testes unitários básicos
- Casos edge (valores limítrofes)
- Cobertura de casos válidos e inválidos

## 🚀 Como Usar

1. **Para aprender sobre debugging**:
   ```bash
   python debug.py
   # Leia explicação_debug.py para entender o erro
   ```

2. **Para entender números primos**:
   ```bash
   python num_primo.py
   # Leia explicação_num_primo.md para detalhes técnicos
   ```

3. **Para estudar refatoração**:
   ```bash
   python refatoração.py
   # Leia explicação_refatoração.md para ver as mudanças
   ```

## 📊 Resultados Esperados

### debug.py
```
A média do aluno é: 8.5
```

### num_primo.py (modo teste)
```
n=-5: Erro esperado - O número deve ser não negativo.
n=0: esperado=False, obtido=False
n=1: esperado=False, obtido=False
n=2: esperado=True, obtido=True
...
Todos os testes passaram com sucesso!
```

### refatoração.py
```
Total: 346
Mean: 34.6
Maximum: 89
Minimum: 2
```

## 🔍 Checklist de Aprendizado

- [ ] Entender a estrutura básica de funções Python
- [ ] Identificar e corrigir erros de sintaxe
- [ ] Implementar loops e estruturas de repetição
- [ ] Aplicar algoritmos otimizados
- [ ] Usar anotações de tipo
- [ ] Escrever docstrings efetivas
- [ ] Implementar testes unitários
- [ ] Refatorar código confuso
- [ ] Seguir convenções PEP 8
- [ ] Aplicar princípios de Clean Code

## 🛠️ Ferramentas Utilizadas

- **Python 3.7+**: Linguagem de programação
- **Type Hints**: Anotações de tipo para melhor segurança
- **Docstrings**: Documentação no padrão Google
- **Assertions**: Validação em testes

## 📚 Referências e Leitura Adicional

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Google Style Guide - Python](https://google.github.io/styleguide/pyguide.html)
- [Real Python - Clean Code](https://realpython.com/learning-paths/writing-pythonic-code/)
- [Algoritmos de Verificação de Números Primos](https://en.wikipedia.org/wiki/Prime_number)

## 💡 Dicas de Estudo

1. **Execute cada arquivo** e observe a saída
2. **Leia as explicações** em formato markdown
3. **Modifique o código** para experimentar mudanças
4. **Execute os testes** para validar seu entendimento
5. **Compare o antes/depois** na refatoração

## 📄 Licença

Projeto educacional de código aberto. Sinta-se livre para usar, modificar e compartilhar.

---

**Desenvolvido para fins educacionais**  
*Último atualizado: Abril de 2026*
