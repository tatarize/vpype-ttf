from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

setup(
    name="vpype-ttf",
    version="0.0.1",
    description="vpype ttf plugin",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tatarize",
    author_email="tatarize@gmail.com",
    url="https://github.com/tatarize/vpype-ttf/",
    packages=["vpype_ttf"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "click",
        "vpype>=1.9,<2.0",
        "numpy",
        "freetype-py",
    ],
    entry_points="""
            [vpype.plugins]
            render=vpype_ttf.font:render
        """,
)