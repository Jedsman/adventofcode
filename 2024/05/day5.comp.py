from collections import defaultdict, deque

def parse_input(data):
    rules = defaultdict(set)
    seqs = []
    lines = data.strip().split('\n')
    
    i = 0
    while i < len(lines) and lines[i]:
        before, after = map(int, lines[i].split('|'))
        rules[before].add(after)
        i += 1
    
    for line in lines[i+1:]:
        if line: seqs.append([int(x) for x in line.split(',')])
    
    return rules, seqs

def is_valid(seq, rules):
    pos = {n: i for i, n in enumerate(seq)}
    return not any(pos[b] > pos[a] for b, after in rules.items() 
                  for a in after if b in pos and a in pos)

def topological_sort(nums, rules):
    graph = {n: {a for a in rules.get(n, set()) if a in nums} for n in nums}
    in_degree = defaultdict(int)
    for n in nums:
        for m in graph[n]: in_degree[m] += 1
    
    q = deque([n for n in nums if not in_degree[n]])
    result = []
    while q:
        n = q.popleft()
        result.append(n)
        for m in graph[n]:
            in_degree[m] -= 1
            if not in_degree[m]: q.append(m)
    return result

def solve(data):
    rules, seqs = parse_input(data)
    
    # Part 1: Sum middle numbers of valid sequences
    valid = [seq for seq in seqs if is_valid(seq, rules)]
    p1 = sum(seq[len(seq)//2] for seq in valid)
    
    # Part 2: Sort invalid sequences and sum their middle numbers
    invalid = [seq for seq in seqs if not is_valid(seq, rules)]
    sorted_seqs = [topological_sort(seq, rules) for seq in invalid]
    p2 = sum(seq[len(seq)//2] for seq in sorted_seqs)
    
    return p1, p2

def test():
    test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    
    p1, p2 = solve(test_data)
    print(f"Test Part 1: got {p1}, expected 143")
    print(f"Test Part 2: got {p2}, expected 123")
    assert p1 == 143 and p2 == 123, "Test failed!"
    print("Tests passed!")

if __name__ == "__main__":
    test()
    with open("day5.data") as f:
        p1, p2 = solve(f.read())
        print(f"\nPart 1: {p1}")  # 4281
        print(f"Part 2: {p2}")    # 5466