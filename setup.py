"""Python package description."""
from setuptools import setup, find_packages


def readme():
    """Load the readme file."""
    with open('README.md', 'r') as readme_file:
        return readme_file.read()


setup(
    name='miflora-mqtt',
    version='0.1',
    description='Simple MQTT bridge to publish data from Mi Flora sensor',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/yolkhovyy/miflora',
    author='Yuriy Olkhovyy',
    author_email='y.olkhovyy@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),
    keywords='plant sensor bluetooth low-energy ble',
    zip_safe=False,
    install_requires=['btlewrap', 'getmac', 'gatttool', 'paho-mqtt'],
    include_package_data=True,
)
