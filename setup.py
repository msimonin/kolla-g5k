from setuptools import setup, find_packages
from ham import __version__

setup(
    name='ham',
    version=__version__,
    license='GPL-3.0',
    packages=find_packages(),
    install_requires=[
        'Jinja2==2.8',
        'execo==2.5.4',
        'ansible==2.1.2',
        'docopt==0.6.2',
        'requests==2.11.0',
        'httplib2==0.9.2',
        'python-cinderclient==1.8.0',
        'python-dateutil==2.2',
        'python-glanceclient==2.3.0',
        'python-keystoneclient==3.4.0',
        'python-neutronclient==5.1.0',
        'python-novaclient==5.0.0',
        'python-openstackclient==2.6.0'
    ],
    entry_points={'console_scripts': ['ham = ham.ham:main']}
)
