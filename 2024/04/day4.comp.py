def solve_xmas_puzzle(grid_data, part2=False):
    # Create grid from input
    grid = [list(line.strip()) for line in grid_data.split('\n') if line.strip()]
    rows, cols = len(grid), len(grid[0])
    
    if part2:
        # Part 2: Find X-shaped MAS patterns
        count = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] != 'A':
                    continue
                diag1 = grid[r-1][c-1] + 'A' + grid[r+1][c+1]
                diag2 = grid[r-1][c+1] + 'A' + grid[r+1][c-1]
                if any(d in ['MAS', 'SAM'] for d in [diag1, diag1[::-1]]) and \
                   any(d in ['MAS', 'SAM'] for d in [diag2, diag2[::-1]]):
                    count += 1
        return count
    
    else:
        # Part 1: Find XMAS in all directions
        dirs = [(dx, dy) for dx in (-1,0,1) for dy in (-1,0,1) if dx or dy]
        count = 0
        for r in range(rows):
            for c in range(cols):
                for dx, dy in dirs:
                    if (0 <= r + 3*dx < rows and 0 <= c + 3*dy < cols and
                        ''.join(grid[r + i*dx][c + i*dy] for i in range(4)) == 'XMAS'):
                        count += 1
        return count

# Example usage
test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

print(f"Part 1: {solve_xmas_puzzle(test_data)}")  # Should print 18
print(f"Part 2: {solve_xmas_puzzle(test_data, True)}")  # Should print 9

# For actual puzzle
with open('day4.data', 'r') as f:
    puzzle_data = f.read()
    print(f"Puzzle Part 1: {solve_xmas_puzzle(puzzle_data)}")
    print(f"Puzzle Part 2: {solve_xmas_puzzle(puzzle_data, True)}")