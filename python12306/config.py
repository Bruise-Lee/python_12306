import os
import yaml
import namedtupled   #namedtuple，你不必再通过索引值进行访问，你可以把它看做一个字典通过名字进行访问，只不过其中的值是不能改变的。


def parsing_config():
    """
    解析yaml （yaml类似于xml语言，但更简洁。）
    :return: s  字典
    """
    path = os.path.join(os.getcwd(), 'config.yaml')
    with open(path, 'r', encoding='utf-8') as f:
        s = yaml.safe_load(f)
    return s


Config = namedtupled.map(parsing_config())
