from setuptools import setup, find_packages

with open('README.MD', 'r') as f:
    readme = f.read()
    
with open('LICENSE.MD', 'r') as f:
    license = f.read()
    
setup(
    name='fb-modules',
    version='0.0.1',
    description='Just a simple set of modules ',
    long_description=readme,
    package_dir={'': 'fbmodules'},
    packages=find_packages(where='fb-modules'),
    author='Timot',
    author_email='',
    url='https://github.com/timotofcourse/fb-modules',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)