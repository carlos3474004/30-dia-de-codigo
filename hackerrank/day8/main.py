import sys

def main():
    # Read all lines from input at once
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    # First line is N (number of entries)
    n = int(input_data[0])

    phone_book = {}

    # Read the next N lines to populate the dictionary
    for i in range(1, n + 1):
        name, number = input_data[i].split()
        phone_book[name] = number

    # Process all remaining lines as queries
    queries = input_data[n + 1:]
    for query in queries:
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")

if __name__ == "__main__":
    main()