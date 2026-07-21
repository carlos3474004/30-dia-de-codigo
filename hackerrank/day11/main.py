import sys

def main():
    # Read all lines from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    # Build the 6x6 2D matrix
    arr = []
    for line in input_data:
        if line.strip():
            arr.append(list(map(int, line.split())))

    # Initialize maximum sum to a very small number
    max_sum = -64

    # Iterate through possible top-left corners of each hourglass
    # Rows 0 to 3, Columns 0 to 3
    for r in range(4):
        for c in range(4):
            # Calculate the current hourglass sum
            top = arr[r][c] + arr[r][c+1] + arr[r][c+2]
            middle = arr[r+1][c+1]
            bottom = arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
            
            current_sum = top + middle + bottom
            
            # Keep track of the maximum sum found
            if current_sum > max_sum:
                max_sum = current_sum

    print(max_sum)

if __name__ == '__main__':
    main()