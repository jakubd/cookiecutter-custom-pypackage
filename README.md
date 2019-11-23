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
