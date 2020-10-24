from setuptools import setup, find_packages
from whitediver.NewInstall import NewInstall

setup(
    name="servo-control",
    version='0.0.2',
    maintainer='Serge Arbuzov',
    author_email='info@whitediver.com',
    maintainer_email='info@whitediver.com',
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "servo-control=whitediver:main"
        ]
    },
    data_files=[
        (
            '/lib/systemd/system',
            ['config/servo-control.service']
        )
    ],
    install_requires=[
        'adafruit-pca9685'
    ],
    cmdclass={'install': NewInstall},
    python_requires='>=3.5.1'
)