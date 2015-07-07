from setuptools import setup
import sys

setup(name='py-pageres',
      description='Python tool to Capture Web Screenshots',
      version='1.0.1',
      license='GPL v3.0',
      author='Sriram Sundarraj',
      author_email='ssundarraj@gmail.com',
      packages=['py_pageres'],
      entry_points={
          'console_scripts': ['py-pageres=py_pageres:main'],
      },
      install_requires=[
          'Ghost.py'
      ],
      url='https://github.com/ssundarraj/py-pageres',
      keywords=['screenshot', 'webpage screenshot', 'python'],
      classifiers=[
          'Operating System :: POSIX',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
