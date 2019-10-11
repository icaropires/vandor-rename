import pytest
import vandor_rename as vandor 
from vandor_rename import os

valid_names = vandor.VALID_NAMES


def test_valid_names_and_exts():
    """
    Should ensure that all the names have their valid type
    """

    expected_result = [
        "('sql',)",
        "('brM3',)",
        "('pdf', 'doc', 'docx')"
    ]

    ext = [vandor._exts]

    for item in valid_names:
        assert str(valid_names[item]) in expected_result

    extensions = {
        'brM3',
        'doc',
        'pdf',
        'docx',
        'sql'
    }

    for extension in ext:
        assert extension == extensions


@pytest.mark.parametrize("input, expected_result", [("aula_test.brM3", True), ("fisico.sql", False)])
def test_is_renamed_exercise_false(input, expected_result):
    """
    Should ensure the return value of is_renamed_exercise()
    """

    result = vandor.is_renamed_exercise(input)
    assert expected_result == result


@pytest.mark.parametrize("input, expected_result", [("logico.brM3", True), ("fisico.sql", True)])
def test_is_shortname_exercise(input, expected_result):
    """
    Should ensure the type and return value of is_shortname_exercise()
    """

    result = vandor.is_shortname_exercise(input)
    assert expected_result == result


@pytest.mark.parametrize("input, expected_result", [("test", "Test"), ("doc", "DOC")])
def test_type_to_presentation_type(input, expected_result):
    """
    Should ensure the type and return value of is_shortname_exercise()
    """

    result = vandor.type_to_presentation_type(input)
    assert expected_result, result


def test_alert_ignored_files():
    """
    Ensures the alert_ignored_files() prints
    """
    
    assert vandor.alert_ignored_files(("A", 2, "C", 4)) == None


def test_alert_renamings_to_be_applied():
    """
    Ensures alert_renamings_to_be_applied() prints
    """
    file_list = {
        "oldName": "newName",
        "Star": "*",
        "test": "test"
    }
    
    assert vandor.alert_renamings_to_be_applied(file_list) == None


def test_no_alert_renamings_to_be_applied():
    """
    Ensures alert_renamings_to_be_applied() raises a FileNotFoundError
    """
    
    with pytest.raises(FileNotFoundError):
        vandor.alert_renamings_to_be_applied({})


def test_confirm_operations():
    pass


def test_parse_files():
    pass


def test_zip_result():
    pass


def test_assemble_classname():
    pass


def test_get_new_name():
    pass


def test_validate_params():
    pass
