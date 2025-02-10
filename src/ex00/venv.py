#!/usr/bin/env python3
import os


def show_venv_path():
    print(f"Your current virtual env is {os.environ.get('VIRTUAL_ENV')}")


if __name__ == '__main__':
    show_venv_path()
