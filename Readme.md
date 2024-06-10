# Overview

This repository is for implementation in C++ using VSCode for participation in Atcoder.

This repository includes the following features by default

- Debugger
- Executable script files
- Sample code

## Requirements

- VSCode
- Docker Desktop for Windows(Mac)
- Dev Containers(VSCode Extension)

## Install

Execute the following command on VSCode.

```:bash
git clone https://github.com/itkmaingit/atcoder_for_cpp
```

In addition, execute the following commands in the palette on VSCode. (Ctrl+Shift+P)

`Dev Containers: Open Folder In Container...`

Open the `atcoder_for_cpp` folder with this command and wait for the Docker container to be built.

## Directory Structure

```:plaintext
root
|   .env
|   .gitignore
|   Readme.md
|
+---.devcontainer
    |   devcontainer.json
    |   docker-compose.yml
    |   Dockerfile  # config file for container, no editing allowed
    |
    \---works
        |   a.out
        |   debug
        |   run.sh
        |
        +---.vscode # Configuration file for debugging, no editing allowed
        |       c_cpp_properties.json
        |       launch.json
        |       settings.json
        |       tasks.json
        |
        +---problems
        |   |   .gitignore
        |   |
        |   \---[date]
        |           [difficulty].cpp # Actual solution cpp program
        |           [difficulty].in  # Input file
        |           [difficulty].out # Output file, you don't need to create
        |           [difficulty].res # Result file
        +---scripts
        |       rename.py # DON'T EDIT
        |       rename.sh # Execute before executing the program and the demon general.
        |       run.sh # Execution script without debugging.
        |
        \---sample_code # Template code commonly used in AtCoder

```

## Usage

You basically write the program in `works/problems/[date]/[difficulty]`.cpp. Name [date] the name of the contest, [difficulty] a.cpp if it is an A problem, and so on.

> ex.) works/problems/abc352/a.cpp
> ex.) works/problems/abc352/a.in
> ex.) works/problems/abc352/a.res

The [difficulty].txt file is automatically output and does not need to be created by you.

Before executing, run `sh scripts/rename.sh [date] [difficult]`. These will configure the debugger and other settings.

> ex) sh scripts/rename.sh abc352 a

It would not be a bad idea to register an alias for this command in bashrc.

### Excution(without debug)

Run `sh run.sh' and the results will be output to standard output and a file.

### Excution(with debug)

You can debug by opening the cpp program you want to debug and pressing F5. Set breakpoints as appropriate.
