#!/usr/bin/python3

def main():
    with open("src/challenge.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        char = chr(int(line))
        print(char, end="")
    print()

if __name__ == "__main__":
    main()
