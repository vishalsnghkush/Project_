from setuptools import find_packages, setup
def Requiremnet(file_path):
    requirment=[]
    with open(file_path) as file:
        requirment =file.readlines()
        requirment =[req.replace("\n","") for req in requirment]
    return requirment
setup(
    name="Vishal Kushwaha",
    version='0.1',
    author='Vishal',
    author_email='vishalsnghkush31@gmail.com',
    long_description='Hello My First SetUp File',
    maintainer='Vishal',
    packages=find_packages(),
    install_requires=Requiremnet("requirements.txt")
    )