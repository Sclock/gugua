from setuptools import setup, Extension
import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='gugua_bot',
      version='1.1',
      author='Sclock',
      author_email='1342810270@qq.com',
      url='https://github.com/Sclock/gugua',
      description=u'适用于nb的孤寡机器人插件',
      long_description_content_type="text/markdown",
      long_description=long_description,
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      install_requires=['nonebot2', 'asyncio'],
      entry_points={'console_scripts': []})
