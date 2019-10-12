# Vandor Rename

[![Build Status](https://travis-ci.com/icaropires/vandor-rename.svg?branch=master)](https://travis-ci.com/icaropires/vandor-rename)

Are you sick of renaming all the thousands of files of all the thousands of exercises assigned
by Professor Vandor every week? So am I! We can't change the format he likes but we can automate
the renaming! This is what this project is about.

## Features

* Support for renaming exercises already renamed and in short form
* Validation on params to avoid user mistakes
* Generates a new zip for all files which has the correct format name
* Visualization of operations performed
* Visualization of files that will be ignored
* Support auto capitalize type on filename
* Check if name conflicts will happen during the renaming
* Confirmation before apply the changes


## The Pattern

Vandor requests that all the the files should be in the following format:
`aulaXexerYEvolucaoZType_NameSurname_registrationnumber.extension`, respecting the case.

Where:
* `aula` means class and X is the the class number
* `exer` means exercise and Y is the exercise number
* `Evolucao` means evolution and Z is the evolution number (optional)
* `Type` is about what part of the exercise the file is, a script for
creating the database, etc. It can be: `Apaga`, `Consulta`, `Controle`,
`Fisico`, `Popula`, `Conceitual`, `Logico`, `DOC` (portuguese words)
* `NameSurname` is the student name
* `registration` number is your number on college, on the format: `nn-nnnnnnn`
* `extension` is the extension of the file

Example of filename: `aula10exer5Evolucao10Popula_AlunoAbobora_19-0000001.sql`.

## Installing

As this is just a script without dependencies, I didn't put it on PyPI and you can install it 
on Unix systems with just:

``` bash
sudo curl https://raw.githubusercontent.com/icaropires/vandor-rename/master/vandor_rename.py \
  -o /usr/local/bin/vandor-rename && sudo chmod a+x+r /usr/local/bin/vandor-rename
```

For updating your version, you can use the same command.

*note: Maybe would be better install it at `~/.local/bin` and without sudo. I've just put the
more general command which won't demand people modifying their PATH*

## Usage

Currently, the command **must be called on the same folder where your exercise files are**.
Your files can be in two formats: already renamed or the short form.

Already renamed means they already are on a valid format and you want to change just the
information ([Look here](https://github.com/icaropires/vandor-rename#the-pattern)).

The short form can be understood as just the `Type` (described before) of the file and the
case sould not make any difference. Examples: `consulta.sql`, `Consulta.sql`.

So, renaming your files accordingly:

``` bash
# vandor-rename [class_number] [exer_number] [evolution] [name] [registration_number]
$ vandor-rename 1 2 3 AlunoSobrenome 15-0129815
```

This will result in files like this: `aula1exer2Evolucao3Consulta_AlunoSobrenome_15-0129815.sql`.
Due to `[evolution]` be optional, you can pass it with value `-1` to ommit `EvolucaoZ` part.

Every time the application is called and there is exist some valid file on folder with correct names,
a zip will be created with these files, even if they weren't renamed now.


## How to contribute

All PRs and issues will are welcome.
For PRs, run `make pre-commit` and if there aren't any erros, your code is ready for review!
