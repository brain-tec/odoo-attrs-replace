from setuptools import setup

setup(
    name='odoo_attrs_replace',
    version='0.1',
    py_modules=['replace_attrs'],
    install_requires=[
        'beautifulsoup4',
        'lxml'
    ],
    entry_points={
        'console_scripts': [
            'replace_attrs=replace_attrs:main',
        ],
    },
)
