import requests
import os
from dotenv import load_dotenv


class eyeapi:


    
    def __init__(self):

        load_dotenv()

        self.ACCESS_KEY = os.getenv("EYEMOBILE_ACCESS_KEY")
        self.SECRET_KEY = os.getenv("EYEMOBILE_SECRET_KEY")

        self.headers = {
            "X-EYEMOBILE-ACCESS-KEY": self.ACCESS_KEY,
            "X-EYEMOBILE-SECRET-KEY": self.SECRET_KEY,
            "Content-Type": "application/json"
        }

        self.response = None
        self.url = ""




    def request(self):

        self.url = "https://api.eyemobile.com.br/v1/synchronizations/transactions/lock"
        self.response = requests.get(self.url, headers=self.headers)

        if self.response.ok:
            data = self.response.json()
            payload = []

            for item in data.get("data"):
                payload.append({
                    item["id"],
                    True,
                    "Venda registrada com sucesso",
                    None
                })
            

            res = requests.post(
                "https://api.eyemobile.com.br/synchronizations/transactions/confirm",
                headers=self.headers,
                json=payload
            )

            if res.ok:
                print("Sincronização confirmada com sucesso.")
            else:
                print(f"Erro ao confirmar: {res.status_code} - {res.text}")

        else:

            print("Falha na importação. Tente novamente.")