// Optimized solution for guard path simulation
use std::fs;

fn main() {
    // Test input from problem description
    let test = r#"....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."#;

    let (test1, test2) = solve(test);
    println!("Test: {}, {}", test1, test2);
    
    // Solve actual input
    let input = fs::read_to_string("day6.data").unwrap();
    let (part1, part2) = solve(&input);
    println!("Solution: {}, {}", part1, part2);
}

fn solve(input: &str) -> (usize, usize) {
    // Convert 2D grid to flat array for better performance
    let width = input.lines().next().unwrap().len();
    let mut grid = vec![b'.'; width * input.lines().count()];
    let mut start = 0;
    
    // Parse input into flat byte array
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.bytes().enumerate() {
            let idx = y * width + x;
            grid[idx] = c;
            if c == b'^' { start = idx; }
        }
    }

    let part1 = simulate(&mut grid, width, start, false);
    let part2 = count_loops(&mut grid, width, start);
    
    (part1, part2)
}

fn simulate(grid: &mut [u8], width: usize, start: usize, find_loops: bool) -> usize {
    // Directional vectors: up, right, down, left
    const DIRS: [(isize, isize); 4] = [(0, -1), (1, 0), (0, 1), (-1, 0)];
    let height = grid.len() / width;
    let mut pos = start;
    let mut dir = 0;
    
    // Track visited states: each position can be visited in 4 directions
    let mut states = vec![false; width * height * 4];
    states[pos * 4 + dir] = true;
    let mut unique = 1;  // Count unique positions visited
    
    loop {
        // Convert flat index to 2D coordinates
        let (x, y) = (pos % width, pos / width);
        let (nx, ny) = ((x as isize + DIRS[dir].0), (y as isize + DIRS[dir].1));
        
        // Check if we're leaving the grid
        if nx < 0 || nx >= width as isize || ny < 0 || ny >= height as isize {
            return if find_loops { 0 } else { unique };
        }
        
        // Calculate next position's flat index
        let next = (ny as usize * width + nx as usize) as usize;
        if grid[next] == b'#' || grid[next] == b'O' {
            // Hit obstacle, turn right
            dir = (dir + 1) & 3;
        } else {
            // Move forward
            pos = next;
            // Check if this is a new unique position
            if !states[pos * 4] && !states[pos * 4 + 1] && 
               !states[pos * 4 + 2] && !states[pos * 4 + 3] {
                unique += 1;
            }
        }
        
        // Check if we've seen this state before (loop detection)
        let state_idx = pos * 4 + dir;
        if states[state_idx] {
            return if find_loops { 1 } else { unique };
        }
        states[state_idx] = true;
    }
}

fn count_loops(grid: &mut [u8], width: usize, start: usize) -> usize {
    // Try placing obstacle at each empty position
    let mut count = 0;
    for i in 0..grid.len() {
        if grid[i] == b'.' && i != start {
            grid[i] = b'O';
            count += simulate(grid, width, start, true);
            grid[i] = b'.';
        }
    }
    count
}