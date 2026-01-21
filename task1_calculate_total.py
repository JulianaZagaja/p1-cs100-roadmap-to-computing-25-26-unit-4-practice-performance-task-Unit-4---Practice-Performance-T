"""
=============================================================================
UNIT 4 PRACTICE - Task 1: Calculate Shopping Cart Total
=============================================================================
Concepts: List operations, slicing, sum(), handling empty lists

INSTRUCTIONS:
1. Complete the function below where it says # TODO
2. Run this file to test your solution
3. All 4 tests should pass before moving to Task 2
=============================================================================
"""

def calculate_total(prices, max_items=None):
    """
    Calculate the total price of items in a shopping cart.
    
    Takes a list of prices and optionally limits to the first N items.
    Returns the sum of prices, rounded to 2 decimal places.
    Returns 0 for an empty list.
    
    Args:
        prices: List of prices (floats/ints)
        max_items: Optional limit - only sum the first N items (default None = all items)
    
    Returns:
        float: Total price rounded to 2 decimal places
    
    Examples:
        >>> calculate_total([10.99, 5.50, 9.48])
        25.97
        
        >>> calculate_total([10.99, 5.50, 9.48], max_items=2)
        16.49
        
        >>> calculate_total([])
        0
        
        >>> calculate_total([19.99])
        19.99
    """
    # TODO: Write your code here (replace 'pass')
    # Hint 1: Check if prices is empty first
    # Hint 2: Use slicing if max_items is provided: prices[:max_items]
    # Hint 3: Use sum() and round() for the final result
    pass


# =============================================================================
# TEST CODE - Run this file to test your solution
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🛒 TASK 1: calculate_total")
    print("=" * 50)
    
    # Test 1: Normal cart with multiple items
    result = calculate_total([10.99, 5.50, 9.48])
    if result == 25.97:
        print("✅ Test 1 PASSED: calculate_total([10.99, 5.50, 9.48]) = 25.97")
    else:
        print(f"❌ Test 1 FAILED: Expected 25.97, got {result}")
    
    # Test 2: Empty cart
    result = calculate_total([])
    if result == 0:
        print("✅ Test 2 PASSED: calculate_total([]) = 0")
    else:
        print(f"❌ Test 2 FAILED: Expected 0, got {result}")
    
    # Test 3: Single item
    result = calculate_total([19.99])
    if result == 19.99:
        print("✅ Test 3 PASSED: calculate_total([19.99]) = 19.99")
    else:
        print(f"❌ Test 3 FAILED: Expected 19.99, got {result}")
    
    # Test 4: Limited to first 3 items
    result = calculate_total([10.00, 20.00, 30.00, 40.00, 50.00], max_items=3)
    if result == 60.0:
        print("✅ Test 4 PASSED: calculate_total([10, 20, 30, 40, 50], max_items=3) = 60.0")
    else:
        print(f"❌ Test 4 FAILED: Expected 60.0, got {result}")
    
    print("=" * 50)
