import re

class Parser:
    def __init__(self, text):
        # Get all instructions in order: multiplications, do(), and don't()
        muls = [(m.start(), 'mul', m.groups()) for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', text)]
        dos = [(m.start(), 'do', None) for m in re.finditer(r'do\(\)', text)]
        donts = [(m.start(), 'dont', None) for m in re.finditer(r'don\'t\(\)', text)]
        self.instructions = sorted(muls + dos + donts)

    def calculate(self):
        enabled = True
        total = 0
        stats = {'total': 0, 'enabled': 0, 'disabled': 0}
        
        for _, type_, vals in self.instructions:
            if type_ == 'do': 
                enabled = True
            elif type_ == 'dont': 
                enabled = False
            else:  # multiplication
                stats['total'] += 1
                if enabled:
                    stats['enabled'] += 1
                    total += int(vals[0]) * int(vals[1])
                else:
                    stats['disabled'] += 1
        
        return total, stats

# Test examples from problem
test1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

total1, stats1 = Parser(test1).calculate()
print(f"Test Part 1: {total1} (expect 161)")  # 2*4 + 5*5 + 11*8 + 8*5

total2, stats2 = Parser(test2).calculate()
print(f"Test Part 2: {total2} (expect 48)")   # 2*4 + 8*5 (middle muls disabled)

if __name__ == "__main__":
    content = open('day3.data').read()
    total, stats = Parser(content).calculate()
    print(f"Sum of enabled products: {total}")
    print(f"Total: {stats['total']}, Enabled: {stats['enabled']}, Disabled: {stats['disabled']}")