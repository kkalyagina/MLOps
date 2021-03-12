from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='my_package',
      version='0.1',
      description='Investment instruments',
      long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
      ],
      url='http://github.com/kkalyagina/my_package',
      author='kkalyagina',
      author_email='kalyagina.kristina@gmail.com',
      license='MIT',
      packages=['my_package'],
      install_requires=[
          'yfinance',
          'matplotlib'
      ],
      entry_points={
          'console_scripts': ['my_package-get_df=my_package.command_line:main'],
      },
      scripts=['bin/my_package-get_df'],
      include_package_data=True,
      zip_safe=False)
