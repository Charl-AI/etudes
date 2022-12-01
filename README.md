# aoc

Advent of code challenges in languages I don't know. For 2022, we are learning Rust.

## Rust Basics

Create a project for each challenge:

```bash
cargo new aoc-2022-XX
```

To build (compile) a project, `cd` into it, then run:

```bash
cargo build
```

Finally, run the code with

```bash
cargo run
```

## Installation

This project includes a `.devcontainer` directory, which enables use of GitHub Codespaces. You can open this repo **without any local installation** in a cloud-hosted 'codespace'. The dependencies will be automatically installed on the remote cloud machine, which you can access through your browser, VSCode, or even PyCharm. Simply start the codespace using the button in the GitHub UI. This is the easiest way to get a working development environment for this project.

For installing locally, you have three options: Docker, VSCode devcontainer, or manual install.

### Option 1: Docker

First, build the image:

```bash
docker build -f .devcontainer/Dockerfile . -t aoc
```

Running the container will give you an interactive bash shell which you can use to run any of the projects.

```bash
docker run --rm -it aoc
```

### Option 2: VSCode devcontainer

If you use VSCode with the remote containers extension, you can install the dependencies and open a VSCode development environment for this project by simply running `Remote Containers: Open folder in Container` from the command palette. You can then run any project you want from the integrated terminal.

### Option 3: Manual install

If you don't want to use Docker, you can install Rust manually, using [Rustup](https://doc.rust-lang.org/book/ch01-01-installation.html).
