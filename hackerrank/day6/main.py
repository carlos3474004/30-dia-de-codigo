import sys

def main():
    lines = sys.stdin.read().split()
    if not lines:
        return
    
    t = int(lines[0])
    for i in range(1, t + 1):
        s = lines[i]
        evens = s[::2]
        odds = s[1::2]
        print(f"{evens} {odds}")

if __name__ == "__main__":
    main()