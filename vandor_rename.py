#!/usr/bin/env python3

import os
import re
from zipfile import ZipFile
from sys import argv
from collections import defaultdict
from typing import Dict, List, Optional, Tuple


# type to extensions
VALID_NAMES = {
    "apaga": ("sql",),
    "consulta": ("sql",),
    "controle": ("sql",),
    "fisico": ("sql",),
    "popula": ("sql",),
    "conceitual": ("brM3",),
    "logico": ("brM3",),
    "doc": ("pdf", "doc", "docx"),
}


_exts = set(ext for exts in VALID_NAMES.values() for ext in exts)


# Renamed exercise is like: class_type_name_registrationnumber.ext
def is_renamed_exercise(filee: str) -> bool:
    return any((filee.endswith(ext)) for ext in _exts) and filee.startswith(
        "aula"
    )


# Shortname exercise is like: consulta.sql
def is_shortname_exercise(filee: str) -> bool:
    # Just some iterations
    short_names = (
        f"{n}.{ext}" for n, _exts in VALID_NAMES.items() for ext in _exts
    )

    return filee in short_names


def type_to_presentation_type(typee: str) -> str:
    if typee.lower() != "doc":
        return typee[0].upper() + typee[1:]
    return "DOC"


def alert_ignored_files(ignored_files: List[str]) -> None:
    print(
        "=============================\n"
        "\tIgnored Files\n"
        "============================="
    )
    ignored_files = "\n".join(
        f"  {i+1}. {f}" for i, f in enumerate(ignored_files)
    )
    print(
        "The following files will be ignored because they don't"
        f" look like exercises:\n{ignored_files}"
    )


def alert_renamings_to_be_applied(renamings: Dict[str, str]) -> None:
    print(
        "======================================\n"
        "\tRenamings to be applied:\n"
        "======================================"
    )
    total_renamings = 0
    for old_name, new_name in renamings.items():
        if old_name != new_name:
            total_renamings += 1
            print(f"{total_renamings}. {old_name} ----> {new_name}")
        else:
            print(f"  X. {old_name} is already renamed!")
    print(f"\nTotal of renamings: {total_renamings}")

    if not total_renamings:
        raise FileNotFoundError("No renamings to be applied")


def confirm_operations(
    renamings: Dict[str, str], ignored_files: List[str]
) -> None:
    alert_ignored_files(ignored_files)
    print()
    alert_renamings_to_be_applied(renamings)

    try:
        input("\nLooks good? ENTER to confirm or CTRL-C to cancel")
    except KeyboardInterrupt:
        print("\n\nRenaming cancelled! No files were touched!")
        exit(0)


def rename_files(renamings: Dict[str, str]) -> None:
    for old_name, new_name in renamings.items():
        os.rename(old_name, new_name)

    print(f"\nFinished! Renamings applied!")


def parse_files(all_files: List[str]) -> Tuple[Dict[str, str], List[str]]:
    def get_renamed_type(filename: str) -> str:
        typee = f.split("_")[0]

        for i, c in enumerate(reversed(typee)):
            index = len(typee) - i - 1
            if c.isupper() and typee[index - 1].islower():
                typee = typee[index:]
                break

        return typee

    renamings = defaultdict(lambda: "")
    renamings_reversed = defaultdict(lambda: "")
    ignored_files = []

    for f in all_files:
        if not renamings[f]:  # Sanity check
            new_name = ""
            if is_renamed_exercise(f):
                typee = get_renamed_type(f)
                typee = type_to_presentation_type(typee)
                new_name = get_new_name(typee)
            elif is_shortname_exercise(f):
                typee, ext = f.split(".")
                typee = type_to_presentation_type(typee)
                new_name = get_new_name(typee, ext)
            else:
                ignored_files.append(f)
                continue

            renamings[f] = new_name
            renamings_reversed[new_name] = f
        else:
            raise ValueError(
                f"'{new_name}' can be generated by '{f}'"
                f" and '{renamings_reversed[f]}'!"
                " No files will be renamed!"
            )

    renamings = {k: v for k, v in renamings.items() if v}
    return renamings, ignored_files


def zip_result(name: str, renamings: Dict[str, str]) -> None:
    if len(renamings):
        try:
            os.remove(name)
        except FileNotFoundError:
            pass

        with ZipFile(name, "w") as z:
            for _, f in renamings.items():
                z.write(f)
        print("=> New zip generated to:", name)
    else:
        print("No files to be zipped!")


def beg() -> None:
    print(
        "Cool application? Please give a star on Github:"
        " https://github.com/icaropires/vandor-rename !"
    )


if __name__ == "__main__":

    if len(argv) < 6:
        print(
            "Usage example: vandor-rename"
            " [class_number] [exer_number] [evolution]"
            " [name] [registration_number]"
            "\nExample: vandor-rename 1 2 3 AlunoSobrenome 15-0129815"
        )
        exit(0)

    _, class_n, exer_n, evolution, name, registration_number, *_ = argv

    def assemble_classname() -> str:
        class_name = f"aula{class_n}exer{exer_n}"

        if evolution != "-1":
            class_name += "Evolucao" + evolution

        return class_name

    def get_new_name(typee: str, ext: Optional[str] = None) -> str:
        new_name = "_".join(
            (assemble_classname() + typee, name, registration_number)
        )
        ext = ext or VALID_NAMES[typee.lower()][0]

        return f"{new_name}.{ext}"

    def validate_params() -> None:
        message = ""
        param = ""
        name_pat = r"([A-ZÁÉÍÓÚÀÂÊÔÃÕÇ]{1}[a-záéíóúàâêôãõç]+){2}"
        registration_pat = r"1[0-9]-0[01][0-9]{5}"

        if int(class_n) <= 0:
            param = "class_n"
            message = "'class_n' must be greater than 0"
        elif int(exer_n) <= 0:
            param = "exer_n"
            message = "'exer_n' must be greater than 0"
        elif evolution != "Oracle" and evolution != "-1":
            param = "evolution_n"
            if int(evolution) <= 0:
                message = "'evolution' must be greater than 0 or 'Oracle'"
        elif re.fullmatch(name_pat, name) is None:
            param = "name"
            message = "'student_name' must be like: 'NameSurname'"
        elif re.fullmatch(registration_pat, registration_number) is None:
            param = "registration_number"
            message = (
                "'registration_number' must be like: 15-0129815"
                " and look like real registrations numbers"
            )

        if message:
            raise ValueError(f"Invalid [{param}]! {message}")

    validate_params()

    all_files = os.listdir()
    renamings, ignored_files = parse_files(all_files)

    try:
        confirm_operations(renamings, ignored_files)
        rename_files(renamings)
    except FileNotFoundError:
        print("No renamings to be applied!")

    name = f"{assemble_classname()}_{name}_{registration_number}.zip"
    zip_result(name, renamings)

    beg()
