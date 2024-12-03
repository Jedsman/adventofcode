# Part 1: Calculate total distance between sorted pairs
def part1(data):
    left, right = zip(*(map(int, line.split()) for line in data.strip().split('\n')))
    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

# Part 2: Calculate similarity score based on right-side frequencies
def part2(data):
    left, right = zip(*(map(int, line.split()) for line in data.strip().split('\n')))
    freq = {}
    for r in right:
        freq[r] = freq.get(r, 0) + 1
    return sum(num * freq.get(num, 0) for num in left)

# Test and run both parts
def main():
    test = """3   4
4   3
2   5
1   3
3   9
3   3"""
    
    print(f"Test Part 1: {part1(test)}")  # Should be 11
    print(f"Test Part 2: {part2(test)}")  # Should be 31
    
    with open('day1.data') as f:
        data = f.read()
        print(f"Part 1: {part1(data)}")
        print(f"Part 2: {part2(data)}")

if __name__ == "__main__":
    main()