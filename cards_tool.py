# 当前文件用来实现名片管理系统中所有的子功能
# 新建名片,显示全部, 查询名片, 修改, 删除, 返回上一级,



class  CardsTool(object):

    def __init__(self):
        # 定义列表,列表中保存字典, 每个字典中保存一个人物详细信息
        # 名片列表定义在所有函数的最上面, 下面所有的函数都能使用到
        self.cards_list = [
            # {"name": "小明", "phone": "10086", "qq": "12345", "email": "xm@qq.com"},
            # {"name": "小红", "phone": "10080", "qq": "23456", "email": "xh@qq.com"},
            # {"name": "小张", "phone": "10090", "qq": "54321", "email": "xz@qq.com"}
        ]


    # 1.显示菜单
    @staticmethod
    def show_menu():
        """当前函数实现菜单显示的功能"""
        print()
        print()
        print("*" * 50)
        print("欢迎使用 [名片管理系统] v1.0")
        print()
        print("1. 新建名片")
        print("2. 显示全部")
        print("3. 查询名片")
        print()
        print("0. 退出系统")
        print("*" * 50)


    # 2.新建名片
    def new_card(self):
        """当前函数实现新建名片功能"""
        # pass占位符起到完善语法结构的作用
        #               不输出任何内容,表示略过
        #               (占用资源, 表示略过)
        # pass
        # 说明: 代码中todo标识代码的完善程度
        print("[功能] 新建名片")
        # 1.获取用户的输入信息
        name_str  = input("请输入姓名:")
        phone_str = input("请输入电话:")
        qq_str    = input("请输入QQ号:")
        email_str = input("请输入邮箱:")

        # 2.将获取的输入信息保存的字典中
        new_dict ={
            "name": name_str,
            "phone": phone_str,
            "qq": qq_str,
            "email": email_str,
        }

        # 3.把字典添加到名片列表中
        self.cards_list.append(new_dict)
        # 4.打印提示信息,新建名片成功
        print("新建姓名是 %s 名片成功 " % name_str)
        # print("打印名片列表cards_list:", cards_list)


    # 3.显示全部
    def show_all(self):
        """当前函数实现显示全部功能"""
        print("[功能] 显示全部")
        """
        ##  TODO 当前函数实现显示全部功能 待完善
        """
        # 0.判断名片列表有没有数据,如果没有数据, 代码不需要继续向下执行
        if len(self.cards_list) <= 0:
            # 代码不需要继续向下执行,return提前终止函数运行
            print("当前名片列表中没有数据,请新建名片!")
            return

        # 1.打印表头信息
        print("-" * 50)
        print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10), sep="\t")
        print("-" * 50)

        # 2.按照格式打印名片列表中数据
        for item in self.cards_list:
            # print(item)   # 临时变量item获取的是名片列表中每一个字典
            print(item["name"].ljust(10), item["phone"].ljust(10),
                  item["qq"].ljust(10), item["email"].ljust(10), sep="\t")



    # 4.查询名片
    def search_card(self):
        """当前函数实现查询名片功能"""
        print("[功能] 查询名片")
        # 1.获取用户要查询的姓名
        find_name = input("请输入您要查询的姓名:")

        # 2.使用for...else...语言遍历名片列表
        for item in self.cards_list:
            # print(item["name"])
            # 判断 名片列表中是否具有 用户要查询的姓名
            if item["name"] == find_name:
                # ① 如果查询到了,需要把 表头 和 人物信息打印出来
                print("已经找到了 %s 的信息了" % item["name"])
                # 打印表头
                print("-" * 50)
                print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10), sep="\t")
                print("-" * 50)
                # 打印表格中信息
                print(item["name"].ljust(10), item["phone"].ljust(10),
                      item["qq"].ljust(10), item["email"].ljust(10), sep="\t")
                print("-" * 50)

                # print("item中的值:", item)   # item中保存的是字典
                # 对当前查询到的人物进行修改处理
                self.deal_card(item)

                # 如果已经找到了,不需要继续向下循环,跳出循环
                break
        # ② 如果整个列表都遍历完成, 没有找到,也需要把 没有找到的信息打印出来
        else:
            print("没有找到姓名是 %s 的信息" % find_name)


    # 5.对名片信息的处理函数
    def deal_card(self, find_dict):
        """当前函数对名片信息的处理"""
        # 1.获取对名片操作的 选择
        action = input("请输入对名片的操作选择[1.修改  2.删除  0.返回上一级菜单]:")
        # 2.对用户输入进行判断,执行不同的操作功能
        # ① 如果用户输入的是 "1", 修改功能
        if action == "1":
            print("[功能] 修改名片")
            # (1).获取用户修改数据的信息
            modify_name  = self.input_card_info( find_dict['name'], "请输入修改后的姓名[不修改直接回车]:")
            modify_phone = self.input_card_info( find_dict['phone'], "请输入修改后的电话[不修改直接回车]:")
            modify_qq    = self.input_card_info( find_dict['qq'], "请输入修改后的QQ号[不修改直接回车]:")
            modify_email = self.input_card_info( find_dict['email'], "请输入修改后的邮箱[不修改直接回车]:")
            # (2).将获取的数据替换字典中 key对应的value值
            find_dict['name']  = modify_name
            find_dict['phone'] = modify_phone
            find_dict['qq']    = modify_qq
            find_dict['email'] = modify_email
            # (3).打印修改名片成功
            print("修改名片成功!")

        # ② 如果用户输入的是 "2", 删除功能
        elif action == "2":
            print("[功能] 删除名片")
            # 从名片列表中删除字典数据
            self.cards_list.remove(find_dict)
            # 打印删除成功
            print("删除成功!")
        # ③ 如果用户输入的是 "0", 返回上一级
        elif action == "0":
            print("[功能] 返回上一级")
            # 返回上一级 return
            return
        # ④ 其他情况, 说明用户输入错误
        else:
            print("您的输入有误,请核对后重新输入!")


    # 6.定义函数,实现对input()函数功能的扩展
    def input_card_info(self, dict_value, tip_message):
        """
        实现对input()函数功能的扩展
        当用户不修改字典中内容,直接回车, 使用字典中key对应value的默认值
        当用户输入了新内容, 将用户输入的内容替换,字典key对应的value值
        """
        # 对input()函数功能扩展
        value = input(tip_message)

        if len(value) <= 0:
            print("用户当前没有输入信息,仅仅是回车")
            print("----->>>>%s<<<---" % value)
            # 用户直接出入回车,没有输入任何内容, 使用字典中默认值
            return dict_value
        else:
            print("用户输入的是--->>>%s<<<---" % value)
            # 使用用户输入的内容替换字典 key对应的value值
            return value








