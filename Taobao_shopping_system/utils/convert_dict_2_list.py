def convert_2_list(chipscoco):
    goods = []
    data = chipscoco["goods"]
    for _ in data:
        goods.append({"id": _, "name": data[_]["name"], "price": data[_]["price"], "amount": data[_]["amount"]})
    return goods
