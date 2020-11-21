from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = ["python-dotenv==0.15.0", "requests==2.25.0"]

dev_requirements = ["black==20.8b1", "pylint==2.6.0"]

setup(
    name="threedify-sfm",
    version="0.0.1",
    author="Anish Silwal Khatri",
    author_email="silwalanish@gmail.com",
    description="A small SfM pipeline",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Threedify/Threedify-SfM",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"": ["data/*.*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
)
