from setuptools import setup, find_namespace_packages

setup(
    name="hello_py",
    version="0.0.1",
    python_requires='>=3',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src')
)
