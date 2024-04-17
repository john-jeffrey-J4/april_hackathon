
import uvicorn
from fastapi import FastAPI
from pywa import WhatsApp
from pywa.types import Message, Button
from fastapi import FastAPI, Body, Path
from pydantic import BaseModel
from typing import List, Optional


def print_message(_, msg): return print(msg)


fastapi_app = FastAPI()

wa = WhatsApp(
    phone_id='273242249210974',
    token='EAAFtnme63bgBO4dI02BeZBfowFGaSZAcm9sgAVmZA0IarGlnSomZAr2ZARjq3iSFZCnl6AemptVf9918XdAWa1pkuQ8t8ZCA51RrlHYcWSTe4VDF1Y9j6ZBUz7RuL2LXrK8yLdD78FMLQ64vx32ZBF7rZA87BO9tvtQ7ljlTAlqgp386BnzjjTSxwsUxr4R9ZBUPSyd',
    server=fastapi_app,
    verify_token='hvjchsdjc'

)


data = {"Pets": ["Tommy", "Charlie", "Cooper"], "services": [
    "Dog Walking", "Adventure Walking", "Nail Clipping"]}


@wa.on_message()
def message_handler(_: WhatsApp, msg: Message):
    number = msg.from_user.wa_id
    if isinstance(number, str) and len(number) > 0:
        services = data.get("services", [])
        buttons = [Button(service, callback_data=service.lower())
                   for service in services]

        wa.send_message(
            to=number,
            text="Choose a service",
            buttons=buttons,
        )

    else:
        print("Invalid phone number or WhatsApp ID:", number)
