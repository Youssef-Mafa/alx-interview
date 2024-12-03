#!/usr/bin/python3
"""Island Perimeter - Optimized Implementation
Combines aspects of both previous approaches for improved readability 
and potential performance.
"""
def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.
    An island consists of 1's (land) surrounded by 0's (water).
    
    Args:
        grid: List[List[int]] where 1 represents land and 0 represents water
        
    Returns:
        int: The perimeter of the island
    """
    if not grid or not grid[0]:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with all 4 sides as potential edges
                current_edges = 4
                
                # Check all adjacent cells and subtract 1 for each adjacent land
                neighbors = [
                    (i-1, j), # up
                    (i+1, j), # down
                    (i, j-1), # left
                    (i, j+1)  # right
                ]
                
                for ni, nj in neighbors:
                    if (0 <= ni < rows and 
                        0 <= nj < cols and 
                        grid[ni][nj] == 1):
                        current_edges -= 1
                        
                perimeter += current_edges
                
    return perimeter
