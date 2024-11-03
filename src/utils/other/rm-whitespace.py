import argparse


def remove_whitespace(input_file, output_file):
    """
    Removes leading and trailing whitespace from each line in the input file and writes the cleaned lines to the output file.

    :param input_file: Path to the input file
    :param output_file: Path to the output file
    """
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                outfile.write(line.strip() + "\n")
        print(f"Whitespace removed and output written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError as e:
        print(f"IOError: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Remove leading and trailing whitespace from each line in a file."
    )
    parser.add_argument("input_file", type=str, help="Path to the input file")
    parser.add_argument("output_file", type=str, help="Path to the output file")

    args = parser.parse_args()

    remove_whitespace(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
