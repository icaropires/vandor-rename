import pytest
import vandor_rename as vandor

valid_names = vandor.VALID_NAMES


@pytest.mark.parametrize("filee, expected", [("aula_test.brM3", True), ("fisico.sql", False), ("aula1exer2Evolucao3Consulta_AlunoSobrenome_15-0129815.sql", True)])
def test_is_renamed_exercise(filee, expected):
    """
    Should ensure the return value of is_renamed_exercise()
    """

    result = vandor.is_renamed_exercise(filee)
    assert expected == result


@pytest.mark.parametrize("filee, expected", [("logico.brM3", True), ("fisico.sql", True), ("uncorrect.pdf", False), ("controle.docx", False)])
def test_is_shortname_exercise(filee, expected):
    """
    Should ensure the type and return value of is_shortname_exercise()
    """

    result = vandor.is_shortname_exercise(filee)
    assert expected == result


@pytest.mark.parametrize("typee, expected", [("test", "Test"), ("doc", "DOC")])
def test_type_to_presentation_type(typee, expected):
    """
    Should ensure the type and return value of is_shortname_exercise()
    """

    result = vandor.type_to_presentation_type(typee)
    assert expected == result


def test_alert_ignored_files(capsys):
    """
    Ensures the alert_ignored_files() prints
    """

    expected = '''=============================
\tIgnored Files
=============================
The following files will be ignored because they don't look like exercises:
  1. cosulta.sql
  2. cotrole.sql
  3. fisco.sql
  4. aula1exer2Evolucao3Consulta_AlunoSobrenome_15\n'''

    vandor.alert_ignored_files(("cosulta.sql", "cotrole.sql", "fisco.sql", "aula1exer2Evolucao3Consulta_AlunoSobrenome_15"))
    result = capsys.readouterr()
    assert result.out == expected


def test_alert_renamings_to_be_applied(capsys):
    """
    Ensures alert_renamings_to_be_applied() prints
    """

    expected = '''======================================
\tRenamings to be applied:
======================================
1. test ----> testOne
\nTotal of renamings: 1\n'''

    vandor.alert_renamings_to_be_applied({"test": "testOne"})
    result = capsys.readouterr()
    assert result.out == expected


@pytest.mark.parametrize("renamings, expected", [({}, '''======================================
\tRenamings to be applied:
======================================
\nTotal of renamings: 0\n'''), ({"oneTest": "oneTest"}, '''======================================
\tRenamings to be applied:
======================================
  X. oneTest is already renamed!
\nTotal of renamings: 0\n''')])
def test_alert_renamings_to_be_applied_not_found(renamings, expected, capsys):
    """
    Ensures alert_renamings_to_be_applied() raises a FileNotFoundError
    """

    with pytest.raises(FileNotFoundError):
        vandor.alert_renamings_to_be_applied(renamings)

    result = capsys.readouterr()
    assert result.out == expected


# def test_confirm_operations():
#     pass
#
#
# def test_parse_files():
#     pass
#
#
# def test_zip_result():
#     pass
#
#
# def test_assemble_classname():
#     pass
#
#
# def test_get_new_name():
#     pass
#
#
# def test_validate_params():
#     pass
