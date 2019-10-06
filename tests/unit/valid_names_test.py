import vandor-rename as vandor


def test_valid_names_and_exts():
    """
    Should ensure that all the names have their valid type
    """
    valid_names = vandor.VALID_NAMES

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
