#实现业务接口、具体SQL语句，pymysql

from Model.User import IuserRepository
from Repository.DbConnection import DbConnection
# from .DbConnection import     #同目录下，相对路径导入
from Model.User import UserTypeModel
from Model.User import VipModel
from Model.User import UserModel

class UserRepository(IuserRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_user(self):
        cursor = self.db_conn.connect()
        sql = """select nid as value,username as text from userinfo"""
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_one_by_email_pwd(self,email,pwd):
        #自己拼接SQL语句，不能直接用select 防止SQL注入
        ret = None
        cursor = self.db_conn.connect()
        sql = """select nid,username,email,last_login,vip,user_type from UserInfo where email = %s and password = %s"""
        #执行SQL
        cursor.execute(sql, (email, pwd))
        # 获取第一行数据
        db_result = cursor.fetchone()
        self.db_conn.close()
        if db_result:
            obj = UserModel(
                nid=db_result['id'],
                username=db_result['username'],
                email=db_result['email'],
                last_login=db_result['last_login'],
                vip_obj=VipModel(nid=db_result['vip']),  # vip_obj是对象VIPModel， m['vip']是一个数字
                user_type_obj=UserTypeModel(nid=db_result['user_type'])
            )
            return obj

        return db_result

    def fetch_one_by_user_pwd(self,user,pwd):
        pass