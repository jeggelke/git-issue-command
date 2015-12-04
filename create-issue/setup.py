from setuptools import setup

setup(name='create-issue',
      version='0.1',
      description='Send issues to gitgub or bitbucket',
      url='http://github.com/jeggelke/python-assessment',
      author='Jake Heggelke',
      author_email='jacob.heggelke@gmail.com',
      license='MIT',
      packages=['create-issue'],
      install_requires=['requests'],
      dependency_links=['https://pypi.python.org/packages/2.7/r/requests/requests-2.8.1-py2.py3-none-any.whl#md5=46f1d621daa3ab38958a42f51478b1ee'],
      scripts=['bin/create-issue'],
      zip_safe=False)
