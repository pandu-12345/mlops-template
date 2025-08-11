from setuptools import setup, find_packages

setup(
    name="project_name",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "torch",
        "flask",
        "mlflow",
    ],
    entry_points={
        "console_scripts": [
            "mlops-cli=mlops_template.cli:main",  # Replace with your actual CLI entry point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
