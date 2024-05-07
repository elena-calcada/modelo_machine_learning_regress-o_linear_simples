from pydantic import BaseModel # Valida os dados de entrada
from fastapi import FastAPI # Faz exposição de API's
import uvicorn # Ativa o servidor interno
import joblib # Lê o arquivo pkl

# 1 - Criar uma instância do FastAPI
app = FastAPI()

# 2 - Criar a classe que terá os dados do request body para a API
class request_body(BaseModel):
  horas_estudo: float

# 3 - Carregar o modelo para realizar a predição
modelo_pontuação = joblib.load('./modelo_regressao.pkl')

# 4 - Função para receber os dados
@app.post('/predict')
def predict(data: request_body):
  # Preparar dados para a predição
  input_feature = [[data.horas_estudo]]

  # Realizar a predição
  y_pred = modelo_pontuação.predict(input_feature)[0].astype(int)

  # Retornar a pontuação predita
  return {'pontuacao_teste': y_pred.tolist()}