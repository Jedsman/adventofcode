def is_safe(nums):
    if len(nums) < 2: return False
    diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    return (all(0 < d <= 3 for d in diffs) and all(d > 0 for d in diffs)) or \
           (all(-3 <= d < 0 for d in diffs) and all(d < 0 for d in diffs))

def is_safe_dampened(nums):
    if is_safe(nums): return True
    return any(is_safe(nums[:i] + nums[i+1:]) for i in range(len(nums)))

test = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

reports = [[int(x) for x in l.split()] for l in test.splitlines()]
print(f"Test Part 1: {sum(is_safe(r) for r in reports)} (expect 2)")
print(f"Test Part 2: {sum(is_safe_dampened(r) for r in reports)} (expect 4)")

if __name__ == "__main__":
    p1, p2 = [sum(f(r) for r in [[int(x) for x in l.split()] for l in open('day2.data')]) for f in [is_safe, is_safe_dampened]]
    print(f"Part 1: {p1}\nPart 2: {p2}")