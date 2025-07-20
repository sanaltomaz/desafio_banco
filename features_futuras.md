# 📌 Features Futuras

Lista detalhada de funcionalidades planejadas para evolução do sistema bancário.

---

## 🛠️ Funcionalidades Planejadas

### 🔑 Sistema de Chaves e Identificação

- [ ] Gerar chaves únicas para cada conta bancária (UUID ou hash seguro).
- [ ] Permitir transferências utilizando chaves.
- [ ] Implementar validação e expiração de chaves.
- [ ] Auditoria de uso de chaves para rastreabilidade.

### 🗄️ Integração com Banco de Dados SQL

- [ ] Migrar persistência de dados para banco SQL (ex: PostgreSQL, MySQL, SQLite).
  - [ ] Modelagem relacional das entidades (Cliente, Conta, Transação).
    - [ ] Scripts de criação e migração de tabelas.
    - [ ] Configuração de conexão segura (variáveis de ambiente).
- [ ] CRUD completo para contas, clientes e transações.
  - [ ] Buscar, atualizar e remover dados.
- [ ] Indexação e otimização de consultas.
- [ ] Backup e restore do banco de dados.

### 🔒 Segurança

- [x] Validação de senha para operações sensíveis (`@validar_senha`).
- [ ] Autenticação de dois fatores (2FA) para operações sensíveis.
  - [ ] Envio de código via e-mail/SMS.
  - [ ] Validação de token temporário.
- [ ] Criptografia de senhas e dados sensíveis.
  - [ ] Utilizar hash seguro (bcrypt, Argon2).
  - [ ] Criptografar dados críticos no banco.
- [ ] Controle de acesso por perfil (admin, usuário comum).
- [ ] Logs de segurança e tentativas de acesso.

### 📊 Relatórios e Estatísticas

- [ ] Relatórios de movimentações financeiras.
  - [ ] Extrato detalhado por período.
  - [ ] Relatório de transferências e saques.
- [ ] Gráficos para análise de saldo e transações.
  - [ ] Dashboard com gráficos de saldo, entradas e saídas.
  - [ ] Exportação de relatórios em PDF/CSV.
- [ ] Notificações automáticas de movimentações relevantes.

### 💳 Operações Bancárias

- [x] Depósito.
- [x] Saque.
- [x] Transferência entre contas.
- [ ] Agendamento de operações futuras.
- [ ] Estorno de transações.

### 🌐 Integração e APIs

- [ ] API RESTful para operações bancárias.
  - [ ] Endpoints seguros para consulta e movimentação.
  - [ ] Documentação via Swagger/OpenAPI.
- [ ] Webhooks para notificações em tempo real.

### 🖥️ Interface e Experiência do Usuário

- [ ] Interface web responsiva para clientes e administradores.
- [ ] Autenticação e cadastro via frontend.
- [ ] Histórico de login e atividades.
- [ ] Suporte a múltiplos idiomas.

---

## 🏁 Status das Features

- **[ ]**: Não iniciada  
- **[x]**: Concluída  

---

## 📝 Notas

- Prioridade: integração com banco de dados SQL, segurança avançada e API para expansão futura.
- As operações básicas já estão implementadas e testadas.
- O roadmap contempla escalabilidade, segurança e experiência do usuário.
