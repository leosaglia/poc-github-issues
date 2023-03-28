import yaml
import os

# get the input and convert it to int

def read_and_modify_one_block_of_yaml_data():
    marks = os.environ.get("INPUT_MARKS")
    ambiente = os.environ.get("INPUT_AMBIENTE")

    novo_comando = 'python -m pytest -M "{0}" -E {1} --junitxml=relatorio.xml || true'.format(marks, ambiente.lower())

    yaml_data = None

    with open(f'tests/teste.yaml', 'r') as f:
        yaml_data = yaml.safe_load(f)

    with open(f'tests/teste.yaml', 'w') as file:
        yaml_data["phases"]["build"]["commands"][-1] = novo_comando 
        yaml.dump(yaml_data,file, sort_keys=False)

read_and_modify_one_block_of_yaml_data()
