#1 模型
from Infrastructure.DI import MetaClass


#2、接口
class IRegionRepository:
    def fetch_province(self):
        """

        :return:
        """
    def fetch_province_by_page(self,start,offset):
        """

        :param start:
        :param offset:
        :return:
        """
    def fetch_province_count(self):
        """

        :return:
        """
#3、协调者
class RegionServince:
    def __init__(self,region_repository):
        self.regionRepository = region_repository
    def get_province_count(self):
        count = self.regionRepository.fetch_province_count()    #获取省份总数
        return count

    def get_province_by_page(self,start,offset):     #根据分页获取省份
        result = self.regionRepository.fetch_province_by_page(start,offset)
        return result

    def get_province(self):     #获取所有省份
        return self.regionRepository.fetch_province()

    def create_province(self,caption):
        exist = self.regionRepository.exist_province(caption)    #先判断省份是否存在，如果存在，该方法返回结果为None
        if not exist:
            self.regionRepository.add_province(caption)   #创建省份
            print(222222)
            return True

    def modify_province(self,nid,caption):
        exist = self.regionRepository.exist_province(caption)
        if not exist:
            self.regionRepository.update_province(nid,caption)  #更新省份
            return True

    def delete_province(self,nid):
        self.regionRepository.remove_province(nid)

    def get_city_by_province(self,province_id):
        rows = self.regionRepository.fetch_city_by_province(province_id)
        return rows

    def get_city_count(self):
        count = self.regionRepository.fetch_city_count()    #获取城市总数
        return count

    def get_city_by_page(self,offset,start):
        result = self.regionRepository.fetch_city_by_page(offset,start)
        return result

    def create_city(self,caption,province_id):
        exist = self.regionRepository.exist_city(caption)   #先判断省份是否存在，如果存在，该方法返回None
        if not exist:
            self.regionRepository.add_city(caption,province_id) #创建省份
            return True

    def delete_city(self,nid):
        self.regionRepository.remove_city(nid)

    def modify_city(self,nid,caption,province_id):
        exist = self.regionRepository.exist_city(caption)
        if not exist:
            self.regionRepository.update_city(nid,caption,province_id)  # 更新城市
            return True

    def create_county(self,caption,city_id):
        exist =self.regionRepository.exist_county(caption)
        if not exist:
            self.regionRepository.add_county(caption,city_id)
            return True

    def get_county_count(self):
        count = self.regionRepository.fetch_county_count()
        return count

    def get_county_by_page(self,start,offset):
        count = self.regionRepository.fetch_county_by_page(start,offset)
        return count

    def delete_county(self,nid):
        self.regionRepository.remove_county(nid)

    def modify_county(self,nid,caption,city_id):
        exist = self.regionRepository.exist_county(caption)
        if not exist:
            self.regionRepository.update_county(nid,caption,city_id)
            return True
    def get_county_by_city(self,city_id):
        rows = self.regionRepository.fetch_county_by_city(city_id)
        print('----',rows)
        return rows


