# 📦 B2B Supply Chain Management System (SCMS)

A robust, web-based **Supply Chain Management System (SCMS)** built with **Django**, designed to streamline product management, order processing, inventory tracking, and secure payments for businesses operating in the supply chain sector.

---

## 📑 Table of Contents

- [📖 Project Overview](#-project-overview)
- [🎯 Objectives](#-objectives)
- [🔑 Key Features](#-key-features)
- [🗄️ Entities and Attributes](#-entities-and-attributes)
- [🔗 Database Relationships](#-database-relationships)
- [🗺️ Relational Model & Schema](#-relational-model--schema)
- [⚙️ Technologies Used](#-technologies-used)

---

## 📖 Project Overview

This **B2B Supply Chain Management System (SCMS)** provides a centralized, automated platform to manage products, orders, payments, and inventory. The system accommodates multiple user roles — **Admin**, **Suppliers**, **Distributors**, **Retailers**, and **Customers** — with specific functionalities tailored to each.

The SCMS improves operational efficiency by eliminating manual processes and offering an intuitive, interactive interface for supply chain management.

---

## 🎯 Objectives

- Automate and simplify order processing and payment handling.
- Improve efficiency in managing inventory and product listings.
- Provide a centralized platform for communication and transactions.
- Enhance scalability for future integrations like real-time tracking.
- Ensure security through proper authentication and authorization.

---

## 🔑 Key Features

- 🔒 **User Authentication**: Secure login and registration.
- 📦 **Product Management**: Add, edit, and manage product listings.
- 📑 **Order Management**: Place orders, track order status, and manage them centrally.
- 📊 **Inventory Management**: Track product availability and sales.
- 💳 **Payment Integration**: Secure, trackable payment handling.
- 👥 **Role-based Access Control (RBAC)**: Role-specific access and functionalities.
- ❌ **Order Cancellation & Refund**: Customers can cancel orders under specific policies.

---

## 🗄️ Entities and Attributes

| Entity    | Attributes                                                                                      |
|-----------|-------------------------------------------------------------------------------------------------|
| **Users** | user_id (PK), username, email, password, role (Admin, Supplier, Distributor, Customer)           |
| **Customer** | customer_id (PK), user_id (FK), phone, address                                                  |
| **Supplier** | supplier_id (PK), name, email, phone, address, company_id (FK)                                  |
| **Company** | company_id (PK), name, address, website, logo                                                    |
| **Product** | product_id (PK), name, description, price, quantity, sold_quantity, supplier_id (FK), company_id (FK) |
| **Order** | order_id (PK), customer_id (FK), product_id (FK), quantity, date_ordered, status                   |
| **OrderItem** | order_item_id (PK), order_id (FK), product_id (FK), quantity, price                             |
| **Payment** | payment_id (PK), order_id (FK), customer_id (FK), amount, payment_method, status, date           |

---

## 🔗 Database Relationships

| Relationship                     | Type   | Cardinality | Description                                                                 |
|----------------------------------|--------|-------------|-----------------------------------------------------------------------------|
| Users ➝ Orders                   | 1:N    | One-to-Many | A user can place multiple orders.                                           |
| Supplier ➝ Product               | 1:N    | One-to-Many | A supplier can supply multiple products.                                    |
| Product ➝ Order                  | 1:N    | One-to-Many | A product can appear in multiple orders.                                    |
| Customer ➝ Order                 | 1:N    | One-to-Many | A customer can place multiple orders.                                       |
| Order ➝ Payment                  | 1:1    | One-to-One  | Each order has one associated payment.                                      |

---

## 🗺️ Relational Model & Schema

**Core Modules:**
- **Company Module**
- **Supplier Module**
- **Product Module**
- **Customer Module**
- **Order Module**
- **Payment Module**

**Schema Diagram Relationships:**

- **Company** (1) ⟶ (N) **Supplier**
- **Supplier** (1) ⟶ (N) **Product**
- **Product** (1) ⟶ (N) **OrderItem**
- **Customer** (1) ⟶ (N) **Order**
- **Order** (1) ⟶ (N) **OrderItem**
- **Order** (1) ⟶ (1) **Payment**

---

## ⚙️ Technologies Used

- **Backend:** Django (Python)
- **Database:** SQLite / PostgreSQL
- **Frontend:** HTML, CSS, JavaScript
- **ORM:** Django ORM
- **Version Control:** Git, GitHub

---

> 📌 _This project was developed as part of an academic coursework on Supply Chain Management Systems using Django._
