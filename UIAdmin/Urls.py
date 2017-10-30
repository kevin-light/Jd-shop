from .Controllers import Home
from .Controllers import Account
from .Controllers import Region
from .Controllers import Merchant

patterns = [
    # (r"/login.html$", Account.Login),
    (r"/index$", Home.IndexHandler),
    (r"/ProvinceManager.html$", Region.ProvinceManagerHandler),
    (r"/province.html$", Region.ProvinceHandler),
    (r"/CityManager.html$", Region.CityManagerHandler),
    (r"/City.html$", Region.CityHandler),
    (r"/CountyManager.html$", Region.CountyManagerHandler),
    (r"/County.html$", Region.CountyHandler),
    (r"/MerchantManager.html$", Merchant.MerchantManagerHandler),
    (r"/Merchant.html$", Merchant.MerchantHandler),
    (r"/MerchantEdit.html$", Merchant.MerchantEditHandler),

]