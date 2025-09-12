# Matrix operations
def matrix_operations():
    # Create matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Access element: O(1)
    element = matrix[1][2]  # Row 1, Column 2
    
    # Traverse matrix: O(m*n)
    def traverse_matrix(matrix):
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result.append(matrix[i][j])
        return result
    
    # Matrix multiplication: O(m*n*p)
    def matrix_multiply(A, B):
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])
        
        if cols_A != rows_B:
            return None
        
        result = [[0] * cols_B for _ in range(rows_A)]
        
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        
        return result
    
    # Spiral traversal
    def spiral_order(matrix):
        if not matrix:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # Down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            # Up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result