from setuptools import setup, find_packages

with open('README.MD', 'r') as f:
    readme = f.read()
    
with open('LICENSE.MD', 'r') as f:
    license = f.read()
    
setup(
    name='fbmodules',
    version='0.0.1',
    description='Just a simple set of modules ',
    long_description=readme,
    long_description_content_type='text/markdown',
    package_dir={'': 'fbmodules'},
    packages=find_packages(where='fbmodules'),
    author='Timot',
    author_email='',
    url='https://github.com/timotofcourse/fb-modules',
    license=license,
    classiifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        ],
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['ruamel.yaml', 'shutil', 'ctypes', 'winotify'],
    extras_require={
        'dev': ['twine'],
    },
    python_requires='>=3.10'
)