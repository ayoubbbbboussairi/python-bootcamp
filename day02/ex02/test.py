import vector
# Example usage and testing:
vec1 = vector([[1., 2., 3.]])
vec2 = vector([[4.], [5.], [6.]])

# Test vector addition
result_addition = vec1 + vec2
print(f"Vector Addition: {result_addition}")

# Test vector subtraction
result_subtraction = vec1 - vec2
print(f"Vector Subtraction: {result_subtraction}")

# Test scalar multiplication
result_scalar_mul = vec1 * 2
print(f"Scalar Multiplication: {result_scalar_mul}")

# Test scalar division
result_scalar_div = vec1 / 2
print(f"Scalar Division: {result_scalar_div}")

# Test vector initialization with size
vec_size = vector(3)
print(f"Vector with size: {vec_size}")

# Test vector initialization with range
vec_range = vector((10, 16))
print(f"Vector with range: {vec_range}")
