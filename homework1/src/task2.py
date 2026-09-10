def add(x, y):
    return x + y

def same_length(str1:str, str2: str) -> bool:
    length_str1 = len(str1)
    length_str2 = len(str2)
    return length_str1 == length_str2

def combine_string(str1:str, str2:str) -> str:
    return str1+str2

def main():
    print("="*50)
    print("Integer Stuff")
    print("="*50)

    # Int + Int
    x = 1
    y = 2
    print(f"{x} + {y} = {add(x, y)}")

    # Float + Float
    x = 1.5
    y = 2.5
    print(f"{x} + {y} = {add(x, y)}")

    # Int + Float
    x = 1
    y = 2.5
    print(f"{x} + {y} = {add(x, y)}")

    print("="*50)
    print("Boolean Stuff")
    print("="*50)

    # Compare String Length (True)
    string_1 = "Potato"
    string_2 = "Tomato"
    print(f"Length of string 1 ({string_1}) is equal to length of string 2 ({string_2}) : {same_length(string_1, string_2)}")

    # Compare String Length (False)
    string_1 = "Success"
    string_2 = "Fail"
    print(f"Length of string 1 ({string_1}) is equal to length of string 2 ({string_2}) : {same_length(string_1, string_2)}")

    print("="*50)
    print("String Operation")
    print("="*50)

    string_1 = "What"
    string_2 = " am I doing"
    print(f"{string_1} + {string_2} = {combine_string(string_1, string_2)}")
if __name__ == "__main__":
    main()