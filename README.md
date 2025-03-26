# Entrega Contínua para Machine Learning: Predição dos Preços de Imóveis

Este projeto acadêmico demonstra a implementação da técnica de **Entrega Contínua (Continuous Delivery - CD)** para **Machine Learning**, utilizando a ferramenta **MLflow** para automação e monitoramento do ciclo de vida do modelo. O objetivo do modelo é prever os preços de imóveis com base em várias características, utilizando **Regressão Linear**.

### Descrição do Projeto

O projeto envolve a construção de um modelo de regressão linear para prever os preços de casas com base em um conjunto de dados. A implementação inclui o uso de **MLflow** para automação do ciclo de vida do modelo, desde o treinamento até a avaliação e o monitoramento das métricas. Além disso, foi configurada uma abordagem de entrega contínua para atualizar e melhorar o modelo ao longo do tempo.

### Objetivo

- **Prever os preços de imóveis** com base em características como tamanho, localização, número de quartos, entre outras.
- Implementar um fluxo de trabalho de **entrega contínua (CD)** para garantir que o modelo seja constantemente monitorado, treinado e atualizado.
- Utilizar o **MLflow** para gerenciar experimentos de machine learning e monitorar as métricas de desempenho do modelo.

### Tecnologias Utilizadas

- **MLflow**: Para monitoramento e automação do ciclo de vida do modelo.
- **XGBoost**: Algoritmo de aprendizado de máquina utilizado para treinamento do modelo.
- **Regressão Linear**: Modelo para previsão de preços de imóveis.
- **Pandas**: Para manipulação de dados.
- **Scikit-learn**: Para pré-processamento e avaliação do modelo.
- **Click**: Para criação de comandos de linha de comando.
- **Logging**: Para rastrear o processo de execução do código.
- **dotenv**: Para carregar variáveis de ambiente a partir de um arquivo `.env`.