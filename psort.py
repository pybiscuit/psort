# options to implement
# [d, f, M, R, r, o, g]
# stretch implementations
# [h, sort=WORD, v, b i]

import sys
import argparse

parser = argparse.ArgumentParser(description='python implmentation of sort')
parser.add_argument('-d', action='store_true')
parser.add_argument('-f', action='store_true')
parser.add_argument('-m', action='store_true')
parser.add_argument('-r', action='store_true')
parser.add_argument('-v', action='store_true')
parser.add_argument('-o', '--output', action='store', type=str)
parser.add_argument('-g', action='store_true')
parser.add_argument('files', action='store', type=str, nargs='?')

args = parser.parse_args()


def no_files():
    usin = input("(separate lists with comma',') >>> ")
    usin_lst = usin.split(',')
    usin_lst = [x.strip() for x in usin_lst]

    usin_sorted = sorted(usin_lst)
    for line in usin_sorted:
        print(line)

def main():
    func_dict = {
            'd': dict_order,
            'f': ignore_case,
            'm': month_sort,
            'r': random_sort,
            'v': reverse_sort,
            'g': gennum
            }
    out_data = [] 
    for key in func_dict:
        if vars(args)[key]:
            exe_func = func_dict[key]
            if isinstance(args.files, str):
                with open(args.files, 'r') as f:
                    data = f.read()
                    print(data)
                    out_data.append(exe_func(split(data)))

    print(out_data)

def split(spin):
    rlst = spin.split('\n')
    rlst = [x.strip() for x in rlst]
    return rlst

def dict_order(to_sort):
    sorted_lst = sorted(to_sort)
    for lin in sorted_lst:
         print(lin)

def ignore_case():
    pass

def gennum():
    pass

def month_sort():
    pass

def reverse_sort():
    pass

def random_sort():
    pass

def out_file():
    pass

if not args.files:
    no_files()
else:
    main()
