from setuptools import setup

setup(
    name='HAP-python-AM2302',
    description='HAP-python AsyncAccessory for the AM2302/DHT22 sensor.',
    author='Ivan Kalchev',
    version='0.9',
    url='https://github.com/ikalchev/HAP-python-AM2302',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Operating System :: Linux',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
    ],
    license='Apache-2.0',
    packages=[
        'pyhap.accessories.AM2302',
    ],
    install_requires=[
        'HAP-python',
        'pigpio',
    ],
)