import math
import mlflow
import xgboost
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# Função que trata os argumentos da linha de comando
def parse_args():
    # Criação do parser de argumentos com uma breve descrição do que o programa faz
    parser = argparse.ArgumentParser(description='House Prices ML')
    
    # Adiciona o argumento para a taxa de aprendizado (learning rate)
    parser.add_argument(
        '--learning-rate',  # Nome do argumento
        type=float,         # Tipo do argumento (número decimal)
        default=0.3,        # Valor padrão caso o usuário não forneça esse argumento
        help=               # Descrição do que o argumento representa
        "taxa de aprendizado para atualizar o tamanho de cada passa do boosting"
    )
    
    # Adiciona o argumento para a profundidade máxima das árvores
    parser.add_argument('--max-depth',  # Nome do argumento
                        type=int,       # Tipo do argumento (número inteiro)
                        default=6,      # Valor padrão
                        help='profundidade maxima das arvores')  # Descrição do que o argumento faz
    
    # Retorna os argumentos analisados
    return parser.parse_args()


# Carrega o conjunto de dados de um arquivo CSV e prepara os dados para o modelo
df = pd.read_csv('data/processed/casas.csv')  # Lê o arquivo CSV com os dados
X = df.drop('preco', axis=1)  # Variáveis independentes (todas as colunas exceto 'preco')
y = df['preco'].copy()  # Variável dependente (preço das casas)

# Divisão dos dados em treino e teste, com 30% dos dados para teste
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,  # 30% para teste
                                                    random_state=42)  # Semente para reprodutibilidade

# Criação dos datasets DMatrix para o XGBoost (formato otimizado para o modelo)
dtrain = xgboost.DMatrix(X_train, label=y_train)  # Dados de treino
dtest = xgboost.DMatrix(X_test, label=y_test)  # Dados de teste


# Função principal que executa o treinamento do modelo e loga os resultados
def main():
    # Chama a função para obter os argumentos passados via linha de comando
    args = parse_args()
    
    # Parâmetros do modelo XGBoost que serão passados durante o treinamento
    xgb_params = {
        'learning_rate': args.learning_rate,  # Taxa de aprendizado passada como argumento
        'max_depth': args.max_depth,  # Profundidade máxima das árvores passada como argumento
        'seed': 42  # Semente para garantir reprodutibilidade dos resultados
    }

    # Configuração do MLflow para rastrear experimentos
    mlflow.set_tracking_uri('http://127.0.0.1:5000')  # Define a URL do servidor MLflow
    mlflow.set_experiment('house-prices-script')  # Define o nome do experimento no MLflow
    
    # Inicia o experimento com o MLflow
    with mlflow.start_run():
        # Ativa o log automático do modelo XGBoost
        mlflow.xgboost.autolog()
        
        # Treinamento do modelo XGBoost
        xgb = xgboost.train(xgb_params, dtrain, evals=[(dtrain, 'train')])
        
        # Realiza as previsões no conjunto de teste
        xgb_predicted = xgb.predict(dtest)
        
        # Calcula a métrica de erro quadrático médio (MSE)
        mse = mean_squared_error(y_test, xgb_predicted)
        
        # Calcula a raiz do erro quadrático médio (RMSE)
        rmse = math.sqrt(mse)
        
        # Calcula o coeficiente de determinação R²
        r2 = r2_score(y_test, xgb_predicted)
        
        # Registra as métricas no MLflow
        mlflow.log_metric('mse', mse)  # MSE
        mlflow.log_metric('rmse', rmse)  # RMSE
        mlflow.log_metric('r2', r2)  # R²


# Verifica se o script está sendo executado diretamente e chama a função principal
if __name__ == '__main__':
    main()