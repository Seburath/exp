from setuptools import setup, find_packages


setup(name='cyberhead',
      version='1.0',
      url='https://github.com/TheCyberHead',
      license='MIT',
      author='CyberHead LLC',
      author_email='info@cyberhead.com',
      entry_points={"console_scripts": ["cyberhead = cyberhead.wrapper:cli"]},
      description='Modular Open Source Trading',
      packages=find_packages(),
      long_description=open('README.rst').read(),
      long_description_content_type='text/x-rst',
      zip_safe=False,
 )
