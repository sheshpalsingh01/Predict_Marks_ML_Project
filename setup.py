# from setuptools import find_packages,setup
# from typing import List
# HYPEN_E_DOT='-e .'



# def get_requirements(file_path:str) ->list[str]:
    
#     '''
#     this  function will return the list of requirements
#     '''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines() #read line inside txt file
#         requirements = [req.replace("\n","") for req in requirements.txt]
        
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
            
            
#     return requirements
        
        

 
# setup(
# name='ml_project',
#     version='0.0.1',
#     author='sheshpal',
#     author_email="sheshpalsingh2024@gmail.com",
#     packages=find_packages(),
#     # install_requires =[ 'pandas','numpy','seaborn'],
#     install_requires =get_requirements('requirements.txt')
# )


from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    """
    requirements = []
    try:
        with open(file_path, "r") as file_obj:
            requirements = file_obj.readlines()  # Read all lines from the file
            requirements = [req.strip() for req in requirements]  # Remove newline characters
            
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)  # Remove '-e .' if present
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Using an empty list.")

    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='sheshpal',
    author_email="sheshpalsingh2024@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
