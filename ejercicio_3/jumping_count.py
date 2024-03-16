from typing import List, Tuple

def jumping_count(X)-> int:
    """Function to calculate the number of jumps to reach X"""
    jumps = 0
    while X > 0:
        jumps += 1
        X -= jumps
        if X == -1:
            jumps += 1

    return jumps

def get_first_value()-> int:
    """Function to get the first value"""
    t = int(input("Number of test cases:"))
    if t < 1 or t > 1000:
        raise ValueError("The number of test cases must be between 1 and 100")
    return t

def get_numbers()-> Tuple[int, bool]:
    x = int(input("Enter a number: "))
    is_ok =  x < 1 or x > 106
    return x, is_ok



def main():
    # Get number of test cases
    t = get_first_value()
    # Loop through test cases
    steps = 0
    while steps < t:
        # Get number
        x, is_ok = get_numbers()
        if is_ok:
            print("The number must be between 1 and 106")
        else:
            print(jumping_count(x))
            steps += 1



if __name__ == "__main__":
    main()
