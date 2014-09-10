"""
Flask-Blitzdb
-------------

This is an extension for the Blitzdb file based NoSQL database platforms


"""
from setuptools import setup


setup(
    name='flask-blitzdb',
    version='0.1',
    url='https://github.com/puredistortion/flask-blitzdb',
    license='',
    author='Dale Stirling',
    author_email='feedback@puredistortion.com',
    description='Flask extension for blitzdb',
    long_description=__doc__,
    py_modules=['flask_blitzdb'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'blitzdb'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware'
    ]
)