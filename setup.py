# from setuptools import find_packages, setup
# from typing import List
# HYPEN_E_DOT ='-e .'
# def get_requirements(file_path:str)->List[str]:
#   '''This function read the requirements file and retuen the list of requirements'''
#   requirements=[]
#   with open(file_path) as file_obj:
#     requirements=file_obj.readlines()
#     requirements=[req.replace("\n","") for req in requirements]
    
#     if HYPEN_E_DOT in requirements:
#       requirements.remove(HYPEN_E_DOT)
      
#   return requirements

# setup(
#    name ='MLproject',
#    version='0.0.1',
#    packages=find_packages(),
#    author='Rajesh kumar',
#    author_email='rajesh8368568776@gmail.com',
#    license='MIT',
#    packages=find_packages(),
#   #  install_requires=[
#   #    'numpy',
#   #    'pandas',
#   #    'seaborn'
#   #  ]
#   install_requires=get_requirements('requirements.txt')
  
   
# )
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function reads the requirements file and returns the list of requirements."""
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Using .strip() instead of .replace("\n", "")

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Rajesh Kumar',
    author_email='rajesh8368568776@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
