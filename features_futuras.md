# 📌 Features Futuras

Lista de funcionalidades planejadas para serem implementadas no projeto. Use as caixinhas para acompanhar o progresso de cada item.

---

## 🛠️ Funcionalidades Planejadas

### 🔑 Sistema de Chaves

- [ ] Criar sistema de chaves únicas para cada conta.
- [ ] Permitir transmissões financeiras utilizando as chaves.

### 🗄️ Banco de Dados Local

- [ ] Criar um banco de dados local para armazenar contas para testes.
- [ ] Implementar funcionalidade para buscar dados do banco local.
- [ ] Implementar funcionalidade para atualizar dados no banco local.

### 📋 Menus Interativos

- [ ] Criar menus interativos no terminal para facilitar a navegação.
- [ ] Adicionar opções como "Sacar", "Depositar", "Transferir" e "Consultar Saldo".
- [ ] Implementar validação de entrada para evitar erros do usuário.

### 🔒 Segurança

- [x] Implementar validação de senha para operações sensíveis usando decorators.
- [ ] Adicionar autenticação de dois fatores (2FA) para operações sensíveis.
- [ ] Melhorar o sistema de validação de senha com criptografia.

### 📊 Relatórios e Estatísticas

- [ ] Gerar relatórios de movimentações financeiras.
- [ ] Criar gráficos para análise de saldo e transações.

### 💳 Operações Bancárias

- [x] Implementar funcionalidade de depósito.
- [x] Implementar funcionalidade de saque.
- [x] Implementar funcionalidade de transferência entre contas.

---

## 🏁 Status das Features

- **[ ]**: Não iniciada  
- **[~]**: Em andamento  
- **[x]**: Concluída  

---

## 📝 Notas

- As funcionalidades de **depósito**, **saque** e **transferência** já foram implementadas na classe `ContaBancaria`.
- A validação de senha foi implementada usando o decorator `@validar_senha`.
- Priorizar a criação de menus interativos para facilitar a interação do usuário.
- Avaliar a integração com um banco de dados local para persistência de dados.
