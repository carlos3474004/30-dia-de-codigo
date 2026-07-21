import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Non-ASCII characters avoided for judge compatibility
    n = int(input_data[0])
    arr = input_data[1:n+1]
    
    # Reverse the array
    reversed_arr = arr[::-1]
    
    # Print elements separated by spaces
    print(" ".join(reversed_arr))

if __name__ == "__main__":
    main()