#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = open('requirements.txt', 'r').read().split('\n')

setup(
    name='pctseng-inference-app',
    author="Po-Chuan(Gary) Tseng",
    author_email='pctseng7@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A model server flask app",
    install_requires=requirements,
    long_description='AI Backend Flask app',
    keywords='inference-app',
    packages=find_packages("src",exclude= ['test']),
    scripts=['serve'],
    include_package_data=True,
    package_dir={"": "src"},
    test_suite='tests',
    url='https://github.com/pctseng7/k8s-demo',
    version='0.0.1',
    zip_safe=False,
)
