# Temtem One-Backend API

This project is a RESTful API built with Django and PostgreSQL for managing products and user authentication with role-based access control.

## Technologies Used

- Django
- PostgreSQL
- Docker

## Prerequisites

- Python (v3.12 or later)
- pip (Python package manager)
- Docker

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/walidmeguenni/temtem_api.git
   ```

2. Running the application using Docker:
   ```bash
   docker compose up -d --build
   ```

## Important Note
Before testing the API in Postman, please wait around 30 seconds for the application to fully start and for the database migrations and seeds to complete.

The following script is executed during the Docker build process:

```bash
#!/bin/bash

# Wait for Postgres to be ready
echo "Waiting for Postgres..."
sleep 10

# Create migrations
echo "Create migrations"
python manage.py makemigrations
echo "=================================="


# Run migrations
echo "Migrate"
python manage.py migrate
echo "=================================="

# Seed the database
echo "Seed the database"
python manage.py seed_data
echo "=================================="

# Start the application in production mode
echo "Start server"
python manage.py runserver 0.0.0.0:8000
```

## API Testing with Postman

To test the API, use Postman and the following base URL:
```bash
http://localhost:8000
```

## Credentials
To access the API, use the following default credentials for authentication:

### Store Owner
```yaml
Email: john_doe@example.com
Password: password123
```

### Guest User
No credentials required for viewing products.


## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

