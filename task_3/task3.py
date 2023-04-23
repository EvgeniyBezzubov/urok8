import yaml

lst = ["computer", "printer", "keyboard", "mouse"]
slovar2 = {"mouse": "50€", "keyboard": "20€"}
slovar = {"items": lst, "sssss": 5, 'item_price': slovar2}

with open('data_write.yaml', 'w') as f_n:
    yaml.safe_dump(slovar, f_n, allow_unicode=True, default_flow_style=False)

with open('data_write.yaml') as f_n:
    print(f_n.read())
