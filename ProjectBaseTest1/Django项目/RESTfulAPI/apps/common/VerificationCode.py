"""
图片验证码
"""

import os
import random
from io import BytesIO
from PIL import Image
from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype

class Bezier(object):
    """贝塞尔曲线"""

    def __init__(self):
        self.tsequense = tuple([t/20.0 for t in range(21)])
        self.beziers = {}
    
    def make_bezier(self,n):
        """绘制贝塞尔曲线"""
        try:
            return self.beziers[n]
        except KeyError:
            combinations = pascal_row(n - 1)
            result = []
            for t in self.tsequense:
                tpowers = (t ** i for i in range(n))
                upowers = ((1-t) ** i for i in range(n - 1, -1 ,-1))
                cofes = [c * a * b for c, a, b in zip(combinations, tpowers, upowers)]

                result.append(cofes)
            self.beziers[n] = result

            return result

class Captcha(object):
    """验证码"""

    def __init__(self, width, height, fonts=None, color=None):
        self._image = None
        self._fonts = fonts if fonts else [os.path.join(os.path.dirname(__file__), 'fonts', font) for font in ['Action.ttf', 'Silom.ttf', 'Verdana.ttf']]
        self._color = color of color else random_color(0, 200, random.randint(220, 255))
        self._width, self._height = width, height








