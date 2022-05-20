#! /usr/bin/env python3
# elegant greeting app

import argparse

parser = argparse.ArgumentParser(description='A greeting application')

parser.add_argument('name',help='It is the name you wanna greet')
args = parser.parse_args()

print('Hello, {}'.format(args.name))