import re

class Parser:
    def __init__(self, text):
        # Part 1: Just find all multiplications
        self.products = [int(x) * int(y) for x, y in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', text)]
        
        # Part 2: Get all instructions in order: multiplications, do(), and don't()
        muls = [(m.start(), 'mul', m.groups()) for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', text)]
        dos = [(m.start(), 'do', None) for m in re.finditer(r'do\(\)', text)]
        donts = [(m.start(), 'dont', None) for m in re.finditer(r'don\'t\(\)', text)]
        self.instructions = sorted(muls + dos + donts)

    def part1(self):
        return sum(self.products)

    def part2(self):
        enabled = True
        total = 0
        for _, type_, vals in self.instructions:
            if type_ == 'do': enabled = True
            elif type_ == 'dont': enabled = False
            elif enabled: total += int(vals[0]) * int(vals[1])
        return total

# Quick test
test1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"
p1 = Parser(test1).part1()  # Should be 2*4 + 11*8 + 8*5 = 8 + 88 + 40 = 161
p2 = Parser(test2).part2()  # Should be 2*4 + 8*5 = 8 + 40 = 48
print(f"Test - Part 1: {p1} (expect 161), Part 2: {p2} (expect 48)")

# Actual solution
content = open('day3.ini.txt').read()
parser = Parser(content)
print(f"Part 1: {parser.part1()}")
print(f"Part 2: {parser.part2()}")