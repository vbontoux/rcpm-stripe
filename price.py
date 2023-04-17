import stripe
import json
import config
import openpyxl
import argparse
import re
from os import getenv
from dotenv import load_dotenv
load_dotenv()

stripe_product= getenv('STRIPE_PRODUCT')
stripe.api_key = getenv('STRIPE_API_KEY')

date_str = config.race_date.strftime("%d/%m/%Y")

def is_valid_email(email):
  regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
  if re.fullmatch(regex, email):
    return True
  else:
    return False

def create_price(amount, **kwargs):

  metadata = kwargs
  metadata["race_date"] = config.race_date.strftime("%Y-%m-%d")
  metadata["date"] = date_str
  email = metadata["email"]
  print(metadata)

  res = stripe.Price.create(
    nickname=f"{config.race_title} {date_str} - {email}",
    unit_amount=int(amount)*100, # = 100 x 0.01 eur
    currency="eur",
    product=stripe_product,
    metadata=metadata
  )
  print(json.dumps(res, indent=2))  



argParser = argparse.ArgumentParser()
argParser.add_argument("-c", "--club", required = True, help="nom du club")
argParser.add_argument("-s", "--structure", required = True, help="numéro de structure")
argParser.add_argument("-n", "--name", required = True, help="nom du responsable")
argParser.add_argument("-e", "--email", required = True, help="delegate email")
argParser.add_argument("-t", "--telephone", required = True, help="delegate email")
argParser.add_argument("-p", "--price", required = True, help="delegate email")

args = argParser.parse_args()
print(f"Nom du club : {args.club}")
print(f"Numéro de structure : {args.structure}")
print(f"Nom du responsable : {args.name}")
print(f"Numéro de téléphone : {args.telephone}")
print(f"Prix : {args.price}")
print(f"Email: {args.email}" if is_valid_email(args.email) else "Invalid email")
print(args.__dict__)
create_price(amount=args.price, **args.__dict__)


# Command line example 
# python price.py -e titi.isabelle@orange.fr -c "RCPM" -s 78024 -n "Vincent Bontoux" -t 0617111111 -p 60



