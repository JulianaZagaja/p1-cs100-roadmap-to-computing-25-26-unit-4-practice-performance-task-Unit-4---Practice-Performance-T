"""
=============================================================================
UNIT 4 PRACTICE - Task 3: Filter Products by Price
=============================================================================
Concepts: List comprehensions, filter pattern, transform pattern

INSTRUCTIONS:
1. Complete the function below where it says # TODO
2. Run this file to test your solution
3. All 4 tests should pass before moving to Task 4
=============================================================================
"""

def filter_products(products, max_price):
    """
    Filter products to only include those at or below max_price.
    
    Takes a list of product dictionaries and returns a NEW list
    containing only products where price <= max_price.
    Returns an empty list if no products match or if input is empty.
    
    Args:
        products: List of dicts, each with at least a "price" key
        max_price: Maximum price to include (float/int)
    
    Returns:
        list: New list containing only products at or below max_price
    
    Examples:
        >>> products = [
        ...     {"name": "Apple", "price": 1.50},
        ...     {"name": "Laptop", "price": 999.99},
        ...     {"name": "Banana", "price": 0.75}
        ... ]
        >>> filter_products(products, 10.00)
        [{"name": "Apple", "price": 1.50}, {"name": "Banana", "price": 0.75}]
        
        >>> filter_products(products, 0.50)
        []
        
        >>> filter_products([], 100)
        []
    """
    # TODO: Write your code here (replace 'pass')
    # Hint 1: Use a list comprehension with a filter
    # Hint 2: Filter pattern: [item for item in list if condition]
    # Hint 3: Access the price with product["price"]
    if not products:
        return []
    filtered = [p for p in products if p["price"] <= max_price]
    return filtered

# =============================================================================
# TEST CODE - Run this file to test your solution
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🛒 TASK 3: filter_products")
    print("=" * 50)
    
    # Test data
    products = [
        {"name": "Apple", "price": 1.50},
        {"name": "Laptop", "price": 999.99},
        {"name": "Banana", "price": 0.75},
        {"name": "Headphones", "price": 49.99},
        {"name": "Milk", "price": 3.99}
    ]
    
    # Test 1: Filter products under $5
    result = filter_products(products, 5.00)
    expected = [
        {"name": "Apple", "price": 1.50},
        {"name": "Banana", "price": 0.75},
        {"name": "Milk", "price": 3.99}
    ]
    if result == expected:
        print("✅ Test 1 PASSED: filter_products(products, 5.00) returns 3 items")
    else:
        print(f"❌ Test 1 FAILED: Expected {expected}")
        print(f"   Got: {result}")
    
    # Test 2: Filter with exact price match
    result = filter_products(products, 49.99)
    # Should include Apple, Banana, Headphones, Milk (all <= 49.99)
    if len(result) == 4 and {"name": "Laptop", "price": 999.99} not in result:
        print("✅ Test 2 PASSED: filter_products(products, 49.99) excludes expensive items")
    else:
        print(f"❌ Test 2 FAILED: Expected 4 items without Laptop, got {len(result) if result else 0} items")
    
    # Test 3: No products match
    result = filter_products(products, 0.50)
    if result == []:
        print("✅ Test 3 PASSED: filter_products(products, 0.50) returns [] when nothing matches")
    else:
        print(f"❌ Test 3 FAILED: Expected [], got {result}")
    
    # Test 4: Empty product list
    result = filter_products([], 100)
    if result == []:
        print("✅ Test 4 PASSED: filter_products([], 100) handles empty list")
    else:
        print(f"❌ Test 4 FAILED: Expected [], got {result}")
    
    print("=" * 50)
