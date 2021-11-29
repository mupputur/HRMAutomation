import sys

def is_last_caps(str_input):
    ch = str_input[-1]
    if ch >= 'A' and ch <='Z':
        return True
    else:
        return False

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Invalid command line operation. Ex: <program.py>  abcD")
        sys.exit(0)
    print(is_last_caps(args[0]))