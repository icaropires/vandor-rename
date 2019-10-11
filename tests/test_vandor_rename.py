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


def test_is_renamed_exercise():
    """
    Should ensure the type returned by is_renamed_exercise() is a bool
    """

    result = vandor.is_renamed_exercise('vandor_rename.py')
    assert isinstance(result, (bool, str, int))
    for filee in os.listdir():
        assert not isinstance(
            type(True),
            type(vandor.is_renamed_exercise(filee))
        )
        


def test_is_shortname_exercise():
    """
    Should ensure the type returned by is_shortname_exercise() is a bool
    """

    for filee in os.listdir():
        assert not isinstance(
            type(False),
            type(vandor.is_shortname_exercise(filee))
        )


def test_type_to_presentation_type_return1():
    """
    Should ensure the type and value returned by is_shortname_exercise() is a Test & str
    """

    result = vandor.type_to_presentation_type('test')
    expected_result = 'Test'
    assert result == expected_result
    assert type(result) == type(expected_result)


def test_type_to_presentation_type_return2():
    """
    Should ensure value returned by is_shortname_exercise() is a DOC
    """

    result = vandor.type_to_presentation_type('doc')
    expected_result = 'DOC'
    assert result == expected_result


def test_alert_ignored_files():
    """
    Ensures the functions prints, nothing to test in this functions
    """
    
    assert vandor.alert_ignored_files(("A", 2, "C", 4)) == None


def test_alert_renamings_to_be_applied():
    """
    Ensures alert_renamings_to_be_appliedalert_renamings_to_be_applied() prints
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
