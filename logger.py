#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Filename: logger.py
#
#         Author: xwisen 1031649164@qq.com
#    Description: ---
#         Create: 2019-10-04 16:59
#  Last Modified: 2019-10-04 16:59
# ***********************************************

import logging

# 创建logger记录器
logger = logging.getLogger('djangodemo')
logger.setLevel(logging.DEBUG)

# 创建一个控制台处理器，并将日志级别设置为debug。
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 创建formatter格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 将formatter添加到ch处理器
ch.setFormatter(formatter)

# 将ch添加到logger
logger.addHandler(ch)

