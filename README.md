# Segundo desafio - Criar um Sistema bancário em python

Este é um sistema bancário simples implementado em Python que permite realizar operações como cadastro de usuários, criação de contas correntes, depósitos, saques e exibição de extratos. O sistema foi projetado para ser modular, com funções específicas para cada operação.

### Funcionalidades
1. **Cadastrar Usuário**

* Função: criar_usuario(nome, data_nascimento, cpf, endereco).
* Descrição: Registra um novo usuário no sistema, armazenando as informações em uma lista de usuários.
* Argumentos:
    * nome (str): Nome do usuário.
    * data_nascimento (str): Data de nascimento do usuário no formato dd/mm/aaaa.
    * cpf (str): CPF do usuário (somente números).
endereco (str): Endereço do usuário no formato logradouro, nro - bairro - cidade/sigla estado.
    * Regra: O CPF deve ser único; o sistema não permite cadastrar dois usuários com o mesmo CPF.
2. **Criar Conta Corrente**

* Função: criar_conta_corrente(cpf_usuario).
* Descrição: Cria uma nova conta corrente para um usuário existente no sistema, vinculando a conta ao usuário através do CPF.
* Argumentos:
    * cpf_usuario (str): CPF do usuário para o qual a conta será criada.
* Regra: Um usuário pode ter mais de uma conta corrente, mas uma conta pertence a apenas um usuário.
3. **Depositar**

* Função: depositar(saldo, valor, extrato, /).
* Descrição: Realiza um depósito em uma conta corrente.
* Argumentos:
    * saldo (float): Saldo atual da conta.
    * valor (float): Valor do depósito.
    * extrato (str): Histórico de transações da conta.
* Retorno: Retorna o novo saldo e o extrato atualizado.
* Regra: Esta função recebe argumentos apenas por posição.
4. **Sacar**

* Função: sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques).
* Descrição: Realiza um saque da conta corrente.
* Argumentos:
    * saldo (float): Saldo atual da conta.
    * valor (float): Valor do saque.
    * extrato (str): Histórico de transações da conta.
    * limite (float): Limite máximo permitido para o saque.
    * numero_saques (int): Número de saques realizados até o momento.
    * limite_saques (int): Limite máximo de saques permitidos por dia.
* Retorno: Retorna o novo saldo, extrato atualizado, e o número de saques incrementado.
* Regra: Esta função recebe argumentos apenas por nome (keyword only).
5. **Exibir Extrato**

* Função: exibir_extrato(saldo, /, *, extrato).
* Descrição: Exibe o extrato bancário da conta corrente, mostrando o histórico de transações e o saldo atual.
* Argumentos:
    * saldo (float): Saldo atual da conta.
    * extrato (str): Histórico de transações da conta.
* Regra: Esta função recebe saldo por posição e extrato por nome.

**Observações**

O sistema foi desenvolvido com foco em modularidade e boas práticas de programação, utilizando argumentos por posição e nome conforme necessário.
O CPF é usado como identificador único para os usuários e deve conter apenas números. Neste caso em específico não foi criado nenhum tipo de validador de CPF, pois não é o objetivo do estudo.