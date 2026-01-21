"""
=============================================================================
UNIT 4 PRACTICE PERFORMANCE TASK - Combined Scoring
=============================================================================
Run this file to test ALL tasks at once and see your total score.

Make sure all task files are in the same folder:
- task1_calculate_total.py
- task2_create_product.py  
- task3_filter_products.py
- task4_inventory_report.py
=============================================================================
"""

from task1_calculate_total import calculate_total
from task2_create_product import create_product
from task3_filter_products import filter_products
from task4_inventory_report import inventory_report

if __name__ == "__main__":
    print("=" * 60)
    print("🛒 UNIT 4 PRACTICE PERFORMANCE TASK - TEST RESULTS")
    print("=" * 60)
    
    total_points = 0
    
    # =========================================================================
    # Task 1 Tests (20 points)
    # =========================================================================
    print("\n📋 TASK 1: calculate_total (20 points)")
    print("-" * 40)
    task1_points = 0
    
    try:
        # Test 1.1: Normal cart
        result = calculate_total([10.99, 5.50, 9.48])
        if result == 25.97:
            print("  ✅ Test 1.1 PASSED: Normal cart total")
            task1_points += 5
        else:
            print(f"  ❌ Test 1.1 FAILED: Expected 25.97, got {result}")
        
        # Test 1.2: Empty cart
        result = calculate_total([])
        if result == 0:
            print("  ✅ Test 1.2 PASSED: Empty cart returns 0")
            task1_points += 5
        else:
            print(f"  ❌ Test 1.2 FAILED: Expected 0, got {result}")
        
        # Test 1.3: Single item
        result = calculate_total([19.99])
        if result == 19.99:
            print("  ✅ Test 1.3 PASSED: Single item")
            task1_points += 5
        else:
            print(f"  ❌ Test 1.3 FAILED: Expected 19.99, got {result}")
        
        # Test 1.4: With max_items limit
        result = calculate_total([10.00, 20.00, 30.00, 40.00, 50.00], max_items=3)
        if result == 60.0:
            print("  ✅ Test 1.4 PASSED: max_items slicing works")
            task1_points += 5
        else:
            print(f"  ❌ Test 1.4 FAILED: Expected 60.0, got {result}")
            
    except Exception as e:
        print(f"  ❌ TASK 1 ERROR: {e}")
    
    print(f"  📊 Task 1 Score: {task1_points}/20 points")
    total_points += task1_points
    
    # =========================================================================
    # Task 2 Tests (25 points)
    # =========================================================================
    print("\n📋 TASK 2: create_product (25 points)")
    print("-" * 40)
    task2_points = 0
    
    try:
        # Test 2.1: Defaults only
        result = create_product("Apple", 1.50)
        expected = {"name": "Apple", "price": 1.50, "category": "General", "in_stock": True}
        if result == expected:
            print("  ✅ Test 2.1 PASSED: Uses default values")
            task2_points += 7
        else:
            print(f"  ❌ Test 2.1 FAILED: Expected {expected}, got {result}")
        
        # Test 2.2: Override category
        result = create_product("Laptop", 999.99, category="Electronics")
        expected = {"name": "Laptop", "price": 999.99, "category": "Electronics", "in_stock": True}
        if result == expected:
            print("  ✅ Test 2.2 PASSED: category='Electronics'")
            task2_points += 6
        else:
            print(f"  ❌ Test 2.2 FAILED: Expected {expected}, got {result}")
        
        # Test 2.3: Override in_stock
        result = create_product("Vintage Clock", 150.00, in_stock=False)
        expected = {"name": "Vintage Clock", "price": 150.00, "category": "General", "in_stock": False}
        if result == expected:
            print("  ✅ Test 2.3 PASSED: in_stock=False")
            task2_points += 6
        else:
            print(f"  ❌ Test 2.3 FAILED: Expected {expected}, got {result}")
        
        # Test 2.4: All parameters
        result = create_product("Gaming Mouse", 79.99, category="Electronics", in_stock=False)
        expected = {"name": "Gaming Mouse", "price": 79.99, "category": "Electronics", "in_stock": False}
        if result == expected:
            print("  ✅ Test 2.4 PASSED: All kwargs specified")
            task2_points += 6
        else:
            print(f"  ❌ Test 2.4 FAILED: Expected {expected}, got {result}")
            
    except Exception as e:
        print(f"  ❌ TASK 2 ERROR: {e}")
    
    print(f"  📊 Task 2 Score: {task2_points}/25 points")
    total_points += task2_points
    
    # =========================================================================
    # Task 3 Tests (25 points)
    # =========================================================================
    print("\n📋 TASK 3: filter_products (25 points)")
    print("-" * 40)
    task3_points = 0
    
    products = [
        {"name": "Apple", "price": 1.50},
        {"name": "Laptop", "price": 999.99},
        {"name": "Banana", "price": 0.75},
        {"name": "Headphones", "price": 49.99},
        {"name": "Milk", "price": 3.99}
    ]
    
    try:
        # Test 3.1: Filter under $5
        result = filter_products(products, 5.00)
        expected = [
            {"name": "Apple", "price": 1.50},
            {"name": "Banana", "price": 0.75},
            {"name": "Milk", "price": 3.99}
        ]
        if result == expected:
            print("  ✅ Test 3.1 PASSED: Filter under $5 returns 3 items")
            task3_points += 7
        else:
            print(f"  ❌ Test 3.1 FAILED: Expected 3 items, got {len(result) if result else 0}")
        
        # Test 3.2: Filter with exact price match
        result = filter_products(products, 49.99)
        if len(result) == 4 and {"name": "Laptop", "price": 999.99} not in result:
            print("  ✅ Test 3.2 PASSED: Filter <= 49.99 excludes Laptop")
            task3_points += 6
        else:
            print(f"  ❌ Test 3.2 FAILED: Expected 4 items without Laptop")
        
        # Test 3.3: No matches
        result = filter_products(products, 0.50)
        if result == []:
            print("  ✅ Test 3.3 PASSED: No matches returns []")
            task3_points += 6
        else:
            print(f"  ❌ Test 3.3 FAILED: Expected [], got {result}")
        
        # Test 3.4: Empty list input
        result = filter_products([], 100)
        if result == []:
            print("  ✅ Test 3.4 PASSED: Empty input returns []")
            task3_points += 6
        else:
            print(f"  ❌ Test 3.4 FAILED: Expected [], got {result}")
            
    except Exception as e:
        print(f"  ❌ TASK 3 ERROR: {e}")
    
    print(f"  📊 Task 3 Score: {task3_points}/25 points")
    total_points += task3_points
    
    # =========================================================================
    # Task 4 Tests (30 points)
    # =========================================================================
    print("\n📋 TASK 4: inventory_report (30 points)")
    print("-" * 40)
    task4_points = 0
    
    inventory = [
        {"name": "Apple", "price": 1.50, "quantity": 100, "category": "Fruit", "in_stock": True},
        {"name": "Laptop", "price": 999.99, "quantity": 5, "category": "Electronics", "in_stock": True},
        {"name": "Banana", "price": 0.75, "quantity": 50, "category": "Fruit", "in_stock": False}
    ]
    
    try:
        result = inventory_report(inventory)
        
        # Test 4.1: total_products
        if result.get("total_products") == 3:
            print("  ✅ Test 4.1 PASSED: total_products = 3")
            task4_points += 6
        else:
            print(f"  ❌ Test 4.1 FAILED: Expected total_products=3, got {result.get('total_products')}")
        
        # Test 4.2: total_value
        expected_value = round(1.50*100 + 999.99*5 + 0.75*50, 2)  # 5187.45
        if result.get("total_value") == expected_value:
            print(f"  ✅ Test 4.2 PASSED: total_value = {expected_value}")
            task4_points += 8
        else:
            print(f"  ❌ Test 4.2 FAILED: Expected {expected_value}, got {result.get('total_value')}")
        
        # Test 4.3: in_stock_count
        if result.get("in_stock_count") == 2:
            print("  ✅ Test 4.3 PASSED: in_stock_count = 2")
            task4_points += 6
        else:
            print(f"  ❌ Test 4.3 FAILED: Expected 2, got {result.get('in_stock_count')}")
        
        # Test 4.4: categories set
        if result.get("categories") == {"Fruit", "Electronics"}:
            print("  ✅ Test 4.4 PASSED: categories = {'Fruit', 'Electronics'}")
            task4_points += 5
        else:
            print(f"  ❌ Test 4.4 FAILED: Expected {{'Fruit', 'Electronics'}}, got {result.get('categories')}")
        
        # Test 4.5: Empty list
        result = inventory_report([])
        expected = {"total_products": 0, "total_value": 0, "in_stock_count": 0, "categories": set()}
        if result == expected:
            print("  ✅ Test 4.5 PASSED: Empty list handled correctly")
            task4_points += 5
        else:
            print(f"  ❌ Test 4.5 FAILED: Empty list not handled")
            
    except Exception as e:
        print(f"  ❌ TASK 4 ERROR: {e}")
    
    print(f"  📊 Task 4 Score: {task4_points}/30 points")
    total_points += task4_points
    
    # =========================================================================
    # Final Score
    # =========================================================================
    print("\n" + "=" * 60)
    print(f"🏆 TOTAL SCORE: {total_points}/100 points")
    print("=" * 60)
    
    if total_points == 100:
        print("🌟 PERFECT SCORE! All solutions correct!")
        print("   You're ready for the assessment! 🎉")
    elif total_points >= 80:
        print("✨ Great job! Review any failing tests before the assessment.")
    elif total_points >= 60:
        print("📚 Good progress! Keep practicing the concepts you missed.")
    else:
        print("💪 Keep practicing! Review the study guide and try again.")
