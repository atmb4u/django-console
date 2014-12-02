from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-console',
    description='bash console in the browser for django admins',
    keywords='django, bash',
    packages=find_packages(),
    include_package_data=True,
    version="0.4.7",
    author="Anoop Thomas Mathew",
    author_email="atmb4u@gmail.com",
    url='http://github.com/atmb4u/django-console',
    classifiers=['Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Web Console',
    'Topic :: Internet :: WWW/HTTP :: WSGI',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license="BSD License",
    platforms=["all"],
    zip_safe=False
)