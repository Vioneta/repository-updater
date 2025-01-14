"Vioneta Agro add-ons repository updater setup."
from setuptools import find_packages, setup

from repositoryupdater import APP_DESCRIPTION, APP_NAME, APP_VERSION

setup(
    name=APP_NAME,
    version=APP_VERSION,
    author="Vioneta",
    author_email="admin@vioneta.com",
    description=APP_DESCRIPTION.split("\n")[0],
    long_description=APP_DESCRIPTION,
    license="MIT",
    url="https://github.com/Vioneta/repository-updater",
    keywords=[
        "addons",
        "repository",
        "add-ons",
        "vioneta",
    ],
    platforms="any",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    install_requires=[
        "click==8.1.7",
        "crayons==0.4.0",
        "emoji==2.14.0",
        "GitPython==3.1.43",
        "Jinja2==3.1.4",
        "PyGithub==2.4.0",
        "python-dateutil==2.9.0.post0",
        "PyYAML==6.0.2",
        "semver==3.0.2",
    ],
    entry_points="""
        [console_scripts]
            repository-updater=repositoryupdater.cli:repository_updater
            repository-updater-git-askpass=repositoryupdater.cli:git_askpass
    """,
)
