import tornado.web
import json
from Model.Region import RegionServince
from Repository.RegionRepository import RegionRepository
from ..Core.HttpRequest import AdminRequestHandler


class ProvinceHandler(AdminRequestHandler):
    def get(self,*args,**kwargs):
        #调用协调者,获取param args, param kwargs, return
        if self.get_argument('type',None) == 'all':
            ret = {'status':True,'rows':'','summary':''}
            try:
                region_service = RegionServince(RegionRepository())     #将数据库处理类的对象传入业务协调类
                all_province_list = region_service.get_province()
                ret['rows'] = all_province_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str[e]
            self.write(json.dumps(ret))     #返回给前端
        else:
            # 如果获取分也数据
            ret = {'status':True,'total':0,'rows':[],'summary':''}
            try:
                rows = int(self.get_argument('rows',10))    #每页显示10条
                page = int(self.get_argument('page',1))     #显示第一页
                start = (page - 1) * rows   #开始条数
                region_service = RegionServince(RegionRepository())
                row_list = region_service.get_province_by_page(start,rows)  #根据分页获取省份数据
                row_count = region_service.get_province_count()     #获取省份总数

                ret['total'] = row_count
                ret['rows'] = row_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)
            self.write(json.dumps(ret))

    def post(self, *args, **kwargs):
        """
        添加
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status':False,'summary':''}
        caption = self.get_argument('caption',None)
        if not caption:
            ret['summary'] = '省份不能为空'
        else:
            try:
                region_service = RegionServince(RegionRepository())
                result = region_service.create_province(caption)    #创建省份，如果省份已存在，返回None
                if not result:
                    ret['summary'] = '省份已存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))     #返回给前端

    def put(self,*args,**kwargs):
        """
        更新
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status':False,'summary':''}
        nid = self.get_argument('nid',None)
        caption = self.get_argument('caption',None)
        if not caption or not nid:
            ret['summary'] = '省份不能为空'
        else:
            try:
                region_service = RegionServince(RegionRepository())
                result = region_service.modify_province(nid,caption)
                if not result:
                    ret['summary'] = '省份已存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        """
        删除
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status':False,'summary':''}
        nid = self.get_argument('nid',None)
        if not nid:
            ret['summary'] = '请选择要删除的省份'
        else:
            # 调用service去删除吧。。。如果删除失败，则显示错误信息
            try:
                region_service = RegionServince(RegionRepository())
                region_service.delete_province(nid)     #根据nid删除省份
                ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

class ProvinceDataHandler(AdminRequestHandler):
    def get(self):
        #调用协调者
        total = 89
        all_list = []
        #省份数据显示 及 easyui分页设置（page，rows）
        for item in range(total):
            temp = {'nid':item,'caption':'省_'+str(item)}
            all_list.append(temp)
        page = int(self.get_argument('page',1))
        rows = int(self.get_argument('rows',10))
        start = (page-1)*rows
        end = page * rows
        data_list = all_list[start:end]
        ret = {'total':total,'rows':data_list}
        import json
        self.write(json.dumps(ret))

class ProvinceManagerHandler(AdminRequestHandler):
    def get(self,*args,**kwargs):
        #打开页面显示所有省
        self.render('Region/ProvinceManager.html')

class CityManagerHandler(AdminRequestHandler):
    def get(self, *args, **kwargs):
        # 调用协调者
        self.render("Region/CityManager.html")

