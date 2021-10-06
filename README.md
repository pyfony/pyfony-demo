# Pyfony demo project

## Cloning project from repository

```
git clone https://github.com/pyfony/pyfony-demo.git
```

## Initialize local environment 

Now run `./env-init.sh` which will initialize your local environment.

**Activate the environment**

Now activate the Conda environment for your new project

```bash
$ conda activate $PWD/.venv
```

or use a shortcut

```bash
$ ca
```

## Running hello world script

Run `python src/pyfonydemo/hello_world.py` to see "Hello world" printed on the screen.

## Running hello world command

Run `console pyfonydemo:say-hello` to see "Hello world" printed on the screen using a standard console logger.
