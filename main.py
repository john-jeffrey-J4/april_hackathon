
import uvicorn
from fastapi import FastAPI
from pywa import WhatsApp
from pywa.types import Message, Button
def print_message(_, msg): return print(msg)


fastapi_app = FastAPI()

wa = WhatsApp(
    phone_id='273242249210974',
    token='EAAFtnme63bgBO4dI02BeZBfowFGaSZAcm9sgAVmZA0IarGlnSomZAr2ZARjq3iSFZCnl6AemptVf9918XdAWa1pkuQ8t8ZCA51RrlHYcWSTe4VDF1Y9j6ZBUz7RuL2LXrK8yLdD78FMLQ64vx32ZBF7rZA87BO9tvtQ7ljlTAlqgp386BnzjjTSxwsUxr4R9ZBUPSyd',
    server=fastapi_app,
    verify_token='hvjchsdjc'

)


data = {"916369135307":{"Pets":["Tommy","Charlie","Cooper"]}}


@wa.on_message()
def message_handler(_: WhatsApp, msg: Message):
    number = msg.from_user.wa_id
    if isinstance(number, str) and len(number) > 0:
        pets = data.get(number, {}).get("Pets", [])
        buttons = [Button(pet, callback_data=pet.lower()) for pet in pets]

        wa.send_message(
            to=number,
            text="Choose a pet to book the service",
            buttons=buttons,
        )
    else:
        print("Invalid phone number or WhatsApp ID:", number)
        
        