class CityHandler(AdminRequestHandler):
    def get(self, *args, **kwargs):
        """
        获取
        :param args:
        :param kwargs:
        :return:
        """
        if self.get_argument('type',None) == 'province':    #如果是获取省份的所有数据
            ret = {'status':True,'rows':'','summary':''}
            try:
                province_id = self.get_argument('province_id',None)
                if not province_id:
                    ret['status'] = False
                    ret['summary'] = '请指定省份ID'
                else:
                    region_service = RegionServince(RegionRepository()) #将数据库处理类的对象传入数据库业务协调类
                    rows = region_service.get_city_by_province(province_id) #获取所有省份
                    ret['rows'] = rows  #将省份数据添加进返回前端的字典
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)
            self.write(json.dumps(ret))  #返回给前端
        else:   #如果获取分页数据
            ret = {'status':'True','rows':[],'total':0,'summary':''}
            try:
                rows = int(self.get_argument('rows',10))    #每页显示条数
                page = int(self.get_argument('page',1))     #显示第一页
                start = (page - 1) * rows
                region_service = RegionServince(RegionRepository())
                row_list = region_service.get_city_by_page(rows,start)  #根据分页获取城市数据
                row_count = region_service.get_city_count()     #获取城市总数
                ret['total'] = row_count
                ret['rows'] = row_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)
            self.write(json.dumps(ret))

    def post(self, *args, **kwargs):
        """
        添加
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status':False,'summary':''}
        caption = self.get_argument('caption',None)
        province_id = self.get_argument('province_id',None)
        if not caption:
            ret['summary'] = '城市不能为空'
        else:
            try:
                region_service = RegionServince(RegionRepository())
                result = region_service.create_city(caption,province_id)
                if not result:
                    ret['summary'] = '城市已存在'
                else:
                    ret['status'] = 'True'  #操作成功
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def put(self, *args, **kwargs):
        """
        更新
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status':'False','summary':''}
        nid = self.get_argument('nid',None)
        caption = self.get_argument('caption',None)
        province_id = self.get_argument('province_id',None)
        if not caption or not nid:
            ret['summary'] = '城市不能为空 '
        else:
            try:
                region_service = RegionServince(RegionRepository())
                result = region_service.modify_city(nid,caption,province_id)
                if not result:
                    ret['summary'] = '城市已存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def delete(self,*args,**kwargs):
        """
        删除
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status':False,'summary':''}
        nid = self.get_argument('nid',None)
        if not nid:
            ret['summary'] = '请选择要删除的省市'
        else:
            try:
                region_service = RegionServince(RegionRepository())
                result = region_service.delete_city(nid)
                ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

class CountyManagerHandler(AdminRequestHandler):
    def get(self,*args,**kwargs):
        #调用协调者
        self.render("Region/CountyManager.html")

class CountyHandler(AdminRequestHandler):
    def get(self, *args, **kwargs):
        """
            获取
            :param args:
            :param kwargs:
            :return:
            """
        if self.get_argument('type',None) == 'city':
            ret = {'status':True,'rows':[],'summary':''}
            try:
                city_id = self.get_argument('city_id',None)
                if not city_id:
                    ret['summary'] = '请指定市ID'
                    ret['status'] = False
                else:
                    region_service = RegionServince(RegionRepository())
                    rows = region_service.get_county_by_city(city_id)
                    ret['rows'] = rows
            except Exception as e:
                ret['summary'] = str(e)
                ret['status'] = False
            self.write(json.dumps(ret))
        else:
            ret = {'status':True,'total':0,'rows':[],'summary':''}
            try:
                rows = int(self.get_argument('rows',6))    #每页显示10条
                page = int(self.get_argument('page',1))     #显示第一页
                start = (page - 1) * rows       #开始条数
                region_service = RegionServince(RegionRepository())
                row_list = region_service.get_county_by_page(rows,start)  #根据分页获取城市数据
                row_count = region_service.get_county_count()     #获取城市总数
                ret['total'] = row_count
                ret['rows'] = row_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)
            self.write(json.dumps(ret))

    def post(self, *args, **kwargs):
        """
        添加
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status':False,'summary':''}
        caption = self.get_argument('caption',None)
        city_id = self.get_argument('city_id',None)
        if not caption:
            ret['summary'] = '县不能为空'
        else:
            try:
                region_service = RegionServince(RegionRepository())
                result = region_service.create_county(caption,city_id)     #创建县，如果已存在返回None
                if not result:
                    ret['summary'] = '县已存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def put(self, *args, **kwargs):
        """
        更新
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status':False,'summary':''}
        nid = self.get_argument('nid',None)
        caption = self.get_argument('caption',None)
        city_id = self.get_argument('city_id',None)
        if not caption or not nid:
            ret['summary'] = '城市不能为空'
        else:
            try:
                region_service = RegionServince(RegionRepository())
                result = region_service.modify_county(nid,caption,city_id)
                if not result:
                    ret['summary'] = '城市已存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def delete(self,*args,**kwargs):
        """
        删除
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status':False,'summary':''}
        nid = self.get_argument('nid',None)
        if not nid:
            ret['summary'] = '请选择要删除的县'
        else:
            #调用service删除，如果删除失败显示错误信息
            try:
                region_service = RegionServince(RegionRepository())
                region_service.delete_county(nid)
                ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

