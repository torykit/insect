"""
常量
"""

import util.decorate as decorate


@decorate.singleton
class Constants(object):

    def __init__(self):
        import configparser
        self.parser = configparser
        print("init")
        pass

    def get(self):

        pass

constants = Constants
