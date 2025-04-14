from setuptools import setup, find_packages

setup(
    name="layered-py",
    version="1.0.0",  # Adjust the version appropriately
    description="A Python library for implementing layered architecture with services and dependency injection.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Malte Harms",
    author_email="mail@malteharms.dev",
    url="https://github.com/upNorthDev/layered-py",  # Replace with your repo URL
    packages=find_packages(exclude=["tests*", "*.tests"]),  # Finds all packages except test folders
    include_package_data=True,
    python_requires=">=3.7",  # Specify the minimum Python version
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "service=service:main",  # Allows running `service` from the command line.
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # Adjust license if needed
        "Operating System :: OS Independent",
    ],
    keywords="layered architecture, services, dependency injection, python",
    project_urls={
        "Bug Tracker": "https://github.com//layered-py/issues",  # Replace with issue tracker
        "Documentation": "https://github.com/upNorthDev/layered-py",  # Replace with your documentation URL
        "Source Code": "https://github.com/upNorthDev/layered-py",  # Replace with repo URL
    },
)
