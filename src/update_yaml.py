import yaml
import os

# get the input and convert it to int

def read_and_modify_one_block_of_yaml_data(filename='teste', key=execucao.mensagem, value="message"):
    with open(f'{filename}.yaml', 'r') as f:
        data = yaml.safe_load(f)
        data[f'{key}'] = f'{value}' 
        print(data) 
    print('done!')
