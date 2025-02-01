from setuptools import setup, find_packages
import os

def get_version():
    version_file = os.path.join(
        os.path.dirname(__file__), "pyscreenrecorder", "__version__.py"
    )
    with open(version_file, "r") as f:
        version_vars = {}
        exec(f.read(), version_vars)
    return version_vars["__version__"]


setup(
    name="pyscreenrecorder",
    version=get_version(),
    description="A Python package for screen recording with customizable resolution, FPS, and mouse tracking.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SSujitX/pyscreenrecorder",
    author="Sujit Biswas",
    author_email="ssujitxx@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "mss==10.0.0",
        "numpy==2.2.2",
        "opencv-python==4.11.0.86",
        "PyAutoGUI==0.9.54",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    keywords="screen recorder, screen capture, video recording, screen recording, recording, screenshots, mouse tracking, automated screen recording",
    project_urls={
        "Bug Tracker": "https://github.com/SSujitX/pyscreenrecorder/issues",
        "Documentation": "https://github.com/SSujitX/pyscreenrecorder#readme",
        "Source Code": "https://github.com/SSujitX/pyscreenrecorder",
    },
    python_requires=">=3.9",
)
