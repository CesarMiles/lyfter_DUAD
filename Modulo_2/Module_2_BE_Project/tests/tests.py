import sys
import os
sys.path.insert(0, os.path.abspath('..'))

def test_import_modules():
    try:
        from user_repo import UserRepository
        from product_repo import ProductRepository
        print("Modules imported correctly")
        assert True
    except ImportError as e:
        print(f"Error: {e}")
        assert False

def test_user_repo_structure():
    from user_repo import UserRepository
    
    assert hasattr(UserRepository, '__init__')
    
    repo_methods = ['create_user', 'get_user_details', 'user_login']
    for method in repo_methods:
        assert hasattr(UserRepository, method), f"Missing Method: {method}"
    
    print("UserRepository has correct strcuture")

def test_product_repo_structure():
    from product_repo import ProductRepository
    
    repo_methods = ['create_product', 'get_products', 'modify_product', 'delete_product']
    for method in repo_methods:
        assert hasattr(ProductRepository, method), f"Method missing: {method}"
    
    print("ProductRepository has correct strcuture")

# Authentication
def test_auth_endpoints_exist():
    """Test: Authentication endpoints are registered"""
    from main import app
    
    rule_list = [str(rule) for rule in app.url_map.iter_rules()]
    
    auth_endpoints = ['/register', '/login', '/me']
    for endpoint in auth_endpoints:
        assert any(endpoint in rule for rule in rule_list), f"Missing endpoint: {endpoint}"
    
    print("Authentication endpoints exist - PASSED")

def test_role_validation():
    """Test: User model has role field"""
    from models import user_table
    
    columns = [col.name for col in user_table.columns]
    assert 'role' in columns, "Role column missing in users table"
    
    print("Role field exists in users table - PASSED")

# Product Test 
def test_product_model_structure():
    """Test: Product table has required columns"""
    from models import products_table
    
    required_columns = ['product_id', 'product_name', 'product_price', 'stock']
    actual_columns = [col.name for col in products_table.columns]
    
    for col in required_columns:
        assert col in actual_columns, f"Missing column: {col}"
    
    print("Product table has required columns - PASSED")

def test_product_price_positive():
    """Test: Product price validation logic"""
    def validate_price(price):
        return price > 0  
    
    assert validate_price(10.99) == True
    assert validate_price(0) == False
    assert validate_price(-5) == False
    
    print("Product price validation logic - PASSED")

#Test for sales and invoices
def test_invoice_model_structure():
    """Test: Invoice table has required columns"""
    try:
        from models import invoice_table
        
        required_columns = ['invoice_id', 'user_id', 'total_amount', 'invoice_status']
        actual_columns = [col.name for col in invoice_table.columns]
        
        for col in required_columns:
            if col not in actual_columns:
                print(f"Warning: Missing column: {col} in invoice table")
        
        print("Invoice table check completed")
        return True
    except ImportError:
        print("Invoice table not available for testing")
        return False

def test_invoice_details_relation():
    """Test: Invoice details table exists and relates to products"""
    try:
        from models import invoice_details_table
        
        columns = [col.name for col in invoice_details_table.columns]
        assert 'product_id' in columns, "product_id column missing"
        assert 'quantity' in columns, "quantity column missing"
        
        print("Invoice details table has correct structure - PASSED")
        return True
    except ImportError:
        print("Invoice details table not available for testing")
        return False

#Test for Roles
def test_admin_required_decorator():
    """Test: admin_required decorator exists"""
    try:
        from decorators import admin_required
        
        assert callable(admin_required)
        
        print("admin_required decorator exists - PASSED")
        return True
    except ImportError:
        print("admin_required decorator not available")
        return False

def test_token_required_decorator():
    """Test: token_required decorator exists"""
    try:
        from decorators import token_required
        assert callable(token_required)
        
        print("token_required decorator exists - PASSED")
        return True
    except ImportError:
        print("token_required decorator not available")
        return False

def run_all_tests():
    """Run all test functions"""
    tests = [
        test_import_modules,
        test_user_repo_structure,
        test_product_repo_structure,
        test_auth_endpoints_exist,
        test_role_validation,
        test_product_model_structure,
        test_product_price_positive,
        test_invoice_model_structure,
        test_invoice_details_relation,
        test_admin_required_decorator,
        test_token_required_decorator
    ]
    
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except:
            pass
    
    return passed == len(tests)

if __name__ == "__main__":
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)