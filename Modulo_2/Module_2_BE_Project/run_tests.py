import sys
import os

def main():
    print("=" * 60)
    print("Running Project Tests")
    print("=" * 60)
    
    sys.path.insert(0, os.path.abspath('.'))
    
    try:
        from tests.tests import (
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
        )
    except ImportError as e:
        print(f"ERROR importing tests: {e}")
        print("Make sure tests/tests.py exists")
        return 1
    
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
    failed = 0
    
    for test_func in tests:
        func_name = test_func.__name__
        print(f"\n{func_name}:")
        try:
            test_func()  
            print("  PASSED")
            passed += 1
        except AssertionError as e:
            print(f"  FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("SUCCESS: All tests passed")
        return 0
    else:
        print("FAILURE: Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())