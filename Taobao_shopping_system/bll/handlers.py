# --* encoding:utf-8 *--


from templates import show
from utils import convert_dict_2_list, clear_shopping_cart
from dal import shopping_goods_data


class ShowGoodsHandler:
    __instance = None

    def __call__(self, chipscoco):
        print("以下是商城中的所有商品:")
        show.show(chipscoco["goods"])

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = ShowGoodsHandler()
        return cls.__instance


class SortGoodsHandler:
    __instance = None

    def __call__(self, chipscoco):
        order = input("您好，输入指令<asc>对商品按售价进行升序排序，输入指令<desc>对商品按售价进行降序排序:____\b\b\b\b")
        goods = convert_dict_2_list.convert_2_list(shopping_goods_data.TAOBAO)
        length_goods = len(goods)
        if order.lower() == "asc":
            for i in range(length_goods - 1):
                is_sort = False
                for j in range(length_goods - 1 - i):
                    if goods[j]["price"] > goods[j + 1]["price"]:
                        goods[j], goods[j + 1] = goods[j + 1], goods[j]
                        is_sort = True
                if not is_sort:
                    break
        elif order.lower() == "desc":
            for i in range(length_goods - 1):
                is_sort = False
                for j in range(length_goods - 1 - i):
                    if goods[j]["price"] < goods[j + 1]["price"]:
                        goods[j], goods[j + 1] = goods[j + 1], goods[j]
                        is_sort = True
                if not is_sort:
                    break
        show.show(goods, flag=1)

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = SortGoodsHandler()
        return cls.__instance


class AddGoodsHandler:
    __instance = None

    def __call__(self, chipscoco):
        while True:
            id = int(input("请输入商品id:__\b\b"))
            if id in chipscoco["goods"]:
                if id in chipscoco["shopping_cart"]:
                    chipscoco["shopping_cart"][id]["amount"] += 1
                    print("您好，已将商品{}加入购物车".format(chipscoco["goods"][id]["name"]))
                else:
                    chipscoco["shopping_cart"][id] = {"name": chipscoco["goods"][id]["name"],
                                                      "price": chipscoco["goods"][id]["price"], "amount": 1}
                    print("您好，已将商品{}加入购物车".format(chipscoco["goods"][id]["name"]))
            else:
                print("请输入有效的商品id！")
            break

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = AddGoodsHandler()
        return cls.__instance


class ShowShoppingCartHandler:
    __instance = None

    def __call__(self, chipscoco):
        print("这是您的购物清单:")
        show.show(chipscoco["shopping_cart"], flag=2)

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = ShowShoppingCartHandler()
        return cls.__instance


class DeleteGoodsHandler:
    __instance = None

    def __call__(self, chipscoco):
        while True:
            id = int(input("请输入你要删除的商品id:__\b\b"))
            if id in chipscoco["shopping_cart"]:
                if chipscoco["shopping_cart"][id]["amount"] != 0:
                    chipscoco["shopping_cart"][id]["amount"] -= 1
                    if chipscoco["shopping_cart"][id]["amount"] != 0:
                        print("您好，已将商品{}的数量减1。".format(chipscoco["goods"][id]["name"]))
                    else:
                        chipscoco["shopping_cart"].pop(id)
                        print("您好，已将商品{}从购物车中删除。".format(chipscoco["goods"][id]["name"]))
            else:
                print("请输入有效的商品id！")
            break

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = DeleteGoodsHandler()
        return cls.__instance


class PayHandler:
    __instance = None

    def __call__(self, chipscoco):
        ShowShoppingCartHandler()(chipscoco)
        goods = chipscoco["shopping_cart"]
        sum_price = 0
        for id in goods:
            sum_price += goods[id]["amount"] * goods[id]["price"]
        print("总价：{}元，输入指令0进行付款，输入指令1继续购物。".format(sum_price))
        user_input = int(input(""))
        if user_input == 0:
            print("正在前往支付页面，请稍候......")
            clear_shopping_cart.clear_shopping_cart(chipscoco)
        elif user_input == 1:
            print("正在前往购物页面，请稍候......")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = PayHandler()
        return cls.__instance
