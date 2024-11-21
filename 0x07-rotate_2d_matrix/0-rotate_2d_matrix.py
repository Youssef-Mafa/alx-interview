#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix by 90 degrees clockwise in place."""
    n = len(matrix)
    
    # Perform the rotation layer by layer
    for i in range(n // 2):
        end = n - i - 1
        for j in range(i, end):
            offset = n - 1 - j
            # Save top element
            tmp = matrix[i][j]
            
            # Rotate values among four sides
            # Top <- Left
            matrix[i][j] = matrix[offset][i]
            
            # Left <- Bottom
            matrix[offset][i] = matrix[end][offset]
            
            # Bottom <- Right
            matrix[end][offset] = matrix[j][end]
            
            # Right <- Top
            matrix[j][end] = tmp


# Example usage
if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Matrix:")
    for row in mat:
        print(row)
    
    rotate_2d_matrix(mat)
    
    print("\nRotated Matrix:")
    for row in mat:
        print(row)
