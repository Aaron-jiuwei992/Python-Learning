# --* encoding:utf-8 *--


def show(goods, flag=0):
    tr = "+" + "-" * 5 + "+" + "-" * 10 + "+" + "-" * 15 + "+" + "-" * 5 + "+"
    heading = "|{:^5s}|{:^7s}|{:^13s}|{:^3s}|".format("id", "商品名", "售价", "数量")
    print(tr + "\n" + heading + "\n" + tr + "\n")
    if flag == 0:
        # flag为0，直接展示所有商品
        for _ in goods:
            print("|{0:^5d}|{1:{4}^5s}|{2:{5}^8d}|{3:^5d}|".format(_, goods[_]["name"], goods[_]["price"],
                                                                   goods[_]["amount"], chr(12288), chr(12288)))
        print(tr)
    elif flag == 1:
        # flag为1，展示排序后的商品
        for _ in goods:
            print("|{0:^5d}|{1:{4}^5s}|{2:{5}^8d}|{3:^5d}|".format(_["id"], _["name"], _["price"], _["amount"],
                                                                   chr(12288), chr(12288)))
        print(tr)
    else:
        # 展示购物车
        for _ in goods:
            print("|{0:^5d}|{1:{4}^5s}|{2:{5}^8d}|{3:^5d}|".format(_, goods[_]["name"], goods[_]["price"],
                                                                   goods[_]["amount"], chr(12288), chr(12288)))
        print(tr)
