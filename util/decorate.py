"""
装饰器
"""


def singleton(cls, *args, **kw):
    """
        使用singleton装饰器后,该类成为单例类
    """
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton
