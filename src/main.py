import argparse


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Process some input.')
    # Add arguments
    parser.add_argument('input1', type=str, help='first input string')
    # Parse the arguments
    args = parser.parse_args()
    custom_input = args.input

    print(custom_input)

    pass


if __name__ == '__main__':
    main()


