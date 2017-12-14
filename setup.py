from setuptools import setup, find_packages


install_requires = [
    # 'progressbar',
    'colorlog'
]

setup(
    name='PyLogger',
    version='1.1.0',
    packages=find_packages(),
    url='http://github.com/junlulocky/PyLogger/',
    license='MIT',
    install_requires=install_requires,
    author='locky1218',
    author_email='jun.lu.locky@gmail.com',
    description='A light weight Python package for logger results',
    long_description=open('README.md').read(),
    keywords="python, logger",
    # platform=['any'],
)


