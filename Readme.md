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
    |   Dockerfile  # config file for container, DON'T EDIT.
    |
    \---works
        |   Makefile # Makefile to initialize the issue and execute commands
        |
        +---.vscode # Configuration file for debugging, DON'T EDIT.
        |       c_cpp_properties.json
        |       launch.json
        |       settings.json
        |       tasks.json
        |
        +---problems
        |   |   .gitignore
        |   |
        |   \---[date]
        |           [difficulty].cpp # Actual solution cpp program, created by makefile
        |           [difficulty].in  # Input file, created by makefile
        |           [difficulty].res # Result file, created by makefile
        |           [difficulty].txt # Output file, you don't need to create
        +---scripts
        |       rename.py # DON'T EDIT
        |
        |
        \---sample_code # Template code commonly used in AtCoder

```

## Usage

You basically write the program in `works/problems/[date]/[difficulty]`.cpp. Name [date] the name of the contest, [difficulty] a.cpp if it is an A problem, and so on.

To do so you should execute the following make command Be sure to go through this command as it also configures the settings for later debugging. These files are created by the following make command, and you only need to edit them.

```bash
make init date=[date] diff=[difficulty]
```

It would not be a bad idea to register an alias for this command in bashrc.

### Excution(without debug)

All you have to do is execute the following command.

```bash
make run date=[date] diff=[difficulty]
```

### Excution(with debug)

You can debug by opening the cpp program you want to debug and pressing F5. Set breakpoints as appropriate.
