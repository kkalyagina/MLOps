from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='kk_lab',
      version='0.1',
      description='Investment instruments',
      long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
      ],
      url='http://github.com/kkalyagina/kk_lab',
      author='kkalyagina',
      author_email='kalyagina.kristina@gmail.com',
      license='MIT',
      packages=['kk_lab'],
      install_requires=[
          'yfinance',
          'matplotlib'
      ],
      entry_points={
          'console_scripts': ['kk_lab-get_df=kk_lab.command_line:main'],
      },
      scripts=['bin/kk_lab-get_df'],
      include_package_data=True,
      zip_safe=False)
