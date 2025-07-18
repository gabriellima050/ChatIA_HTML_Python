from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from datetime import datetime

app = Flask(__name__)

# Configuração da API Groq
GROQ_API_URL = "INSIRA SUA CHAVE GROQ"
GROQ_API_KEY = "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"  # Substitua pela sua chave

# Função para consultar a API Groq
def consultar_groq(mensagem, historico=[]):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Monta o histórico da conversa
    messages = historico + [{"role": "user", "content": mensagem}]
    
    payload = {
        "messages": messages,
        "model": "llama3-8b-8192",
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            resposta = response.json()['choices'][0]['message']['content']
            return resposta
        else:
            return f"Erro na API: {response.status_code}"
    except Exception as e:
        return f"Erro de conexão: {str(e)}"

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar mensagens
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensagem = data.get('mensagem', '')
    historico = data.get('historico', [])
    
    if not mensagem.strip():
        return jsonify({'erro': 'Mensagem vazia'}), 400
    
    resposta = consultar_groq(mensagem, historico)
    
    return jsonify({
        'resposta': resposta,
        'timestamp': datetime.now().strftime('%H:%M')
    })

# Rota para limpar o chat
@app.route('/clear', methods=['POST'])
def clear_chat():
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)