#定义公共类
class AccountTile:
    #定义会计科目
    def __init__(self,Aid,Aname,AccCla,Current=0,Quantity=0,unit=(),Auxiliary=()):
        self.__id=Aid  #科目代码
        self.__name=Aname  #科目名称
        self.__acc_cla=AccCla  #科目类别
        self.__current=Current  #是否业务往来核算，默认否
        self.__quantity=Quantity  #是否数量金额核算，默认否
        self.__unit=unit  #计量单位
        sefl.__auxiliary = Auxiliary  #辅助核算项目

class Asset(AccountTile):
    def __init__(self,balance='借'):
        super().__init__()
        self.__balance=balance

class Auxiliary:
    #定义辅助核算项目
    def __init__(self,Aid,Aname,AccCla,Current=0,Quantity=0,unit=(),Auxiliary=()):
        self.__id=Aid  #核算项目代码
        self.__name=Aname  #核算项目名称

