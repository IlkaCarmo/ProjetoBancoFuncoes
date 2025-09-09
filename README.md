# ProjetoBancoFuncoes

Sistema bancário simples em Python, desenvolvido como desafio do Curso Santander. Permite cadastro de usuários, criação de contas, depósitos, saques, extrato, e listagem de clientes e contas.

## Funcionalidades
- Cadastro de novo usuário
- Cadastro de nova conta (vinculada ao CPF do usuário)
- Depósito em conta
- Saque com limite diário e por operação
- Visualização de extrato
- Listagem de usuários
- Listagem de contas

## Como usar
1. Certifique-se de ter Python 3 instalado.
2. Execute o script:
   ```bash
   python DesafioComFuncoesBanco.py
   ```
3. Siga o menu interativo para realizar operações bancárias.

## Estrutura do Projeto
- `DesafioComFuncoesBanco.py`: Script principal com toda a lógica do sistema.

## Fluxo Principal
- O sistema utiliza listas para armazenar usuários e contas.
- Cada operação é realizada por funções específicas, seguindo boas práticas de modularização.
- O menu principal orienta o usuário pelas opções disponíveis.

## Convenções
- Todas as mensagens e variáveis estão em português.
- O código segue padrão procedural, com funções para cada operação.
- Não há dependências externas além da biblioteca padrão do Python.

## Exemplo de Uso
Ao iniciar o sistema, o usuário verá o menu:
```
=============== MENU ===============
[1] Novo usuário
[2] Nova conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar usuários
[7] Listar contas
[8] Sair
```

## Autor
Desenvolvido por Ilka Carmo para o Curso Santander.
