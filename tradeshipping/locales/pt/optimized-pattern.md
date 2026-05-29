> **Machine translation (pt).** English source: [optimized-pattern.md](../../optimized-pattern.md). Report fixes in guild chat or a GitHub issue.

# Padrão comercial otimizado

Padrão da guilda para remessa comercial **Opportunity** e **Demerzal (Dem)**.

---

## Regras básicas

### Oportunidade — Somente Moeda Galáctica

**A oportunidade só deve rodar Galactic Coin (GC).**

- Não atribua pedidos especiais ao Opportunity
- As execuções do GC são longas (cerca de 8 horas) — definidas e coletadas em um cronograma fixo
- A tarefa do Opportunity é **tempo máximo de atividade do GC**, não produção de pedido especial

### Demerzal – Pedidos especiais, depois Moeda Galáctica

**Dem executa pedidos especiais durante sua janela ativa e depois Galactic Coin.**

Dois modos válidos:

| Modo | Quando | Padrão |
|------|------|---------|
| **Dia ativo** | Você está fazendo check-in regularmente | 4× pedidos especiais → execução do GC |
| **Suspensão / off-line** | Pernoite ou fora | Somente moeda galáctica (igual à oportunidade ociosa) |

Dem é o **navio de pedido especial**. A oportunidade é o **navio GC**. Não troque de papéis.

---

## Prazo — pedidos especiais (Dem)

Dem tem **4 vagas para pedidos especiais** por ciclo.

| Métrica | Valor |
|--------|--------|
| Encomendas especiais por ciclo | **4** |
| Tempo por pedido especial | **2h30m – 4h** (varia conforme pedido) |
| Todos os 4 em uma janela | **~12–16 horas** total |
| Corrida de Moeda Galáctica | **~8 horas** |

**O dia otimizado:** coloque todos os quatro pedidos especiais dentro de uma janela ativa de 12 a 16 horas e, em seguida, inicie uma **execução de GC de 8 horas** antes de dormir ou antes do próximo check-in.```
Active window (12–16 hrs)
├── Special order 1   (~2.5–4 hrs)
├── Special order 2   (~2.5–4 hrs)
├── Special order 3   (~2.5–4 hrs)
└── Special order 4   (~2.5–4 hrs)
        ↓
Galactic Coin run     (~8 hrs)  ← Dem sleeping / offline, or Opportunity parallel
```---

## Exemplos de cronogramas

Ajuste os horários de início ao seu fuso horário e hábitos de check-in.

### Dem — jogador ativo (check-in ~3× dia)

| Tempo | Dem |
|------|-----|
| Manhã | Iniciar pedido especial 1 |
| Meio-dia | Coletar → pedido especial 2 (ou 2 + 3 se for curto) |
| Noite | Coletar → pedidos especiais 3 + 4 |
| Antes de dormir | Iniciar **Moeda Galáctica** (~8 horas durante a noite) |

Acorde com o GC concluído; inicie o ciclo de pedido especial novamente ou execute o GC no Opportunity.

### Dem — apenas modo de suspensão

Se você não tocar no jogo por mais de 8 horas:

- **Pular pedidos especiais** — inicie **Galactic Coin** no Dem antes de ficar offline
- Retomar o ciclo de pedidos especiais quando voltar para um período de 12 a 16 horas

### Oportunidade — sempre

| Janela | Oportunidade |
|--------|------------|
| Sempre que o slot GC estiver gratuito | **Moeda Galáctica** |
| Nunca | Encomendas especiais |

Se Dem estiver executando o GC durante a noite, o Opportunity **já deverá estar no GC** ou iniciar o próximo GC assim que o anterior for concluído - sem tempo ocioso no Opportunity.

---

## Meta de 24 horas (ambos os navios)

Taxa de transferência ideal da guilda:```
Opportunity:  [======== GC 8h ========][======== GC 8h ========](2× GC/day if collected on time)
Dem (active): [SO1][SO2][SO3][SO4][==== GC 8h ====]
Dem (sleep):  [============ GC 8h ============]
```**Pedidos especiais (SO)** = Somente Dem, durante o horário ativo.  
**Moeda Galáctica (GC)** = Oportunidade sempre; Dem preenche lacunas da noite para o dia.

---

## Lista de verificação

### Oportunidade
- [] Apenas Moeda Galáctica atribuída - verifique antes de cada despedida
- [] Nenhum pedido especial neste navio, nunca
- [] Coleta GC no cronômetro; reinicie imediatamente

### Demerzal
- [] 4 pedidos especiais na fila durante a janela ativa de 12 a 16 horas, quando possível
- [] Após a conclusão do 4º pedido especial → iniciar **8 horas de GC** antes de ficar off-line
- [ ] Se dormir mais de 8 horas sem check-ins → **Somente GC**, ignore pedidos especiais
- [] Nunca deixe Dem ocioso entre as execuções se um slot estiver disponível

---

## Erros comuns

| Erro | Correção |
|--------|-----|
| Pedidos especiais no Opportunity | Mova todos os SO para Dem; Opp = somente GC |
| Dem ocioso durante a noite sem GC | Iniciar GC 8 horas antes de dormir |
| Apenas 2–3 pedidos especiais por dia no Dem | Planeje uma janela de 12 a 16 horas para todos os 4 |
| GC on Dem enquanto você está ativo e slots SO abertos | Execute o SO primeiro, o GC por último na janela |
| Ambos os navios sob encomenda especial | Opp nunca administra SO – Dem é o dono deles |

---

## Resumo

| Navio | Função | Padrão |
|------|------|---------|
| **Oportunidade** | Especialista em GC | Moeda Galáctica **apenas** |
| **Demerzal** | SO + GC flexível | 4× pedidos especiais (12–16 horas) → 8 horas GC; ou GC enquanto dorme |

---

*Os tempos são aproximados – confirme a duração do jogo para o seu servidor e atualize este documento se os patches mudarem a duração da execução.*