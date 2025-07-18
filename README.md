
# 🤖 Chat IA com Flask + Groq

Este é um projeto simples e funcional de **chat com inteligência artificial** utilizando:

- 🧠 API da Groq (modelo LLaMA3)
- 🐍 Flask (backend em Python)
- 💬 HTML, CSS e JavaScript puro (frontend moderno e responsivo)

> ✅ Ideal para quem quer aprender como integrar IA com interfaces web de forma simples, sem depender de frameworks pesados.

---

## 🚀 Funcionalidades

- Interface de chat moderna com animações e responsividade
- Envio e recebimento de mensagens em tempo real
- Conexão com o modelo **LLaMA3 da Groq**
- Exportação do histórico do chat em `.txt`
- Botão para limpar a conversa
- Indicador de "IA está digitando..."

---

## 🧰 Tecnologias usadas

- Python 3.10+
- Flask
- HTML + CSS moderno (com animações e responsividade)
- JavaScript (vanilla)
- API da Groq (https://console.groq.com/)

---

## 🛠 Como rodar localmente

### 1. Clone o repositório


### 2. Crie um ambiente virtual e instale as dependências

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

> ⚠️ Certifique-se de ter o Flask instalado (`pip install flask`)

### 3. Configure sua chave da Groq

Abra o arquivo `app.py` e substitua:
```python
GROQ_API_KEY = "sua_chave_groq_aqui"
```

Você pode obter sua chave em: [https://console.groq.com/](https://console.groq.com/)

### 4. Rode o servidor Flask

```bash
python app.py
```

O app estará disponível em: `http://localhost:5000`

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).  
Fique à vontade para usar, estudar e adaptar!

---

## 🙋‍♂️ Autor

Gabriel Silva  
[LinkedIn](https://br.linkedin.com › gabriel-lima-procópio-2b2261b0) 

---

## ⭐ Quer contribuir?

- Deixe uma ⭐ no repositório
- Compartilhe com quem está aprendendo Python ou Flask

