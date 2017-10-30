import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #调用协调者
        self.write("Hello, world")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        #调用协调者
        self.write("hello")
    def post(self, *args, **kwargs):
        user = 'alvin'
        pwd = '123'
        from Model.User import UserService
        from Repository.UserRepository import UserRepository
        service = UserService(UserRepository())
        obj = service.check_login(user=user,email=None,pwd=pwd)
        # obj封装了所有用户的信息，UserMode
        print(obj.username)
        print(obj.email)
        print(obj.vip_obj.nid)
        print(obj.vip_obj.caption)