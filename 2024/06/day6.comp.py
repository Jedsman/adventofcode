def solve(data):
    grid = [list(line) for line in data.strip().split('\n')]
    start = next((x, y) for y, row in enumerate(grid)
                 for x, c in enumerate(row) if c == '^')
    
    def simulate(grid, pos, find_loops=False):
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        cur_dir = 0
        seen = {(pos, cur_dir)}
        
        while True:
            x, y = pos
            nx, ny = x + dirs[cur_dir][0], y + dirs[cur_dir][1]
            
            if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)):
                return len({p for p, _ in seen}) if not find_loops else False
                
            if grid[ny][nx] in '#O':
                cur_dir = (cur_dir + 1) % 4
            else:
                pos = (nx, ny)
                
            state = (pos, cur_dir)
            if state in seen:
                return True if find_loops else len(seen)
            seen.add(state)
    
    part1 = simulate(grid, start)
    
    part2 = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.' and (x, y) != start:
                grid[y][x] = 'O'
                if simulate(grid, start, True):
                    part2 += 1
                grid[y][x] = '.'
    
    return part1, part2

test = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

print("Test:", solve(test))
with open('day6.data') as f:
    print("Solution:", solve(f.read()))