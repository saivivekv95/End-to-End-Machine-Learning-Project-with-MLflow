import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
    
    
__version__ = "0.0.0"

REPO_NAME = "End-to-End-Machine-Learning-Project-with-MLflow"
AUTHOR_USER_NAME = "saivivekv"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "saivivekv95@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small pythong package for ml App",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)