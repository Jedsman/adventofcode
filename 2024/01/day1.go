// main.go
package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// Part1 calculates total distance between sorted pairs
func Part1(data string) int {
	left, right := parseInput(data)
	
	// Sort both slices
	sort.Ints(left)
	sort.Ints(right)
	
	// Calculate sum of absolute differences
	total := 0
	for i := range left {
		diff := left[i] - right[i]
		if diff < 0 {
			diff = -diff
		}
		total += diff
	}
	
	return total
}

// Part2 calculates similarity score based on right-side frequencies
func Part2(data string) int {
	left, right := parseInput(data)
	
	// Create frequency map for right numbers
	freq := make(map[int]int)
	for _, r := range right {
		freq[r]++
	}
	
	// Calculate similarity score
	total := 0
	for _, num := range left {
		total += num * freq[num]
	}
	
	return total
}

// parseInput splits input string into two slices of integers
func parseInput(data string) ([]int, []int) {
	// Split input into lines and trim any whitespace
	lines := strings.Split(strings.TrimSpace(data), "\n")
	
	// Pre-allocate slices to avoid reallocation
	left := make([]int, 0, len(lines))
	right := make([]int, 0, len(lines))
	
	// Process each line
	for _, line := range lines {
		// Split line into fields (handles multiple spaces)
		nums := strings.Fields(line)
		if len(nums) == 2 {
			// Parse both numbers and append to respective slices
			l, _ := strconv.Atoi(nums[0])
			r, _ := strconv.Atoi(nums[1])
			left = append(left, l)
			right = append(right, r)
		}
	}
	
	return left, right
}

func main() {
	// Test data
	test := `3   4
4   3
2   5
1   3
3   9
3   3`

	fmt.Printf("Test Part 1: %d\n", Part1(test)) // Should be 11
	fmt.Printf("Test Part 2: %d\n", Part2(test)) // Should be 31
	
	// Read actual data file
	data, err := os.ReadFile("day1.data")
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}
	
	fmt.Printf("Part 1: %d\n", Part1(string(data)))
	fmt.Printf("Part 2: %d\n", Part2(string(data)))
}