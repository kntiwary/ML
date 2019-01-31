import os
import sys
import itertools

def find_min(input):
    # implement your logic here

    total_list = []

    for L in range(0, len(input) + 1):
        for subset in itertools.combinations(input, L):
            total_list.append(sum(subset))

    new_list = list(set(total_list))
    new_list.sort()
    for each in range(0, new_list[-1] + 2):
        if each not in new_list:
            print(each)
            break




def print_usage():
    print("Usage:- python {} space-separated-integers".format(
        os.path.basename(__file__),
    ))


def parse_arg():
    parsed_list = []
    for value in sys.argv[1:]:
        try:
            parsed_list.append(int(value))
        except ValueError:
            print_usage()
            exit(1)
    return parsed_list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_list = parse_arg()
        # print(input_list)
        find_min(input_list)
    else:
        print_usage()
        exit(1)