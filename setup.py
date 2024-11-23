from setuptools import setup, find_packages

setup(
    name="design-language",  
    version="0.1.0", 
    description="A simple design-focused programming language for designers and developers.",  
    long_description=open("README.md").read(), 
    long_description_content_type="text/markdown",  
    author="Your Name",  
    author_email="your.email@example.com",  
    url="https://github.com/yourusername/design-language", 
    packages=find_packages(where="src"), 
    package_dir={"": "src"},  
    python_requires=">=3.6", 
    install_requires=[
       
    ],
    extras_require={
        "dev": ["pytest", "flake8"], 
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "design-language=parser:main",  
        ],
    },
    include_package_data=True,  
    license="MIT",  
)
