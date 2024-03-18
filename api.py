from flask import Flask, jsonify
import pandas as pd

df = pd.read_csv('C:/Users/Lucas/Documents/projetos/workplace/Projects/complement_files/vendas.csv')

app = Flask(__name__)

@app.route('/api/vendas', methods=['GET'])
def obter_dados_vendas():
    # Converter DataFrame para formato JSON
    json_data = df.to_json(orient='records')
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)

    
