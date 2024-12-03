# Go Implementation of Distance Calculator

This implements the distance calculation challenge in Go, converted from the Python implementation. It serves as a learning exercise to understand the differences between the two languages.

## Key Differences Explained

### 1. Type System
- **Python**: Dynamic typing allows for flexible variable usage
  ```python
  # Type inference happens automatically
  left, right = zip(*(map(int, line.split()) for line in data.strip().split('\n')))
  ```
- **Go**: Static typing requires explicit type declarations
  ```go
  // Types must be declared
  var left, right []int
  // Pre-allocation improves performance
  left := make([]int, 0, len(lines))
  ```

### 2. Input Processing
- **Python**: Uses list comprehensions and built-in functions
  ```python
  left, right = zip(*(map(int, line.split()) for line in data.strip().split('\n')))
  ```
- **Go**: Uses string splitting and explicit loops
  ```go
  lines := strings.Split(strings.TrimSpace(data), "\n")
  for _, line := range lines {
      nums := strings.Fields(line)
      // Process each line...
  }
  ```

### 3. Memory Management
- **Python**: Automatic memory management with dynamic lists
- **Go**: Manual pre-allocation of slices for better performance
  ```go
  // Pre-allocate to avoid reallocations
  left := make([]int, 0, len(lines))
  ```

### 4. Error Handling
- **Python**: Often uses exceptions
  ```python
  with open('day1.data') as f:
      data = f.read()
  ```
- **Go**: Uses explicit error returns
  ```go
  data, err := os.ReadFile("day1.data")
  if err != nil {
      // Handle error
  }
  ```

## Running the Code

To run the Go version:
```bash
go run main.go
```

Make sure the `day1.data` file is in the same directory as the program.

## Code Structure

The code is organized into three main functions:
1. `parseInput`: Handles the input processing for both parts
2. `Part1`: Calculates distances between sorted pairs
3. `Part2`: Calculates similarity scores based on frequencies
