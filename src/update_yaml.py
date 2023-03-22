import yaml
import os

# get the input and convert it to int

def read_and_modify_one_block_of_yaml_data():
    marks = os.environ.get("INPUT_MARKS")
    ambiente = os.environ.get("INPUT_AMBIENTE")

    novo_comando = f'python -m pytest -M "{marks}" -E {ambiente.lower()} --junitxml=relatorio.xml || true'

    yaml_data = None

    with open(f'teste.yaml', 'r') as f:
        yaml_data = yaml.safe_load(f)

    with open(f'teste.yaml', 'w') as f:
        yaml_data["phases"]["build"]["commands"][-1] = novo_comando 
        yaml.dump(yaml_data,f,sort_keys=False)

read_and_modify_one_block_of_yaml_data()
