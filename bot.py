#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
if not f'{os.getcwd()}\\'.upper() == f'{__file__.rstrip(os.path.basename(__file__))}'.upper():
    right_path = __file__.rstrip(os.path.basename(__file__))    # 获取当前文件的所在路径
    os.chdir(right_path)    # 将工作路径改至目标路径

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)



def ld(b: str):
    a = "src/plugins/"
    nonebot.load_plugins(a + b)



a = "F:\document\OneDrive - 南京农业大学\My_codes\python\my_bot1\src\plugins"

nonebot.load_builtin_plugins("echo")
nonebot.load_plugin("nonebot_plugin_gocqhttp")
nonebot.load_plugin("nonebot_plugin_remake")
ld('plugin1')


# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
#nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    #nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
