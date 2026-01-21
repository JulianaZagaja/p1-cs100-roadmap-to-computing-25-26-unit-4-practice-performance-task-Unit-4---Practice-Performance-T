"""
=============================================================================
UNIT 4 PRACTICE - Task 4: Generate Inventory Report
=============================================================================
Concepts: List of dictionaries, aggregation, .get() for safe access, nested data

INSTRUCTIONS:
1. Complete the function below where it says # TODO
2. Run this file to test your solution
3. All 4 tests should pass to complete the practice!
=============================================================================
"""

def inventory_report(products):
    """
    Generate a summary report from a list of product dictionaries.
    
    Takes a list of products and returns a dictionary containing:
    - total_products: count of all products
    - total_value: sum of all (price * quantity) values
    - in_stock_count: count of products where in_stock is True
    - categories: a SET of unique category names
    
    Products may or may not have a "quantity" key (default to 1 if missing).
    Products may or may not have "in_stock" key (default to True if missing).
    
    Args:
        products: List of dicts, each with "name", "price", and optionally
                  "category", "quantity", and "in_stock" keys
    
    Returns:
        dict: Report with keys "total_products", "total_value", 
              "in_stock_count", and "categories"
    
    Examples:
        >>> products = [
        ...     {"name": "Apple", "price": 1.50, "quantity": 100, "category": "Fruit", "in_stock": True},
        ...     {"name": "Laptop", "price": 999.99, "quantity": 5, "category": "Electronics", "in_stock": True},
        ...     {"name": "Banana", "price": 0.75, "quantity": 50, "category": "Fruit", "in_stock": False}
        ... ]
        >>> inventory_report(products)
        {
            "total_products": 3,
            "total_value": 5187.45,  # (1.50*100) + (999.99*5) + (0.75*50)
            "in_stock_count": 2,
            "categories": {"Fruit", "Electronics"}
        }
        
        >>> inventory_report([])
        {"total_products": 0, "total_value": 0, "in_stock_count": 0, "categories": set()}
    """
    # TODO: Write your code here (replace 'pass')
    # Hint 1: Handle empty list first
    # Hint 2: Use .get("quantity", 1) for safe access with default
    # Hint 3: Use .get("in_stock", True) for safe access with default
    # Hint 4: Use a set to collect unique categories
    # Hint 5: Calculate total_value as sum of (price * quantity) for each product
    if not products:
        return {"total_products": 0, "total_value": 0, "in_stock_count": 0, "categories": set()}
    total_products = len(products)
    total_value = 0
    in_stock_count = 0
    categories = set()
    for product in products:
        quantity = product.get("quantity", 1)
        if  product.get("in_stock", True):
            in_stock_count += 1
        price = product.get("price", 0)
        total_value += price * quantity
    
        if "category" in product:
            categories.add(product["category"])
    
    return {
        "total_products": total_products,
        "total_value": total_value,
        "in_stock_count": in_stock_count,
        "categories": categories
    }


# =============================================================================
# TEST CODE - Run this file to test your solution
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🛒 TASK 4: inventory_report")
    print("=" * 50)
    
    # Test 1: Full inventory with all fields
    products = [
        {"name": "Apple", "price": 1.50, "quantity": 100, "category": "Fruit", "in_stock": True},
        {"name": "Laptop", "price": 999.99, "quantity": 5, "category": "Electronics", "in_stock": True},
        {"name": "Banana", "price": 0.75, "quantity": 50, "category": "Fruit", "in_stock": False}
    ]
    result = inventory_report(products)
    
    # Check total_products
    if result.get("total_products") == 3:
        print("✅ Test 1a PASSED: total_products = 3")
    else:
        print(f"❌ Test 1a FAILED: Expected total_products=3, got {result.get('total_products')}")
    
    # Check total_value (1.50*100 + 999.99*5 + 0.75*50 = 150 + 4999.95 + 37.5 = 5187.45)
    expected_value = round(1.50*100 + 999.99*5 + 0.75*50, 2)
    if result.get("total_value") == expected_value:
        print(f"✅ Test 1b PASSED: total_value = {expected_value}")
    else:
        print(f"❌ Test 1b FAILED: Expected total_value={expected_value}, got {result.get('total_value')}")
    
    # Check in_stock_count
    if result.get("in_stock_count") == 2:
        print("✅ Test 1c PASSED: in_stock_count = 2")
    else:
        print(f"❌ Test 1c FAILED: Expected in_stock_count=2, got {result.get('in_stock_count')}")
    
    # Check categories (should be a set with "Fruit" and "Electronics")
    if result.get("categories") == {"Fruit", "Electronics"}:
        print("✅ Test 1d PASSED: categories = {'Fruit', 'Electronics'}")
    else:
        print(f"❌ Test 1d FAILED: Expected {{'Fruit', 'Electronics'}}, got {result.get('categories')}")
    
    # Test 2: Empty list
    result = inventory_report([])
    expected = {"total_products": 0, "total_value": 0, "in_stock_count": 0, "categories": set()}
    if result == expected:
        print("✅ Test 2 PASSED: inventory_report([]) handles empty list")
    else:
        print(f"❌ Test 2 FAILED: Expected {expected}, got {result}")
    
    # Test 3: Products with missing optional fields (use defaults)
    products_minimal = [
        {"name": "Mystery Item", "price": 10.00},  # No quantity, category, or in_stock
        {"name": "Widget", "price": 5.00, "quantity": 3}  # No category or in_stock
    ]
    result = inventory_report(products_minimal)
    # quantity defaults to 1, in_stock defaults to True
    # total_value = 10.00*1 + 5.00*3 = 25.00
    if result.get("total_value") == 25.00 and result.get("in_stock_count") == 2:
        print("✅ Test 3 PASSED: Handles missing quantity/in_stock with defaults")
    else:
        print(f"❌ Test 3 FAILED: Expected total_value=25.00, in_stock_count=2")
        print(f"   Got: total_value={result.get('total_value')}, in_stock_count={result.get('in_stock_count')}")
    
    # Test 4: Single product
    single = [{"name": "Single Item", "price": 99.99, "quantity": 2, "category": "Test", "in_stock": True}]
    result = inventory_report(single)
    if result.get("total_products") == 1 and result.get("total_value") == 199.98:
        print("✅ Test 4 PASSED: Single product handled correctly")
    else:
        print(f"❌ Test 4 FAILED: Expected total_products=1, total_value=199.98")
        print(f"   Got: {result}")
    
    print("=" * 50)
    
    # Bonus info
    print("\n💡 Key concepts used:")
    print("   - List of dictionaries (nested data)")
    print("   - .get(key, default) for safe access")
    print("   - Set for unique values")
    print("   - Aggregation (sum, count)")
