from setuptools import setup, find_packages
import sky_thumbnails

setup(
    name='django-sky-thumbnails',
    version=".".join(map(str, sky_thumbnails.VERSION)),
    packages = find_packages(),
    install_requires=[
        'cropresize==0.1.6'
    ],

    author = 'Concentric Sky',
    author_email = 'django@concentricsky.com',
    description = 'Concentric Sky\'s thumbnailing model',
)
