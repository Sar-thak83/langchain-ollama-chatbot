# Chatbot Application

A simple chatbot built with Langchain, Ollama, and Streamlit.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create `.env` file:

```
LANGCHAIN_API_KEY=your_api_key_here
LANGCHAIN_PROJECT=your_project_name
```

3. Install Ollama and pull llama2 model:

```bash
ollama pull llama2
```

## Run

```bash
streamlit run app.py
```

## Usage

Enter your question in the text input and get AI-powered responses using the Llama2 model.
