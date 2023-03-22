import yaml
import os

# get the input and convert it to int

def read_and_modify_one_block_of_yaml_data(filename='teste', key='["execucao"]["mensagem"]'):
    num = os.environ.get("INPUT_MARKS")

    with open(f'{filename}.yaml', 'w') as f:
        data = yaml.safe_load(f)
        data["execucao"]["mensagem"] = num 
        yaml.dump(data,f,sort_keys=False)
        print(data) 
    print('done!')

read_and_modify_one_block_of_yaml_data()
