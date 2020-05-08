from setuptools import find_namespace_packages, setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='sr.comp.scorer',
    version='1.1.0',
    packages=find_namespace_packages(),
    namespace_packages=['sr', 'sr.comp'],
    description="Student Robotics Competition Score Entry Application",
    long_description=long_description,
    include_package_data=True,
    zip_safe=False,
    author="Student Robotics Competition Software SIG",
    author_email="srobo-devel@googlegroups.com",
    install_requires=[
        'PyYAML >=3.11, <5',
        'six >=1.8, <2',
        'Flask >=1.0, <2',
        'sr.comp >=1.2, <2',
    ],
    python_requires='>=3.5',
    setup_requires=[
        'Sphinx >=1.3, <2',
    ],
    classifiers=[
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
)
