# flake8: noqa
import os
import sys


# This function sorts a list of numbers but
# prioritizes one group of numbers to come first.
# It returns whether the higher-priority items were seen at all.
def sort_priority(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


def print_usage():
    instr = "comma-separated-integers"
    print(
        "Usage:- python {} numbers={} group={}".format(
            os.path.basename(__file__),
            instr,
            instr,
        ),
    )


def parse_arg():
    try:
        # numbers = [int(s) for s in sys.argv[1].split('numbers=')[1].split(',')]
        numbers = [int(s) for s in sys.argv[1].split(',')]
        # print("numbers",numbers)
        group = set([int(s)
                     # for s in sys.argv[2].split('group=')[1].split(',')])
                     for s in sys.argv[2].split(',')])
        # print(numbers,group)
        return numbers, group
    except Exception:
        print_usage()
        exit(1)


if __name__ == "__main__":

    if len(sys.argv) == 3:
        # print(sys.argv)
        numbers, group = parse_arg()
        found = sort_priority(numbers, group)
        print("Found: {}".format(found))
        print(numbers)
    else:
        print("else_usage")
        print_usage()
        exit(1)