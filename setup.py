"""Setup script."""

import os
from setuptools import setup

if __name__ == '__main__':
    print(
        'Sopel does not correctly load plugins installed with setup.py '
        'directly. Please use "pip install .", or add '
        f'{os.path.dirname(os.path.abspath(__file__))}/sopel_dum_e to '
        'core.extra in your config.'
    )

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    long_description=readme,
    long_description_content_type='text/markdown'
)
