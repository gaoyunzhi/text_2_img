#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import text_2_img
import os

text = '''根据1873年以来的传统，法庭入口和已故法官金斯伯格的法官席上披上了黑色羊毛绉纱。

原文： https://www.facebook.com/feministnews.us/photos/a.110963062584254/1316491612031387/?type=1&theater
翻译： https://t.me/twitter_translate/284
'''

def test(text):
	os.system('open ' + text_2_img.gen(text)[0] + ' -g')
	
if __name__=='__main__':
	test(text)