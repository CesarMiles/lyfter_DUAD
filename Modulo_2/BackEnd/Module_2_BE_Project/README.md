# 🐾 Pet E-commerce Backend

Backend API for pet store with Flask, PostgreSQL, JWT authentication and Redis caching.

## Features
- JWT authentication with roles (admin/user)
- Product CRUD with admin protection
- Purchase system with invoicing
- Redis caching for optimization
- Unit testing included

## Installation

### 1. Requirements
- Python 3.9+
- PostgreSQL 14+
- Redis 7+

### 2. Database Setup
CREATE DATABASE pet_ecommerce;
CREATE SCHEMA m2_be_project;

### 3. Running the Application
python main.py

## API Endpoints

### Authentication
- POST /register - Register user
- POST /login - Login user
- GET /me - User profile

### Products
- GET /products - List products (cached)
- POST /create_product - Create product (admin only)
- PATCH /modify_product - Modify product (admin only)
- DELETE /delete_product - Delete product (admin only)

### Purchases
- POST /purchase_product - Make purchase
- Purchase endpoint requires this payload to complete purchase. 
    # {
    #     "products": [
    #         {
    #             "product_id": 4,
    #             "quantity": 1
    #         },
    #         {
    #             "product_id": 3, 
    #             "quantity": 3
    #         }
    #     ]
    # }

### Invoices
- GET /invoices - My invoices
- GET /invoices/<id> - Invoice details
- PATCH /admin/invoices/<id> - Update status (admin only)

### Testing
# Run all tests
python run_tests.py

# Run individual tests
python -m pytest tests/tests.py -v

### Database
## ER Diagram
![Database ER Diagram](docs/images/ER_Diagram.png)

*Figure: Database schema showing relationships between Users, Products, Invoices, and Invoice Details tables.*

## Schema
- users: id, email, password, role, created_at
- products: id, name, price, stock
- invoices: id, user_id, total, status
- invoice_details: id, invoice_id, product_id, quantity

### Cache Strategy
## Cached Endpoints::
- GET /products → 10 minutes
- GET /products?id=X → 5 minutes
- GET /invoices → 10 minutes

## Cache Invalidation:
- CREATE/UPDATE/DELETE products → clear product cache
- New purchase → clear inventory cache
- Invoice update → clear invoice cache

### Security
- JWT with RSA 256-bit encryption
- Role validation on endpoints
- SQL injection protection
- Input data validation

### Project Structure

Module_2_BE_Project/
├── main.py              # Entry point
├── models.py            # Database models
├── user_module.py       # User endpoints
├── product_module.py    # Product endpoints
├── invoice_module.py    # Invoice endpoints
├── purchase_module.py   # Purchase logic
├── cache.py             # Redis manager
├── decorators.py        # Auth decorators
├── tests/               # Unit tests
└── requirements.txt     # Dependencies

### Deployment
Create database schema
Generate RSA keys
Start Redis server
Run python main.py
