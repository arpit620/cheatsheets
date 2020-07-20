import math
import argparse

parser = argparse.ArgumentParser(description="Calculate volume of Cylinder")
# parser.add_argument('radius', type=int, help="Radius of Cylinder")
# parser.add_argument('height', type=int, help="Height of Cylinder")
# parser.add_argument('-r', '--radius', type=int, help="Radius of Cylinder")
# parser.add_argument('-H', '--height', type=int, help="Height of Cylinder")
parser.add_argument('-r', '--radius', type=int, metavar='',required=True, help="Radius of Cylinder")
parser.add_argument('-H', '--height', type=int, metavar='',required=True, help="Height of Cylinder")
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quite')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = math.pi * ( radius ** 2 ) * height
    return vol


if __name__ == "__main__":
    # print(cylinder_volume(2, 4))

    # python parser_py.py 4 2
    # python parser_py.py -h
    volume = cylinder_volume(args.radius, args.height)

    # python parser_py.py -r 2 -H 4 -q
    if args.quiet:
        print(volume)
    elif args.verbose:
        print("Print using verbose:", volume)
    else:
        print("Normal: ", volume)


