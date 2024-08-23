# Cloth Shop Management System

# 📄 Project Overview
This project is a Django-based web application designed to manage an online clothing store. It includes features for both administrators and users, allowing for efficient management of products, user accounts, and transactions.

# Key Components
- **AdminApp**:
  - **Purpose** :Manages the backend operations, such as adding or updating products, processing orders, and managing user accounts.
  - **Files**:
      - **'admin.py'**: Defines the admin interface for managing the database models.
      - **'models.py'**: Contains the data models that represent the shop's products, orders, and other relevant entities.
      - **'views.py'**: Handles the logic for rendering admin pages and processing backend operations.
- **UserApp**:
  - **Purpose**: Handles all user interactions, including browsing products, managing shopping carts and wishlists, making purchases, and managing user profiles.
  - **Files**:
     - **'views.py'**: Implements the logic for rendering user-facing pages and processing user requests.
     - **'templates/'**: Contains HTML templates for various user pages such as home, login, product details, and shopping cart.

- **Database**:
  - **'productdb.db'**: An SQLite database used to store product data, user information, orders, and other relevant records.

- **Static and Media Files**:
  - **Images**: The images/ directory contains product images that are used within the application.
  - **CSS**: The templates/ folder includes CSS files for styling the web pages.

- **Core Django Configuration**:
  - **'settings.py'**: Configures the Django project settings, including database configuration, static file handling, and installed apps.
  - **'urls.py'**: Maps URLs to their respective view functions or classes.
  - **'manage.py'**: A command-line utility for interacting with this Django project (e.g., running the development server, executing migrations).


# Features
- **Admin Dashboard**: Allows administrators to manage products, view orders, and manage user accounts.
- **User Authentication**: Users can sign up, log in, and manage their profiles.
- **Product Browsing**: Users can browse products, add items to their shopping cart or wishlist, and view product details.
- **Order Management**: Users can place orders, view their order history, and make payments.
