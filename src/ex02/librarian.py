#!/usr/bin/env python3
import os
import sys
import subprocess


def check_the_venv():

    try:
        if (os.path.basename(os.environ.get('VIRTUAL_ENV')) != "shirledo"):
            raise EnvironmentError(
                "this script have wrong venv (not shirledo)")
    except:
        raise EnvironmentError("You are not in a viral environment.")


def install_libraries():
    # subprocess.run(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'])
    if (subprocess.check_call(['python3', '-m', 'pip', 'install', '-r', 'requirements.txt'])):
        raise ValueError("Something went wrong")


def show_libs():
    result = subprocess.run(['python3', '-m', 'pip', 'freeze'],
                            capture_output=True, text=True, check=True).stdout
    print(
        f"\ninstalled libs :\n{result}")
    with open('requirements.txt', 'w') as f:
        f.write(result)


def archive_environment():
    env_path = os.path.dirname(os.path.dirname(sys.executable))
    env_name = os.path.basename(env_path)
    archive_name = f"{env_name}.tar.gz"
    subprocess.run(['tar', '-czf', archive_name, '-C',
                   os.path.dirname(env_path), env_name])
    print(f"The venv is archived in {os.path.dirname(env_path)}")


def unpack_archive():
    archive_name = "shirledo.tar.gz"
    subprocess.run(['tar', '-xzf', archive_name])
    print(f"The venv is unpacked in {os.getcwd()}")


if __name__ == '__main__':
    try:
        check_the_venv()
        install_libraries()
        show_libs()
        archive_environment()
    except Exception as e:
        print(
            f"you have launched the program with an error : {e}\nTrying to unpack the archive with the environment")
        try:
            unpack_archive()
        except Exception as ee:
            print(f"unpacking failed with error:{ee}")
