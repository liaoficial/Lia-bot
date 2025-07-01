from flask import Flask, request

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").strip().lower()
    response = ""

    if "agendar" in incoming_msg:
        response = "Claro! Para qual dia e horário você gostaria de agendar?"
    elif "confirmar" in incoming_msg:
        response = "Seu agendamento foi confirmado com sucesso!"
    elif "cancelar" in incoming_msg:
        response = "O agendamento foi cancelado. Se precisar remarcar, estou aqui!"
    else:
        response = "Olá! Sou a Lia, sua assistente virtual. Você pode digitar: agendar, confirmar ou cancelar."

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
