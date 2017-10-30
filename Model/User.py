#1、模型
class UserTypeModel:
    USER_TYPE = (
        {'nid': 1, 'caption': '用户'},
        {'nid': 2, 'caption': '商户'},
        {'nid': 3, 'caption': '用户管理员'},
    )

    def __init__(self,nid):
        self.nid = nid
    # @property       #方发一： 装饰器，负责把一个方法变成属性调用
    # def caption(self):
    #     for item in UserTypeModel.USER_TYPE:
    #         if item['nid'] == self.nid:
    #             return item['caption']

    def get_caption(self):
        for item in UserTypeModel.USER_TYPE:
            if item['nid'] == self.nid:
                return item['caption']
    caption = property(fget=get_caption)      #方发二：方法变成属性调用

class VipModel:
    VIP_TYPE = (
        {'nid': 1, 'caption': '铜牌'},
        {'nid': 2, 'caption': '银牌'},
        {'nid': 3, 'caption': '金牌'},
        {'nid': 4, 'caption': '铂牌'},
    )

    def __init__(self,nid):
        self.nid = nid

    def caption(self):
        for item in VipModel.VIP_TYPE:
            if item['nid'] == self.nid:
                return item['caption']

class UserModel:
    def __init__(self,nid,username,email,last_login,vip_obj,user_type_obj):
        self.nid = nid
        self.username = username
        self.email = email
        self.last_login = last_login
        self.vip_obj = vip_obj  #{vip:1,金牌会员}
        self.user_type_obj = user_type_obj  #{user_type_obj:1,普通用户}

#2、接口
class IuserRepository:
    def fetch_one_by_user_pwd(self,user,pwd):
        #根据用户名和密码获取对象
        pass

    def fetch_one_by_email_pwd(self,email,pwd):
        #根据邮箱和密码获取对象
        pass

#3、协调
class UserService:
    def __init__(self,user_repository):
        #数据仓库的对象
        self.userRepository = user_repository

    def get_user_to_select(self):
        user_list = self.userRepository.fetch_user()
        return user_list

    def check_login(self,user,email,pwd):
        if user:
            # 数据仓库执行SQL返回的字典 m={‘nid':asdf,username:xcgvs, 'vip':1,'usertype':1}
            m = self.userRepository.fetch_one_by_user_pwd(user,pwd)
        else:
            m = self.userRepository.fetch_one_by_email_pwd(email,pwd)
        # m是对象或者是None，


        return m
