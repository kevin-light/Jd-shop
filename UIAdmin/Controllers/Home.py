import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        #调用协调者
        self.render("index.html")