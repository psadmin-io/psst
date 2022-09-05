from setuptools import setup, find_packages
from pathlib import Path

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text()

setup_args = dict(
    name='psst',
    version='0.0.1',
    description='psst',
    long_description_content_type="text/markdown",
    long_description=README,
    url='https://github.com/psadmin-io/psst',    
    author='psadmin.io',
    author_email='info@psadmin.io',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    packages=find_packages(),
    keywords=['PeopleSoft', 'PeopleTools', 'OCI', 'Oracle Cloud Infrastructure', 'Oracle Cloud'],    
    include_package_data=True,
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "psst=psst.psst:cli",
        ]
    },
)

if __name__ == '__main__':
    setup(**setup_args) 