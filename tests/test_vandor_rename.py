import pytest
import vandor_rename as vandor

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


@pytest.mark.parametrize("data, expected_result", [("aula_test.brM3", True), ("fisico.sql", False), ("aula1exer2Evolucao3Consulta_AlunoSobrenome_15-0129815.sql", True)])
def test_is_renamed_exercise(data, expected_result):
    """
    Should ensure the return value of is_renamed_exercise()
    """

    result = vandor.is_renamed_exercise(data)
    assert expected_result == result


@pytest.mark.parametrize("data, expected_result", [("logico.brM3", True), ("fisico.sql", True), ("uncorrect.pdf", False), ("controle.docx", False)])
def test_is_shortname_exercise(data, expected_result):
    """
    Should ensure the type and return value of is_shortname_exercise()
    """

    result = vandor.is_shortname_exercise(data)
    assert expected_result == result


@pytest.mark.parametrize("data, expected_result", [("test", "Test"), ("doc", "DOC")])
def test_type_to_presentation_type(data, expected_result):
    """
    Should ensure the type and return value of is_shortname_exercise()
    """

    result = vandor.type_to_presentation_type(data)
    assert expected_result == result


def test_alert_ignored_files(capsys):
    """
    Ensures the alert_ignored_files() prints
    """

    result_expected = '''=============================
\tIgnored Files
=============================
The following files will be ignored because they don't look like exercises:
  1. cosulta.sql
  2. controle.sql
  3. fisico.sql
  4. aula1exer2Evolucao3Consulta_AlunoSobrenome_15\n'''

    vandor.alert_ignored_files(("cosulta.sql", "controle.sql", "fisico.sql", "aula1exer2Evolucao3Consulta_AlunoSobrenome_15"))
    result = capsys.readouterr()
    assert result.out == result_expected


def test_alert_renamings_to_be_applied(capsys):
    """
    Ensures alert_renamings_to_be_applied() prints
    """

    expected_result = '''======================================
\tRenamings to be applied:
======================================
1. test ----> testOne
\nTotal of renamings: 1\n'''

    vandor.alert_renamings_to_be_applied({"test": "testOne"})
    result = capsys.readouterr()
    assert result.out == expected_result


@pytest.mark.parametrize("data, expected_result", [({}, '''======================================
\tRenamings to be applied:
======================================
\nTotal of renamings: 0\n'''), ({"oneTest": "oneTest"}, '''======================================
\tRenamings to be applied:
======================================
  X. oneTest is already renamed!
\nTotal of renamings: 0\n''')])
def test_alert_renamings_to_be_applied_NONE(data, expected_result, capsys):
    """
    Ensures alert_renamings_to_be_applied() raises a FileNotFoundError
    """

    with pytest.raises(FileNotFoundError):
        vandor.alert_renamings_to_be_applied(data)

    result = capsys.readouterr()
    assert result.out == expected_result



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
