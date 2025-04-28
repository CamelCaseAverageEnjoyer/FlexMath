from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='flexmath',
  version='1.0.0',
  author='CamelCaseAverageEnjoyer',
  author_email='orlov-vladislove@yandex.ru',
  description='List of basic functions that work with both Numpy and SymPy simultaneously.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/CamelCaseAverageEnjoyer/FlexMath',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.10',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='sympy numpy polymorphism',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)
