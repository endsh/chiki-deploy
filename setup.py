# coding: utf-8
import re
import os
from setuptools import setup, find_packages


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('chiki_deploy/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


def get_data_files(*dirs):
    results = []
    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            results.append((root, map(lambda f: root + "/" + f, files)))
    return results


setup(
    name='chiki-deploy',
    version='0.0.1',
    url='https://github.com/endsh/chiki-deploy',
    author='Linshao',
    author_email='438985635@qq.com',
    description='chiki deploy libs.',
    py_modules=['chiki_deploy'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Fabric==1.10.2',
    ],
)
