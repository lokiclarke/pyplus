
from setuptools import setup, find_packages


setup(
    name='PyPlus',
    version='1.0.3',
    license='MIT',
    author="SSoloSkrips",
    author_email='lokiclarke09@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/lokiclarke/pyplus',
    keywords=['shell','batch','plus','extra','premium'],
    install_requires=['pyfiglet',]
)
