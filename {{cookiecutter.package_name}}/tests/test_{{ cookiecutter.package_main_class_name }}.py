from {{ cookiecutter.package_name }} import {{ cookiecutter.package_main_class_name }}

def test_pass():
    assert True, "dummy sample test"

def test_init():
    s = {{ cookiecutter.package_main_class_name }}()
    assert s
