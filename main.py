import os
import json
import subprocess

def load_config():
    with open('config/config.json', 'r') as file:
        config = json.load(file)
    return config

def run_script(language, script_name):
    try:
        print(f"Running script: {script_name}")
        if language == 'python':
            subprocess.run(['python', script_name])
        elif language == 'cpp':
            subprocess.run(['g++', script_name, '-o', 'output', '&&', './output'])
        elif language == 'javascript':
            subprocess.run(['node', script_name])
        elif language == 'go':
            subprocess.run(['go', 'run', script_name])
    except Exception as e:
        print(f"Error running the script: {e}")

def main():
    config = load_config()

    # Przykład uruchamiania skryptu AES w Pythonie
    run_script('python', f"encryption/python/{config['encryption']['python']}")

    # Przykład uruchamiania skryptu OAuth2 w Javie
    run_script('java', f"access_control/java/{config['access_control']['java']}")

    # Przykład uruchamiania detekcji zagrożeń w Pythonie
    run_script('python', f"threat_detection/python/{config['threat_detection']['python']}")

if __name__ == '__main__':
    main()
