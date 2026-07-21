import sys

def main():
    n = int(input().strip())
    
    # Convert n to binary string and remove the '0b' prefix
    binary_str = bin(n)[2:]
    
    # Split by '0' to group consecutive '1's
    ones_groups = binary_str.split('0')
    
    # Find the maximum length of consecutive '1's
    max_ones = max(len(group) for group in ones_groups)
    
    print(max_ones)

if __name__ == '__main__':
    main()