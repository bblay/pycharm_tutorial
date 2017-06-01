from argparse import ArgumentParser

from my_package.process_data import process_data_file

if __name__ == '__main__':

    arg_parser = ArgumentParser()
    arg_parser.add_argument('--max-lines', default=10)
    args = arg_parser.parse_args()

    # It's best practice to pass params as keywords in case the function changes in the future.
    result = process_data_file(fpath='data.txt', max_lines=args.max_lines)
    print result
