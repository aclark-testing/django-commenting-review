from setuptools import find_packages
from setuptools import setup


setup(
    entry_points={
    },
    include_package_data=True,
    install_requires=[
        'Django',
        'django-contrib-comments',
        'django-threadedcomments',
        'django-comments-xtd',
        'django-fluent-comments',
    ],
    name='django-commenting-review',
    namespace_packages=[
    ],
    packages=find_packages(),
)
