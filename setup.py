from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns
    a list of dependencies, excluding any unnecessary symbols.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        # Remove '-e .' if it exists in the requirements
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='your_project_name',
    version='0.0.1',
    author='Your Name',
    author_email='your_email@example.com',
    description='A short description of your project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Dynamically get dependencies
)
