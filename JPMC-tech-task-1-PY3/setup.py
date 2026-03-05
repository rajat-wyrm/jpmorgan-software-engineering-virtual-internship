from setuptools import setup, find_packages

setup(
    name="jpmc-task1-stock-feed",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.0',
        'pandas>=1.2.0',
        'websocket-client>=0.58.0',
    ],
    author="Rajat",
    description="JPMorgan Chase Virtual Internship - Task 1",
    python_requires='>=3.8',
)
