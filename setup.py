from setuptools import setup, find_packages

setup(
    name="linear_regression",
    version="0.1.0",
    description="A simple linear regression module with gradient descent",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    python_requires=">=3.6",
)
