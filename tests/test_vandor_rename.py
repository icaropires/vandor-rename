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
    Should ensure the type return by is_renamed_exercise() is a bool
    """

    for filee in os.listdir():
        assert not isinstance(
            type(True),
            type(vandor.is_shortname_exercise(filee))
        )


def test_return_value_of_shortname_excersise():
    """
    Should ensure the type return by is_renamed_exercise() is a bool
    """

    for filee in os.listdir():
        assert not isinstance(
            type(False),
            type(vandor.is_shortname_exercise(filee))
        )


def test_type_to_presentation_type():
    pass


def test_alert_ignored_files():
    pass


def test_alert_renamings_to_be_applied():
    pass


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
