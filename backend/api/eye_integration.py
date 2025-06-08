import requests
import os
from dotenv import load_dotenv



load_dotenv()

ACCESS_KEY = os.getenv("EYEMOBILE_ACCESS_KEY")
SECRET_KEY = os.getenv("EYEMOBILE_SECRET_KEY")

headers = {
    "X-EYEMOBILE-ACCESS-KEY": ACCESS_KEY,
    "X-EYEMOBILE-SECRET-KEY": SECRET_KEY,
    "Content-Type": "application/json"
}



url = "https://api.eyemobile.com.br/v1/synchronizations/transactions/lock"
response = requests.get(url, headers=headers)

if response.ok:
    data = response.json()
    payload = []

    for item in data.get("data"):
        payload.append({
            response("data"("id")),
            True,
            "Venda registrada com sucesso",
            None
        })
    

    res = requests.post(
        "https://api.eyemobile.com.br/synchronizations/transactions/confirm",
        headers=headers,
        json=payload
    )

    if res.ok:
        print("Sincronização confirmada com sucesso.")
    else:
        print(f"Erro ao confirmar: {res.status_code} - {res.text}")
