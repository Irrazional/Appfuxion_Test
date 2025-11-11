> Appfuxion Take Home Test\ Michael Joshua Kusnadi

# LLM Inference with Flask API

Requirements:

- Python (ver. 3.8+)
- Ollama local installation
- Model pulled from Ollama ('gemma3:1b' and 'llama3.2:1b' used in this program)

# Ollama Installation

Download and Install Ollama through their official website:
[Link](https://ollama.com/download)

Ensure that Ollama is running by running this code in bash:

```bash
ollama list
```

# Pull Models from Ollama

## llama3.2:1b installation (for testing)

```bash
ollama pull llama3.2:1b
```

## gemma3:1b installation (for inference)

```bash
ollama pull gemma3:1b
```

# Set Up Python Environment (venv)

Create and activate Python's virtual environment or venv:

```bash
python -m venv .venv
```

Afterwards, activate it in bash using:

```bash
source ollama-flask-api\.venv\Scripts\activate
```

# Install Dependencies in Virtual Environment

Install Flask's and Ollama's libraries:

```bash
pip install flask ollama
```

---

# Running the Flask Python Program

With the virtual environment active, run the program in bash:

```bash
python app.py
```

The program runs at 127.0.0.1:5000

# Test the API

To test the API, send a POST request to '/inference' of the program containing the prompt. The format of the structure is as such:

## With curl:

```bash
curl -X POST http:127.0.0.1:5000/inference
-H "Content-Type: application/json"
-d '{"prompt":"Example Prompt Text that will be sent to the LLM"}'
```

## Response output (in JSON format):

```json
{
  "model": "MODEL_NAME",
  "prompt": "Example Prompt Text that will be sent to the LLM",
  "response": "Example Prompt Answer based on Prompt"
}
```

## Closing Notes

To test out other models, please browse on Ollama's website for available models, pull it, and include it in the program as done already.
