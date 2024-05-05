<h1>DIOBanco v1--> v2 --> v3</h1>

# 🎯 Objetivo Geral:
Este foi um desafio proposto no bootcamp Python AI Back-end developer no qual é preciso desenvolver as funções básicas de um banco:

# 💰 Depósito
- O valor deve ser positivo

# 💸 Saque
- O limite de cada saque é de R$ 500,00
- Só podem ser feitos 3 saques por dia
- O valor do saque deve ser maior que R$ 0,00 e menor que o saldo

# 🧾 Extrato
- Deve-se mostrar ao usuário todas as movimentações feitas por ele e ao final exibir o saldo
- Na versão 2, a função extrato deve receber os argumentos apenas por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

<h2>DIOBanco v2</h2>
# ✅ Novas funções
duas novas funções: criar usuário e criar conta corrente.

# 🧍‍♂️ Criar usuário (cliente)
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

# 💲 Criar conta corrente
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

<h2>DIOBanco v3</h2>

Implementação de classes e estruturação do programa no paradigma OOP