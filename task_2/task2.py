import json
def write_order_to_json(item,quantity,price,buyer,date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('mes_example_write_3.json', 'a') as f_n:
        json.dump(dict_to_json, f_n, sort_keys=True, indent=4)

    with open('mes_example_write_3.json') as f_n:
        print(f_n.read())


write_order_to_json("qr-scanner","5","10000","Albion-2002","23.04.2023")
