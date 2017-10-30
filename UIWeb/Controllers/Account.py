#!/usr/bin/env python
# -*- coding:utf-8 -*-
import io
from Infrastructure import CheckCode
from ..Core.HttpRequest import WebRequestHandler



class CheckCodeHandler(WebRequestHandler):
    def get(self, *args, **kwargs):
        stream = io.BytesIO()
        img, code = CheckCode.create_validate_code()
        img.save(stream, "png")
        # self.session["CheckCode"] = code
        self.write(stream.getvalue())


class LoginHandler(WebRequestHandler):

    def get(self, *args, **kwargs):
        self.render('Account/Login.html')


class LogoutHandler(WebRequestHandler):

    def get(self, *args, **kwargs):

        self.redirect('/Login.html')


class RegisterHandler(WebRequestHandler):

    def get(self, *args, **kwargs):
        self.render('Account/Register.html')










