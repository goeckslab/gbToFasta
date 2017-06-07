import sys
import argparse

def filter(cds_file, valid_cds_file):
    valid = open(valid_cds_file, 'w')
    with open(cds_file, 'r') as f:
        for line in f:
            if len(line.rstrip().split('\t')) == 2:
                valid.write(line)
    valid.close()

def main(argv):
    parser = argparse.ArgumentParser(description='Filter out records without CDS coordinates')
    parser.add_argument('-f', help='cds file')
    parser.add_argument('-o', help='validated cds file')
    args = parser.parse_args()
    filter(args.f, args.o)

if __name__ == '__main__':
    main(sys.argv)
