# cookiecutter-custom-pypackage

A customized, minimal [cookiecutter](https://github.com/audreyr/cookiecutter) template for Python packages, built off of the 
[cookiecutter-pypackage-minimal](https://github.com/kragniz/cookiecutter-pypackage-minimal) template.

Packaging in Python can be annoying so this hopes to save some time.

# Usage

```
pip install cookiecutter
git clone https://github.com/jakubd/cookiecutter-custom-pypackage.git
cookiecutter cookiecutter-custom-pypackage/
```

You should then change the classifiers in `{{ package_name }}/setup.py` - it is assumed that the project will run on the latest versions of Python 2 and 3, so you should remove any classifiers that do not apply. The full list of PyPI classifiers can be found [here](https://pypi.org/classifiers/).

# Features

Though overall this is minimal template some features that are set up which include:

* [pytest](https://docs.pytest.org/) as the default test runner.
* [tox](https://tox.readthedocs.io/) for testing Python version compatibility.
* [Dockerfile](https://www.docker.com/) generated for testing in a disposable environment.
* [setuptools](https://setuptools.readthedocs.io/) for packaging.
* [requirements.txt](https://pip.readthedocs.io/en/1.1/requirements.html) support as well for those that need that kind of thing.
* [travis-ci.org](https://travis-ci.org/) setup for CI integration.
* [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)
* [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) instead of RST for documentation..