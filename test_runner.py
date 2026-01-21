"""
=============================================================================
GitHub Classroom Test Runner for Unit 4 Practice Performance Task
=============================================================================
This script runs individual tests and returns exit code 0 (pass) or 1 (fail).
Usage: python3 test_runner.py <test_name>
=============================================================================
"""

import sys

def run_test(test_name):
    """Run a specific test by name. Returns True if passed, False if failed."""
    
    # =========================================================================
    # TASK 1 TESTS
    # =========================================================================
    if test_name == "task1_normal":
        from task1_calculate_total import calculate_total
        result = calculate_total([10.99, 5.50, 9.48])
        assert result == 25.97, f"Expected 25.97, got {result}"
        return True
    
    elif test_name == "task1_empty":
        from task1_calculate_total import calculate_total
        result = calculate_total([])
        assert result == 0, f"Expected 0, got {result}"
        return True
    
    elif test_name == "task1_single":
        from task1_calculate_total import calculate_total
        result = calculate_total([19.99])
        assert result == 19.99, f"Expected 19.99, got {result}"
        return True
    
    elif test_name == "task1_max_items":
        from task1_calculate_total import calculate_total
        result = calculate_total([10.00, 20.00, 30.00, 40.00, 50.00], max_items=3)
        assert result == 60.0, f"Expected 60.0, got {result}"
        return True
    
    # =========================================================================
    # TASK 2 TESTS
    # =========================================================================
    elif test_name == "task2_defaults":
        from task2_create_product import create_product
        result = create_product("Apple", 1.50)
        expected = {"name": "Apple", "price": 1.50, "category": "General", "in_stock": True}
        assert result == expected, f"Expected {expected}, got {result}"
        return True
    
    elif test_name == "task2_category":
        from task2_create_product import create_product
        result = create_product("Laptop", 999.99, category="Electronics")
        expected = {"name": "Laptop", "price": 999.99, "category": "Electronics", "in_stock": True}
        assert result == expected, f"Expected {expected}, got {result}"
        return True
    
    elif test_name == "task2_in_stock":
        from task2_create_product import create_product
        result = create_product("Vintage Clock", 150.00, in_stock=False)
        expected = {"name": "Vintage Clock", "price": 150.00, "category": "General", "in_stock": False}
        assert result == expected, f"Expected {expected}, got {result}"
        return True
    
    elif test_name == "task2_all_kwargs":
        from task2_create_product import create_product
        result = create_product("Gaming Mouse", 79.99, category="Electronics", in_stock=False)
        expected = {"name": "Gaming Mouse", "price": 79.99, "category": "Electronics", "in_stock": False}
        assert result == expected, f"Expected {expected}, got {result}"
        return True
    
    # =========================================================================
    # TASK 3 TESTS
    # =========================================================================
    elif test_name == "task3_filter_under_5":
        from task3_filter_products import filter_products
        products = [
            {"name": "Apple", "price": 1.50},
            {"name": "Laptop", "price": 999.99},
            {"name": "Banana", "price": 0.75},
            {"name": "Headphones", "price": 49.99},
            {"name": "Milk", "price": 3.99}
        ]
        result = filter_products(products, 5.00)
        expected = [
            {"name": "Apple", "price": 1.50},
            {"name": "Banana", "price": 0.75},
            {"name": "Milk", "price": 3.99}
        ]
        assert result == expected, f"Expected {expected}, got {result}"
        return True
    
    elif test_name == "task3_filter_excludes":
        from task3_filter_products import filter_products
        products = [
            {"name": "Apple", "price": 1.50},
            {"name": "Laptop", "price": 999.99},
            {"name": "Banana", "price": 0.75},
            {"name": "Headphones", "price": 49.99},
            {"name": "Milk", "price": 3.99}
        ]
        result = filter_products(products, 49.99)
        assert len(result) == 4, f"Expected 4 items, got {len(result)}"
        assert {"name": "Laptop", "price": 999.99} not in result, "Laptop should be excluded"
        return True
    
    elif test_name == "task3_no_matches":
        from task3_filter_products import filter_products
        products = [
            {"name": "Apple", "price": 1.50},
            {"name": "Laptop", "price": 999.99}
        ]
        result = filter_products(products, 0.50)
        assert result == [], f"Expected [], got {result}"
        return True
    
    elif test_name == "task3_empty_input":
        from task3_filter_products import filter_products
        result = filter_products([], 100)
        assert result == [], f"Expected [], got {result}"
        return True
    
    # =========================================================================
    # TASK 4 TESTS
    # =========================================================================
    elif test_name == "task4_total_products":
        from task4_inventory_report import inventory_report
        products = [
            {"name": "Apple", "price": 1.50, "quantity": 100, "category": "Fruit", "in_stock": True},
            {"name": "Laptop", "price": 999.99, "quantity": 5, "category": "Electronics", "in_stock": True},
            {"name": "Banana", "price": 0.75, "quantity": 50, "category": "Fruit", "in_stock": False}
        ]
        result = inventory_report(products)
        assert result.get("total_products") == 3, f"Expected total_products=3, got {result.get('total_products')}"
        return True
    
    elif test_name == "task4_total_value":
        from task4_inventory_report import inventory_report
        products = [
            {"name": "Apple", "price": 1.50, "quantity": 100, "category": "Fruit", "in_stock": True},
            {"name": "Laptop", "price": 999.99, "quantity": 5, "category": "Electronics", "in_stock": True},
            {"name": "Banana", "price": 0.75, "quantity": 50, "category": "Fruit", "in_stock": False}
        ]
        result = inventory_report(products)
        expected_value = round(1.50*100 + 999.99*5 + 0.75*50, 2)  # 5187.45
        assert result.get("total_value") == expected_value, f"Expected total_value={expected_value}, got {result.get('total_value')}"
        return True
    
    elif test_name == "task4_in_stock_count":
        from task4_inventory_report import inventory_report
        products = [
            {"name": "Apple", "price": 1.50, "quantity": 100, "category": "Fruit", "in_stock": True},
            {"name": "Laptop", "price": 999.99, "quantity": 5, "category": "Electronics", "in_stock": True},
            {"name": "Banana", "price": 0.75, "quantity": 50, "category": "Fruit", "in_stock": False}
        ]
        result = inventory_report(products)
        assert result.get("in_stock_count") == 2, f"Expected in_stock_count=2, got {result.get('in_stock_count')}"
        return True
    
    elif test_name == "task4_categories":
        from task4_inventory_report import inventory_report
        products = [
            {"name": "Apple", "price": 1.50, "quantity": 100, "category": "Fruit", "in_stock": True},
            {"name": "Laptop", "price": 999.99, "quantity": 5, "category": "Electronics", "in_stock": True},
            {"name": "Banana", "price": 0.75, "quantity": 50, "category": "Fruit", "in_stock": False}
        ]
        result = inventory_report(products)
        assert result.get("categories") == {"Fruit", "Electronics"}, f"Expected categories={{Fruit, Electronics}}, got {result.get('categories')}"
        return True
    
    elif test_name == "task4_empty":
        from task4_inventory_report import inventory_report
        result = inventory_report([])
        expected = {"total_products": 0, "total_value": 0, "in_stock_count": 0, "categories": set()}
        assert result == expected, f"Expected {expected}, got {result}"
        return True
    
    else:
        print(f"Unknown test: {test_name}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 test_runner.py <test_name>")
        print("\nAvailable tests:")
        print("  Task 1: task1_normal, task1_empty, task1_single, task1_max_items")
        print("  Task 2: task2_defaults, task2_category, task2_in_stock, task2_all_kwargs")
        print("  Task 3: task3_filter_under_5, task3_filter_excludes, task3_no_matches, task3_empty_input")
        print("  Task 4: task4_total_products, task4_total_value, task4_in_stock_count, task4_categories, task4_empty")
        sys.exit(1)
    
    test_name = sys.argv[1]
    
    try:
        if run_test(test_name):
            print(f"✅ PASSED: {test_name}")
            sys.exit(0)
        else:
            print(f"❌ FAILED: {test_name}")
            sys.exit(1)
    except AssertionError as e:
        print(f"❌ FAILED: {test_name}")
        print(f"   {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ ERROR: {test_name}")
        print(f"   {type(e).__name__}: {e}")
        sys.exit(1)
