try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Learn python the hard way exercise 48',
    'author': 'Usmaan Ali',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'usmaanalii@hotmail.co.uk',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
