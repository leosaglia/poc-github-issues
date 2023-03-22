import yaml
import os

# get the input and convert it to int

def read_and_modify_one_block_of_yaml_data():
    marks = os.environ.get("INPUT_MARKS")
    ambiente = os.environ.get("INPUT_AMBIENTE")

    novo_comando = f'        
      - echo "Executando os testes no ambiente de DEV"
      - cd tests/integrations
      - python -m pytest -M "{marks}" -E {ambiente.lower()} --junitxml=relatorio.xml || true
    '

    with open(f'teste.yaml', 'r+') as f:
        data = yaml.safe_load(f)
        data["phases"]["build"]["commands"] = novo_comando 
        yaml.dump(data,f,sort_keys=False)
        print(data) 
    print('done!')

read_and_modify_one_block_of_yaml_data()
