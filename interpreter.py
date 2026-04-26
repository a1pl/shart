import sys


def main():
    if len(sys.argv) < 2:
        print("usage: interpreter.py <file>")
        sys.exit(1)

    lines = []
    with open(sys.argv[1]) as f:
        for line in f:
            lines.append(line.rstrip("\n"))

    print(lines)


if __name__ == "__main__":
    main()
