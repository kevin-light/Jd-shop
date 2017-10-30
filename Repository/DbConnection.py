import Config
import pymysql


class DbConnection:
    def __init__(self):
        self.__conn_dict = Config.PY_MYSQL_CONN_DICT
        self.conn = None
        self.cursor = None

    def connect(self,cursor=pymysql.cursors.DictCursor):
        self.conn = pymysql.connect(**self.__conn_dict,charset="utf8")
        self.cursor = self.conn.cursor(cursor=cursor)
        return self.cursor

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


