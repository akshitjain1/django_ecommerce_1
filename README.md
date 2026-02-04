# CampusMart - E-commerce Platform

A Django-based e-commerce platform designed for campus communities to buy and sell products.

## Features

- User authentication and profile management
- Product listing and detailed product views
- Shopping cart functionality
- Order management system
- Admin panel for product and order management
- Responsive design with custom templates

## Tech Stack

- **Backend:** Django 5.2.10
- **Database:** MySQL
- **Frontend:** HTML, CSS
- **Media Storage:** Local file storage

## Project Structure

```
campusmart/
├── admin_panel/      # Admin dashboard functionality
├── campusmart/       # Main project settings
├── main/             # Core app (products, homepage)
├── orders/           # Order management
├── users/            # User authentication and profiles
├── media/            # User-uploaded files
├── static/           # Static files (CSS, JS, images)
└── templates/        # HTML templates
```

## Installation

### Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/campusmart.git
   cd campusmart
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```
   - Update the `.env` file with your configuration:
     - `SECRET_KEY`: Generate a new Django secret key
     - `DB_NAME`: Your MySQL database name
     - `DB_USER`: Your MySQL username
     - `DB_PASSWORD`: Your MySQL password
     - `DB_HOST`: Database host (usually localhost)
     - `DB_PORT`: Database port (usually 3306)

5. **Create MySQL database**
   ```sql
   CREATE DATABASE ecommerce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files (for production)**
   ```bash
   python manage.py collectstatic
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Main site: http://localhost:8000/
    - Admin panel: http://localhost:8000/admin/

## Usage

### For Customers
- Browse products on the homepage
- Register/login to create an account
- Add products to cart
- Place orders
- View order history in profile

### For Admins
- Access admin dashboard at `/admin/`
- Add, edit, or delete products
- Manage orders and view order details
- Monitor platform activity

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| SECRET_KEY | Django secret key | - |
| DEBUG | Debug mode (True/False) | True |
| DB_ENGINE | Database engine | django.db.backends.mysql |
| DB_NAME | Database name | ecommerce_db |
| DB_USER | Database user | root |
| DB_PASSWORD | Database password | - |
| DB_HOST | Database host | localhost |
| DB_PORT | Database port | 3308 |
| ALLOWED_HOSTS | Comma-separated allowed hosts | - |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security

- Never commit your `.env` file
- Keep your `SECRET_KEY` secret
- Set `DEBUG = False` in production
- Use strong database passwords
- Regularly update dependencies

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

Your Name - [@akshitjain1](https://github.com/akshitjain1)

Project Link: [https://github.com/akshitjain1/django_ecommerce_1](https://github.com/akshitjain1/django_ecommerce_1)

## Acknowledgments

- Django Documentation
- Bootstrap (if used)
- All contributors who helped build this project
