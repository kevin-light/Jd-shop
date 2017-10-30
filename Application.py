import tornado.ioloop
import tornado.web
import tornado.options
import Config


def load_ui_module(settings):
    model_list = []
    for path in Config.ui_method:
        m = __import__(path,fromlist=True)
        model_list.append(m)
    settings['ui_models'] = model_list

def load_ui_method(settings):
    method_list = []
    for path in Config.ui_method:
        m = __import__(path,fromlist=True)
        method_list.append(m)
    settings['ui_methods'] = method_list

def load_routes(app):
    for route in Config.routes:
        host_pattern = route['host_pattern']
        route_path = route['route_path']
        route_name = route['route_name']

        m = __import__(route_path,fromlist=True)
        pattern_list = getattr(m,route_name)
        app.add_handlers(host_pattern,pattern_list)

def load_hook():
    pass

def start():
    settings = {}

    load_ui_method(settings)
    load_ui_module(settings)
    settings.update(Config.settings)

    application = tornado.web.Application([

    ],**settings)

    load_routes(application)    #加载路由关系

    load_hook()
    application.listen(8000)
    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    start()