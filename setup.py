from setuptools import setup, find_packages
import sky_thumbnails

setup(
    name='django-sky-thumbnails',
    version=".".join(map(str, sky_thumbnails.VERSION)),
    packages = find_packages(),
    install_requires=[
        'PILLOW==1.7.7'
    ],

    author = 'Concentric Sky',
    author_email = 'django@concentricsky.com',
    description = 'Concentric Sky\'s thumbnailing model',
)
