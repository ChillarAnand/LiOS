"""
Auto sync photos/videos/music/files between iOS & Linux.
"""
from setuptools import find_packages, setup

dependencies = ['click']

setup(
    name='lios',
    version='0.1.0',
    url='https://github.com/chillaranand/lios',
    license='BSD',
    author='anand reddy pandikunta',
    author_email='anand21nanda@gmail.com',
    description='Auto sync photos/videos/music/files between iOS & Linux.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'lios = lios.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
