#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'text_2_img'

#!/usr/bin/env python
# coding: utf-8

# You need PIL <http://www.pythonware.com/products/pil/> to run this script
# Download unifont.ttf from <http://unifoundry.com/unifont.html> (or use
# any TTF you have)
# Copyright 2011 Álvaro Justen [alvarojusten at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

from .image_utils import ImageText
import os
import re

#You don't need to specify text size: can specify max_width or max_height
# and tell write_text to fill the text in this space, so it'll compute font
# size automatically
#write_text will return (width, height) of the wrote text
# img.write_text((100, 350), 'test fill', font_filename=font,
#                font_size='fill', max_height=150, color=color)


def getFilename(text, dirname = 'tmp'):
	text = re.sub(r'[-\s]+', '', text)
	return text[:10]

heiti_loc = '/System/Library/Fonts/STHeiti Light.ttc'
other_font_loc = '~/Library/Fonts/SourceHanSerifSC-Light.otf'

def gen(text, dirname = 'tmp', font=other_font_loc):
	os.system('mkdir %s > /dev/null 2>&1' % dirname)
	color = (50, 50, 50)
	# 是不是要划线
	img = ImageText((900, 1600), background=(252, 250, 222, 200))  # 200 => 255?
	print(img.write_text_box((50, 50), text, box_width=800, font_filename=font, font_size=40, color=color))
	fn_base = dirname + '/' + getFilename(text)
	f0 = fn_base + '_0.png'
	img.save(f0)
	return [f0]

