from setuptools import setup

setup(name='StatsPykage',
      version='1.1',
      description='StatsPykage is an open source Python package for analysing standard statistical distributions: Gaussian, Binomial, Poisson etc..',
      packages=['StatsPykage'],
      license='MIT',
      author='VoidCodez, VaasuCodez',
      install_requires=[
      	'math',
      	'matplotlib',
      ],
      zip_safe=False)
