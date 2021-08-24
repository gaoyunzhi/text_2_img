#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import text_2_img
import os

text = '''【科普】【阅读障碍】

1. 阅读障碍是一种与语言相关的学习障碍，是神经发展障碍的一种。阅读障碍主要影响读写，与智力发展无关。

2. 阅读障碍者可能会在以下任务中遇到困难：幼儿语音发展，将语句拆分为音节，将语句拆分为单词，拼写，短时记忆，阅读理解，速读，写作。阅读障碍有时与家族遗传有关。

3. 如何与阅读障碍者更好的沟通：制作多媒体信息，图文结合，使用 OpenDyslexic 字体，列出重点，划出重点，提供讲稿，提供辅助阅读工具或软件。

4. 阅读障碍者是人类多元性的一种，不是疾病。刨开病理视角，我们可以更容易发现阅读障碍者常常更擅长：空间思维，三维想象，创新，解决问题。

5. 现有的教学方式往往并非为阅读障碍者设计。阅读障碍者需要不同的教学方式。

6. 阅读障碍不是病，所以也不能被治好，也不会自动消失。在恰当教学下，阅读障碍者能够学会阅读。

7. 阅读障碍往往影响到工作和学习，请关注阅读障碍者的需求，为ta们提供应有的帮助和支持。 

原文： https://www.facebook.com/feministnews.us/photos/a.110963062584254/1316491612031387/?type=1&theater
翻译： https://t.me/twitter_translate/284
'''

def test(text):
	# print(text_2_img.getFilename('ss/\nbb.sfsj'))
	background = (255, 255, 255)
	os.system('open ' + text_2_img.gen(text, background = background)[0] + ' -g')
	
if __name__=='__main__':
	test(text)