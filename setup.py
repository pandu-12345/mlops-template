from setuptools import setup, find_packages

setup(
    name="project_name",                      # Your package name
    version="0.1.0",                        # Version (semantic versioning)
    description="MLOps project template",   # Optional: Short description
    author="Your Name",                     # Optional
    package_dir={"": "src"},                # Tell setuptools that packages live in `src/`
    packages=find_packages(where="src"),   # Finds all packages under `src/`
    python_requires=">=3.8",               # Optional: Enforce minimum Python version
)