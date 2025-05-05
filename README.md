# Case: Grupo Boticário (Cientista de Dados)

Este projeto tem como objetivo realizar a análise do comportamento dos produtos similares quando o produto principal entra em ruptura. Além disso realizar a estimativa de venda caso aquele produto não tivesse tido ruptura.
---

## Estrutura do Projeto

```
.
├── data/                  # Bases utilizadas no case (raw e processadas)
├── notebooks/             # Notebooks com exploração, modelagem e análises
├───── 02_Estimativa_Venda # Notebooks estudo estimativa de vendas
├── imgs/                  # Gráficos gerados para o relatório Analise
├── README.md              # Este arquivo
└── requirements.txt       # Dependências do projeto
```

---

## 📊 Etapas do Projeto

### 1. Análise Compartamento Similares Ruptura
- Criação Flag Ruptura
- Ranking das Lojas por quantidade de Venda
- Analise das lojas com mais venda (8 e 5) e lojas com menos vendas (1 e 7)

### 2. Estimativa de venda
- Classificação de Tipo de Demanda
- Calcular a mediana da quantidade de vendas por combinação loja + produto quando não houve ruptura
- Prever para quando houve ruptura
