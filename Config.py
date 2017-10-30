routes = (
    {
        'host_pattern':'www.kevin.com',       # 配置 host
        'route_path': 'UIWeb.Urls',
        'route_name': 'patterns',
    },
    {
        'host_pattern':'admin.kevin.com',
        'route_path': 'UIAdmin.Urls',
        'route_name': 'patterns',
    },
    {
        'host_pattern': 'dealer.kevin.com',
        'route_path': 'UIDealer.Urls',
        'route_name': 'patterns',
    },
)

ui_method = (
    'Infrastructure.UIMethods.Null',
)

ui_method = (
    'Infrastructure.UIMethods.Null',
)

settings = {
    'template_path': 'Views',
    'static_path': 'Statics',
    'static_url_prefix': '/Statics/',
}

PY_MYSQL_CONN_DICT = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '111111',
    'db': 'ShoppingDb',
}