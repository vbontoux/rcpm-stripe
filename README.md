# Stripe tools for RCPM

## price.py command line example

```bash
python price.py -e titi.isabelle@orange.fr -c "RCPM" -s 78024 -n "Vincent Bontoux" -t 0617111111 -p 60
```

## link.py command line example

```bash
echo price_xxxxxxxxxxx | python link.py
```

## price.py combined w/ link.py
```bash
python price.py -e titi.isabelle@orange.fr -c "RCPM" -s 78024 -n "Vincent Bontoux" -t 0617111111 -p 60 | jq -r .id | python link.py  | jq -r .url
```

## Read registration file and create a bash script to create prices and links
```bash
python read_registration_file.py > generated-payment-links.sh
```