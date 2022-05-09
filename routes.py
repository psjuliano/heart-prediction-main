# Importação de bibliotecas
import pandas as pd
from flask import Blueprint, request
import numpy as np
from joblib import load
import json

# Carregamento do modelo extraido depois do treinamento.
model = load('models/heart_disease.joblib')

# Declaração de rota do backend com prefixo /main, ou seja, para chamar http://127.0.0:5000/main/api/run_model (localmente).
bp1 = Blueprint('main', __name__, url_prefix='/main')

# Rota do backend responsável por coletar as informações enviadas pelo frontend.
@bp1.route('/api/run_model', methods=['POST'])
def run_model():
    # Coleta dos valores da request e criação de DataFrame
    form_hd_df = pd.DataFrame(request.form, index=[0])
    # Extração de apenas os valores da tabela, sem seus indices
    records_hd = form_hd_df.to_records(index=False)
    results_hd = list(records_hd[0])
    # Conversão necessaria para ser feita o "predict"
    results_hd_as_numpy_array= np.asarray(results_hd)
    results_hd_reshaped = results_hd_as_numpy_array.reshape(1,-1)
    predicted = model.predict(results_hd_reshaped)

    # Retorno da função convertendo para String
    return { 
        'pred': json.dumps(int(predicted[0]))
    }
