# 当前文件实现总控制中心
# 不实现具体的功能, 主要用来负责调度
# 调度整体的业务逻辑


# 1.导入工具包 import 模块名
import cards_tool

class  CardsMain(object):
    def __init__(self):
        self.ct = cards_tool.CardsTool()



    def run(self):
        # 添加死循环
        while True:
            # 2.使用工具包中工具   模块名.函数名()  / 模块名.变量名
            self.ct.show_menu()

            # 3.获取用户的输入信息
            op = input("请输入您的选择:")

            # 4.根据用户输入信息进行判断, 实现不同的功能
            if op in ["1", "2", "3"]:
                # print("用户要实现某个具体的功能", op)
                if op == "1":
                    # 新建名片
                    self.ct.new_card()
                elif op == "2":
                    # 显示全部
                    self.ct.show_all()
                else:
                    # 查询名片
                    self.ct.search_card()
            elif op == "0":
                print("欢迎使用名片管理系统,欢迎下次光临", op)
                # 退出死循环
                break
            else:
                print("您的输入有误,请重新输入", op)


        print("<<<<名片管理系统程序运行结束>>>>")


if __name__ == "__main__":
    # 程序的开始
    # 创建对象
    cm = CardsMain()
    cm.run()