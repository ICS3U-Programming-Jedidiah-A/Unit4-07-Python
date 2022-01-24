# !/usr/bin/env python3
# Created By: Jedidiah.
# Date: Jan 22, 2022
# This program prints numbers from 1000 to 2000.
def main():
    for counter in range(1000, 2001, 1):
        if counter % 5 == 0:
            print("")
        print(counter, "", end="")
    print("\nThanks for playing")


if __name__ == "__main__":
    main()
    