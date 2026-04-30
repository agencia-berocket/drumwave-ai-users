# Planejamento de Coleta e Gestão de Cookies

Este documento descreve a estratégia para coletar, gerenciar e documentar cookies para conformidade legal (LGPD/GDPR) usando o Google Sheets como repositório de inventário e logs.

## 1. Inventário de Cookies (Google Sheets)
A planilha deve ser utilizada como o **Registro de Operações**. Colunas recomendadas:
- **ID/Nome**: Nome técnico do cookie (ex: `_ga`, `_fbp`).
- **Provedor**: Empresa responsável (ex: Próprio, Google, Meta).
- **Finalidade**:
    - **Essenciais**: Necessários para o site funcionar.
    - **Analíticos**: Estatísticas de uso.
    - **Marketing/Publicidade**: Rastreamento para anúncios.
- **Duração**: Prazo de validade (ex: Sessão, 2 anos).
- **Descrição**: O que o cookie faz exatamente.

## 2. Fluxo de Coleta e Consentimento
Para cumprir as obrigações legais, o fluxo técnico deve ser:
1. **Bloqueio Prévio**: Nenhum cookie não essencial deve ser disparado antes do consentimento.
2. **Banner de Cookies**: Interface para o usuário aceitar ou rejeitar categorias.
3. **Persistência**: Armazenar a escolha do usuário localmente.

## 3. Integração com Google Sheets (Logs de Consentimento)
Para auditoria, é possível registrar cada decisão de usuário em uma aba de "Logs" na planilha:
- **Data/Hora**: Timestamp do aceite.
- **ID Anônimo**: Identificador para provar que o consentimento existiu.
- **Categorias**: Quais categorias o usuário autorizou.

## 4. Próximos Passos
- [ ] Criar a estrutura da planilha no Google Sheets.
- [ ] Realizar um scan no site para identificar todos os cookies ativos atualmente.
- [ ] Implementar ou configurar o banner de consentimento no `index.html` e `data-savings.html`.
- [ ] Conectar o banner à planilha via script (opcional, para logs de auditoria).

---
*Documento criado para referência futura em estratégias de conformidade de dados.*
