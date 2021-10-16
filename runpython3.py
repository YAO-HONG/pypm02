import os
from glob import glob

class TreesCounter2:
    @staticmethod
    def count(path, stage, model, cat):
        w = os.path.join(path, stage, model, cat, '*.jpg')
        count = len(glob(w))
        
        return count

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str, required=True)
parser.add_argument('-s', '--stage', type=str, required=True, choices=['train', 'test'])
parser.add_argument('-m', '--model', type=str, required=True, choices=['tree', 'leaf'])  
parser.add_argument('-c', '--category', type=str, required=True) 

args = parser.parse_args()

print(f'{args.model} {args.category}:'
      f'{TreesCounter2.count(args.path, args.stage, args.model ,args.category)}')
