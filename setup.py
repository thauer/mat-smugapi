from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='matsmug',
    version='0.0.1',
    description='API for smugmug.com',
    long_description=readme,
    author='Tamás Hauer',
    author_email='tamas@hauers.net',
    url='https://github.com/thauer/matsmug',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)