"""
=============================================================================
UNIT 4 PRACTICE - Task 2: Create Product Dictionary
=============================================================================
Concepts: Dictionary creation, default parameters, .get() method

INSTRUCTIONS:
1. Complete the function below where it says # TODO
2. Run this file to test your solution
3. All 4 tests should pass before moving to Task 3
=============================================================================
"""

def create_product(name, price, category="General", in_stock=True):
    """
    Create a product dictionary with the given information.
    
    Takes product details and returns them as a structured dictionary.
    The category and in_stock have default values if not specified.
    
    Args:
        name: Product name (required, string)
        price: Product price (required, float)
        category: Product category (default "General", string)
        in_stock: Whether item is in stock (default True, bool)
    
    Returns:
        dict: A dictionary with keys "name", "price", "category", "in_stock"
    
    Examples:
        >>> create_product("Apple", 1.50)
        {"name": "Apple", "price": 1.50, "category": "General", "in_stock": True}
        
        >>> create_product("Laptop", 999.99, category="Electronics")
        {"name": "Laptop", "price": 999.99, "category": "Electronics", "in_stock": True}
        
        >>> create_product("Vintage Clock", 150.00, in_stock=False)
        {"name": "Vintage Clock", "price": 150.00, "category": "General", "in_stock": False}
    """
    # TODO: Write your code here (replace 'pass')
    # Hint: Create a dictionary with the four keys and return it
    # The parameters already have default values, so just use them!
    pass


# =============================================================================
# TEST CODE - Run this file to test your solution
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🛒 TASK 2: create_product")
    print("=" * 50)
    
    # Test 1: Only required parameters (use defaults)
    result = create_product("Apple", 1.50)
    expected = {"name": "Apple", "price": 1.50, "category": "General", "in_stock": True}
    if result == expected:
        print("✅ Test 1 PASSED: create_product('Apple', 1.50) uses defaults")
    else:
        print(f"❌ Test 1 FAILED: Expected {expected}")
        print(f"   Got: {result}")
    
    # Test 2: Override category with keyword argument
    result = create_product("Laptop", 999.99, category="Electronics")
    expected = {"name": "Laptop", "price": 999.99, "category": "Electronics", "in_stock": True}
    if result == expected:
        print("✅ Test 2 PASSED: create_product('Laptop', 999.99, category='Electronics')")
    else:
        print(f"❌ Test 2 FAILED: Expected {expected}")
        print(f"   Got: {result}")
    
    # Test 3: Override in_stock with keyword argument
    result = create_product("Vintage Clock", 150.00, in_stock=False)
    expected = {"name": "Vintage Clock", "price": 150.00, "category": "General", "in_stock": False}
    if result == expected:
        print("✅ Test 3 PASSED: create_product('Vintage Clock', 150.00, in_stock=False)")
    else:
        print(f"❌ Test 3 FAILED: Expected {expected}")
        print(f"   Got: {result}")
    
    # Test 4: Override both optional parameters
    result = create_product("Gaming Mouse", 79.99, category="Electronics", in_stock=False)
    expected = {"name": "Gaming Mouse", "price": 79.99, "category": "Electronics", "in_stock": False}
    if result == expected:
        print("✅ Test 4 PASSED: create_product with all keyword args")
    else:
        print(f"❌ Test 4 FAILED: Expected {expected}")
        print(f"   Got: {result}")
    
    print("=" * 50)
