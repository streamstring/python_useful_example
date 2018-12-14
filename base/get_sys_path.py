# encoding : utf-8


def get_sys_path():
    import sys
    print("The program arguments: ", sys.argv)
    print("The search paths of the program: ")
    for x_path in sys.path:
        print(x_path)
    return "success"


get_sys_path()