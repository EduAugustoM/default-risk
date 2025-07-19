# 📊 Projeto: **Análise de Risco de Inadimplência (Default Risk)**

Este projeto propõe o desenvolvimento de um modelo de _Machine Learning_ voltado para a previsão da probabilidade de inadimplência de clientes. Seu principal objetivo é oferecer suporte à tomada de decisões proativas na gestão de cobranças, permitindo à empresa direcionar seus esforços para clientes com maior risco.

Utilizando técnicas de _Machine Learning_ aliadas à _Análise Exploratória de Dados (EDA)_, o modelo foi treinado para classificar clientes de acordo com o seu potencial de inadimplência. A partir disso, são gerados insights estratégicos que fortalecem o processo de concessão de crédito e otimizam a gestão de risco financeiro.

## ☕**Metodologia**

O projeto foi estruturado em um pipeline claro, seguindo as melhores práticas de ETL (Extract, Transform, Load) e modelagem.

1.  **Extração e Preparação dos Dados:**

    - Os dados foram carregados a partir de quatro arquivos CSV distintos: histórico de pagamentos, informações mensais, cadastro de clientes e a base de teste a ser prevista[cite: 31, 32].
    - Foi criada a variável alvo **`INADIMPLENTE`** com base na regra de negócio: pagamentos com 5 ou mais dias de atraso foram considerados inadimplentes[cite: 22].
    - As bases foram unificadas utilizando chaves compostas (`ID_CLIENTE`, `SAFRA_REF`) para garantir a consistência temporal das informações[cite: 34].

2.  **Engenharia de Features:**

    - Foram criadas novas variáveis para enriquecer o modelo, como:
      - **`TEMPO_RELACIONAMENTO_DIAS`**: Tempo desde o cadastro do cliente até a data da cobrança.
      - **`PRAZO_PAGAMENTO_DIAS`**: Intervalo entre a emissão do documento e o vencimento.
      - **Flags para dados faltantes**: Colunas binárias (`RENDA_FALTANTE`, `FUNCIONARIOS_FALTANTES`) para que o modelo pudesse aprender com a ausência de informação.

3.  **Modelagem e Validação:**

    - **Estratégia de Validação:** Foi implementada uma **validação temporal**, utilizando os dados da safra mais recente para validação e os meses anteriores para treino. Esta abordagem simula o cenário real de produção e fornece uma estimativa de performance mais robusta e confiável.
    - **Pipeline de Machine Learning:** Foi construído um `Pipeline` no Scikit-learn para encapsular o pré-processamento (`OneHotEncoder` para variáveis categóricas) e o treinamento do modelo, garantindo a aplicação consistente das transformações.
    - **Algoritmo:** O modelo escolhido foi o `RandomForestClassifier`, conhecido por sua robustez e alto desempenho em dados tabulares.

## 📈**Resultados**

O modelo final demonstrou um excelente poder preditivo no conjunto de validação:

- **ROC AUC: 0.93** - Este resultado indica uma altíssima capacidade do modelo de discriminar corretamente entre clientes adimplentes e inadimplentes.

A análise do `classification_report` revelou que, com um ponto de corte de 0.5, o modelo atinge uma **precisão de 80%** para a classe de inadimplentes, mas com um **recall de 34%**. Isso mostra que o modelo é muito confiável quando aponta um cliente como risco, mas que a "régua de decisão" (ponto de corte) deve ser ajustada para um valor menor a fim de capturar uma parcela maior dos inadimplentes, de acordo com a estratégia de negócio.

## 🚀 **Como Executar o Projeto**

1.  Clone este repositório:
    ```bash
    git clone https://github.com/EduAugustoM/default-risk.git
    ```
2.  Crie um ambiente virtual e instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute o notebook Jupyter `eda.ipynb`. O arquivo final `probabilidade_inadimplencia.csv` será gerado ao final.

## 🔧**Ferramentas Utilizadas**

- **Linguagem:** Python 3
- **Bibliotecas Principais:** Pandas, NumPy, Scikit-learn

## 📂 **Estrutura do Projeto**

```
default-risk/
├── data/                   # Bases de dados brutas (CSV)
├── notebooks/              # Jupyter Notebooks com análises
├── outputs/                # Resultados (previsões)
├── src/                    # Códigos-fonte (pré-processamento, utilitários)
│   ├── preprocessing.py    # Funções para extração
│   └── utils.py            # Auxiliares (métricas, transformações)
└── README.md               # Este arquivo
```


## ✨ **Melhorias Futuras**

- Implementar **XGBoost** para comparação de desempenho.
- Desenvolver um dashboard interativo com **Streamlit**.

---

## 📧 **Contato**

**Eduardo:** [LinkedIn](https://www.linkedin.com/in/eduardo-augusto-mendes) | [GitHub](https://github.com/eduaugustom)

_<sup>(Projeto desenvolvido para fins educacionais)</sup>_


> **Nota**: Os dados utilizados são fictícios ou anonimizados para preservar confidencialidade.
