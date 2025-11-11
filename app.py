from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)
MODEL_NAME = "llama3.2:1b" # First model endpoint for testing
MODEL_NAME_2 = "gemma3:1b" # Second model endpoint for inference

@app.post("/inference")
def inference():
    data= request.get_json(silent=True) or {}
    prompt= data.get("prompt", "")
    if not isinstance(prompt, str) or not prompt.strip():
        return jsonify({"error": "Invalid input"}), 400
    try:
        response = ollama.chat(
            model=MODEL_NAME_2,
            messages=[{"role": "user", "content": prompt}],
            stream=False,
            options={
                "num_predict":256,
                "temperature":0.2
            })
        
        text= response["message"]["content"]
    except Exception as e:
        return jsonify({"error": "Inference failed", "details": str(e)}), 500
    return jsonify({
        "model": MODEL_NAME_2,
        "prompt": prompt,
        "response": text
    }), 200

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)