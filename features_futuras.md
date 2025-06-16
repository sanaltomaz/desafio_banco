# 📌 Features Futuras

Lista de funcionalidades planejadas e seu progresso no projeto.

---

## 🛠️ Funcionalidades Planejadas

### 🔑 Sistema de Chaves

- [ ] Gerar chaves únicas para cada conta bancária.
- [ ] Permitir transferências utilizando chaves.

### 🗄️ Banco de Dados Local

- [ ] Implementar banco de dados local para persistência das contas.
- [ ] Buscar, atualizar e remover dados do banco local.

### 🔒 Segurança

- [x] Validação de senha para operações sensíveis (`@validar_senha`).
- [ ] Autenticação de dois fatores (2FA) para operações sensíveis.
- [ ] Criptografia de senhas e dados sensíveis.

### 📊 Relatórios e Estatísticas

- [ ] Relatórios de movimentações financeiras.
- [ ] Gráficos para análise de saldo e transações.

### 💳 Operações Bancárias

- [x] Depósito.
- [x] Saque.
- [x] Transferência entre contas.

---

## 🏁 Status das Features

- **[ ]**: Não iniciada  
- **[x]**: Concluída  

---

## 📝 Notas

- **Depósito**, **saque** e **transferência** já implementados na classe `ContaBancaria`.
- Validação de senha disponível via decorator `@validar_senha`.
- Prioridade: integração com banco de dados local e futura implementação de front end para melhor experiência e visibilidade dos dados.
