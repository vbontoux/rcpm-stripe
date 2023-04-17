import stripe
from os import getenv
import argparse
import json
from dotenv import load_dotenv
load_dotenv()

stripe.api_key = getenv('STRIPE_API_KEY')

def create_link(price_id, **kwargs) : 
  res = stripe.PaymentLink.create(
    line_items=[
      {
        "price": price_id,
        "quantity": 1,
      },
    ],
    metadata=kwargs
  )
  print(json.dumps(res, indent=2))


argParser = argparse.ArgumentParser()
argParser.add_argument("-p", "--price", required = False, help="Identifiant du price stripe", default="")
args = argParser.parse_args()
price_id = args.price
if not price_id :
  price_id = input()

# print(f"Input is {price_id}")

create_link(price_id=price_id)
