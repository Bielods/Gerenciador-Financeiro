# Gerenciador Financeiro

## Descrição
O projeto consiste no desenvolvimento de um sistema de Controle Financeiro Pessoal, criado para ajudar usuários a organizar suas finanças do dia a dia de forma simples e eficiente. O sistema permite cadastrar receitas e despesas, pagar contas pendentes, consultar o histórico de pagamentos e acompanhar o saldo atual.

## Integrantes e Turma
- Guilherme Arcanjo
- Gabriel
- Isabelle
- Grupo 22
## Explicação Conceitual

### Fila (FIFO)
Uma fila funciona como uma fila de banco: o primeiro a entrar é o primeiro a sair. No nosso projeto, as despesas pendentes ficam na `fila_pendentes`. Quando o usuário cadastra uma despesa, ela entra no final da fila com `.append()`. Quando paga, a mais antiga sai primeiro com `.pop(0)`.

```python
fila_pendentes.append(dict_transacao)  # entra no final
fila_pendentes.pop(0)  # sai pelo início (FIFO)
```

### Pilha (LIFO)
Uma pilha funciona como uma pilha de pratos: o último a entrar é o primeiro a sair. No projeto, os pagamentos realizados ficam na `pilha_pagamentos`. O histórico é exibido do mais recente ao mais antigo com `reversed()`.

```python
pilha_pagamentos.append(transacao)  # empilha no topo
for transacao in reversed(pilha_pagamentos):  # lê do topo para baixo
```

### Dicionário
Cada transação é armazenada como um dicionário Python, agrupando todos os seus atributos em uma única estrutura acessada pelo nome da chave.

```python
dict_transacao = {
    "id": 1,
    "descricao": "Conta de luz",
    "valor": 150.0,
    "tipo": "despesa",
    "categoria": "outros",
    "status": "Pendente"
}
```

### Lista e Tupla
A lista `transacoes` armazena todos os dicionários do sistema e é mutável — itens podem ser adicionados a qualquer momento. As tuplas `TIPOS`, `STATUS` e `CATEGORIAS` armazenam valores fixos que não mudam durante a execução, protegendo o sistema contra alterações acidentais.

```python
transacoes = []  # mutável
CATEGORIAS = ('alimentação', 'transporte', 'saúde', 'educação', 'lazer', 'outros', 'ganhos')  # imutável
```

### Modularização
O projeto foi dividido em 4 arquivos com responsabilidades separadas:
- `dados.py` — variáveis globais
- `utils.py` — funções auxiliares
- `tarefas.py` — regras de negócio
- `main.py` — menu principal

## Como Executar
- Python 3.10 ou superior
- No terminal, dentro da pasta do projeto, execute:
```bash
python main.py
```
- Não são necessárias bibliotecas externas

## Funcionalidades Implementadas
- Cadastrar receitas e despesas
- Listar todas as transações
- Pagar despesa pendente (FIFO)
- Exibir histórico de pagamentos (LIFO)
- Consultar saldo atual
- Validação de valor com try/except

## Dificuldades e Aprendizados
Durante o desenvolvimento do projeto, a maior dificuldade foi entender como as estruturas de dados se conectam na prática. Compreender que a fila e a pilha são listas com regras diferentes de acesso exigiu atenção. A modularização também foi desafiadora no início, pois precisávamos entender como um arquivo importa e usa variáveis de outro. O uso do `reversed()` para exibir o histórico foi um conceito novo que não havia sido visto em aula. No geral, o projeto ajudou a consolidar os conceitos de lista, fila, pilha, dicionário e tupla de forma prática e aplicada ao dia a dia.
