from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Reads the requirements.txt file and returns a list of dependencies."""
    requirements_list = []
    try:
        with open("requirements.txt", "r") as file:
            requirements = file.readlines()
            for requirement in requirements:
                requirement = requirement.strip()
                # Ignore blank lines and '-e .' entries
                if requirement and not requirement.startswith("-e"):
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")
    return requirements_list

setup(
    name="ai_trip_planner",
    version="0.0.1",
    author="Ammar Vohra",
    author_email="ammarvohra92@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
