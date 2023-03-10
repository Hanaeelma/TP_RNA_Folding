#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import argparse
from TP_part1 import main_script1
from TP_part2 import main_script2
from TP_part3 import main_script3


def main():
    start = time.time()

    parser = argparse.ArgumentParser(
        description='RNA folding problem; Output log ratio tabulate, graph of interaction profiles')
    parser.add_argument('-i', '-input', type=str, required=True,
                        help='Input directory with RNA file (pdb) [str]')
    parser.add_argument('-o', '-output', type=str, required=True,
                        help='Output directory of log ratio file (tabular) '
                             'and matplolib plot (png) [str]')
    parser.add_argument('-te', '-test', type=str, required=True,
                        help='Input RNA test file [pdb]')
    parser.add_argument('-s', '-savepng', type=lambda x: (str(x).lower() == 'true'), default=False,
                        required=False, help='An optional boolean switch to output matplolib plot (png) [boolean]')
    parser.add_argument('-p', '-printpng', type=lambda x: (str(x).lower() == 'true'), default=True,
                        required=False, help='An optional boolean switch to print matplolib plot [boolean]')

    args = parser.parse_args()
    results_file = True
    try:
        os.remove("Results_RNA_folding_problem.txt")
    except:
        pass

    with open('output.txt', 'a+') as file_scoring:
        file_scoring.write(f'Input : {args.i}\n')
        file_scoring.write(f'Input test: {args.te}\n')
        file_scoring.write(f'Output : {args.o}\n')
        file_scoring.write(f'plot: {args.p}\n')
        file_scoring.write(f'plot : {args.s}\n\n')

    file = args.i
    directory = args.o
    file_test = args.te
    print_png = args.p
    save_png = args.s

    main_script1(file, directory, results_file)
    main_script2(directory, save_png, print_png, results_file)
    main_script3(directory, file_test, results_file)

    end = time.time()
    elapsed = end - start

    print(f'Total runtime : {elapsed:.1f}s')

    with open('Results_RNA_folding_problem.txt', 'a+') as file_scoring:
        file_scoring.write(f'\nTotal runtime : {elapsed:.1f}s\n')
        file_scoring.write(f'\nSaving Results...')

if __name__ == '__main__':
    main()
