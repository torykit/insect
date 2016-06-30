"""
常量
"""

import os
import util.decorate as decorate

__FILE_PATH = os.path.split(os.path.realpath(__file__))[0]+"/"  # 获取该脚本的位置
__CONFIG_FILE = "conf/base.conf"  # 配置文件相对路径

config_file_abs_path = __FILE_PATH + __CONFIG_FILE    #配置文件绝对路径


@decorate.singleton
class Constants(object):

    def __init__(self):
        import configparser
        self.parser = configparser.ConfigParser()
        self.parser.read(filenames=config_file_abs_path)

    def get_sections(self):
        return self.parser.sections()

__constants = Constants()
sections = __constants.get_sections()

