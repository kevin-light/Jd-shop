#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Infrastructure.Form.Forms import BaseForm
from Infrastructure.Form.Fields import StringField
from Infrastructure.Form.Fields import IntegerField
from Infrastructure.Form.Fields import EmailField
from Infrastructure.Form import Widget

from Model.User import UserService
from Repository.UserRepository import UserRepository

class MerchantForm(BaseForm):

    def __init__(self):
        self.nid = IntegerField(required=False, widget=Widget.InputText(attributes={'class': 'hide'}))

        self.name = StringField(custom_error_dict={'required': '名称不能为空', 'valid': '名称格式错误'})
        self.domain = StringField(custom_error_dict={'required': '域名不能为空', 'valid': '域名格式错误'})

        self.business_mobile = StringField(custom_error_dict={'required': '业务电话不能为空', 'valid': '业务电话格式错误'})
        self.business_phone = StringField(custom_error_dict={'required': '业务手机不能为空', 'valid': '业务手机格式错误'})
        self.qq = StringField(custom_error_dict={'required': 'QQ不能为空', 'valid': 'QQ格式错误'})
        self.address = StringField(widget=Widget.TextArea(attributes={'class': 'address'}),
                                   custom_error_dict={'required': '地址信息不能为空', 'valid': '地址信息格式错误'})
        self.backend_mobile = StringField(custom_error_dict={'required': '负责人电话不能为空', 'valid': '负责人电话格式错误'})
        self.backend_phone = StringField(custom_error_dict={'required': '负责人手机不能为空', 'valid': '负责人手机格式错误'})

        self.user_id = IntegerField(
            widget=Widget.Select(attributes={}, choices=UserService(UserRepository()).get_user_to_select()),
            custom_error_dict={'required': '请选择登录用户', 'valid': '选择登录用户错误'})

        self.province_id = IntegerField(
            widget=Widget.Select(attributes={'id': 'province'}, choices=[{'value': 0, 'text': '请选择省份'}]),
            custom_error_dict={'required': '请选择省', 'valid': '省选择错误'})
        self.city_id = IntegerField(
            widget=Widget.Select(attributes={'id': 'city'}, choices=[{'value': 0, 'text': '请选择市'}]),
            custom_error_dict={'required': '请选择市', 'valid': '市选择错误'})
        self.county_id = IntegerField(
            widget=Widget.Select(attributes={'id': 'county'}, choices=[{'value': 0, 'text': '请选择县（区）'}]),
            custom_error_dict={'required': '请选择县(区)', 'valid': '县(区)选择错误'})

        super(MerchantForm, self).__init__()

