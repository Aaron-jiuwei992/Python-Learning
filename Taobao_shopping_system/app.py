# --* encoding:utf-8 *--
# 使用面向对象的思想构建一个简单的在线商城购物系统
# author: Aaron-jiuwei992

from dal import shopping_goods_data
from bll import handlers


class ShoppingSystem:
    def __init__(self, data):
        self.__data = data
        self.welcome_prompt = "您好，欢迎使用淘宝在线购物系统，输入<>中对应的指令来使用系统:\n"
        self.prompt = []
        self.quit_prompt = "<quit>:退出本系统\n请输入指令:____\b\b\b\b"
        self.__exit_commands = {"quit", "退出"}
        self.__handlers = {}
        self.__index = 1

    def add_handler(self, handler, prompt):
        self.__handlers[self.__index] = handler.get_instance()
        self.__index += 1
        self.prompt.append(prompt)

    def __generate_prompt(self):
        prompt = self.welcome_prompt
        for index, value in enumerate(self.prompt):
            prompt += "<{}>:{}\n".format(index+1, value)
        prompt += self.quit_prompt
        return prompt

    def __obtain_user_input(self, prompt):
        # 假定一开始的指令为合法
        command, valid = "quit", True
        try:
            command = input(prompt)
            _ = self.__handlers[int(command)]

        except (ValueError, KeyError):
            command = command.lower()
            if command not in self.__exit_commands:
                valid = False
        return command, valid

    def serve_forever(self):
        prompt = self.__generate_prompt()
        while True:
            command, valid = self.__obtain_user_input(prompt)
            if not valid:
                print("您输入了非法的指令，请重新输入！")
            else:
                if command in self.__exit_commands:
                    print("Bye,欢迎下次光临！")
                    break
                _ = self.__handlers[int(command)](self.__data)
        _ = input("按下键盘任意键，继续使用该系统...")


if __name__ == '__main__':

    TAOBAO = ShoppingSystem(shopping_goods_data.TAOBAO)
    TAOBAO.add_handler(handlers.ShowGoodsHandler, "展示所有商品")
    TAOBAO.add_handler(handlers.SortGoodsHandler, "对商品按售价进行排序(asc表示升序，desc表示降序)")
    TAOBAO.add_handler(handlers.AddGoodsHandler, "添加商品到购物车")
    TAOBAO.add_handler(handlers.ShowShoppingCartHandler, "查看购物车")
    TAOBAO.add_handler(handlers.DeleteGoodsHandler, "删除购物车指定商品")
    TAOBAO.add_handler(handlers.PayHandler, "下单结账")

    TAOBAO.serve_forever()
