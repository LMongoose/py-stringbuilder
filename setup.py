from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'py-stringbuilder',
  packages = ['py-stringbuilder'],
  version = '0.0.1',
  license = 'GNU GPLv3',
  description = 'TYPE YOUR DESCRIPTION HERE',
  long_description = long_description,
  author = 'LMongoose',
  author_email = 'lukaspellezario@hotmail.com',
  url = 'https://github.com/LMongoose/py-stringbuilder',
  download_url = 'https://github.com/LMongoose/py-stringbuilder/0.0.1.tar.gz',
  keywords = ['string', 'building', 'concatenation'],
  install_requires = [],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.6',
  ],
  python_requires='>=3.6'
)