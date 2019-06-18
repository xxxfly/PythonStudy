# -*- coding: utf-8

import hashlib
from .setting import IS_TEST, APP_VERIFY_CODE


class BaseApi(object):
    def authenticate(self, token):
        """
        认证
        """
        if IS_TEST or self.md5(APP_VERIFY_CODE) == token:
            return True
        else:
            return False

        def authenticate_user(self, token, guid):
            """
            登录用户认证
            """
            pass

        def md5(self, str):
            """
            md5加密
            """
            m = hashlib.md5()
            m.update(str.encode('utf-8'))
            return m.hexdigest()

        def is_in_enum(self, enum, key=None, value=None):
            """
            判断是否为枚举值的元素
            """
            pass
