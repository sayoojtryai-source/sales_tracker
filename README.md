# caek — Sales Order Admin

A small, daily-use sales order management web app for the **caek** brand
(cakes, brownies, cookies). Works on laptop and smartphone.

## Features

- Admin login (single-user by default, more can be added in the DB)
- Product management (create / edit / delete) with name, category, price, quantity, description, active flag
- Order creation with multiple line items — stock is automatically deducted
- **Edit orders** — update customer name, phone, and notes after creation
- **Delete orders** — removes the order and restores stock automatically
- **Customer management** — customers are auto-saved when a phone number is entered on an order; view order history per customer, add customers manually
- INR pricing throughout (₹)
- SQLite database (single `caek.db` file, zero setup)
- Timestamps stored in local time (matches your server timezone)
- Dashboard widgets:
  - Orders today / past days / all time
  - Sales today / past days / all time (in INR)
  - Stock on hand & low-stock alerts
- Order list filterable by **All / Today / Past**
- One-click **Excel (.xlsx)** export for products, sales, and customers
- Responsive UI — mobile-first nav, touch-friendly forms

## Quick start

```bash
# 1. Install dependencies (Python 3.10+)
pip install -r requirements.txt

# 2. (Optional) Seed sample products
python seed.py

# 3. Run
python app.py
```

Then open <http://localhost:5000>.

**Default login:** `admin` / `admin123` (change the password in the DB after first login).

## Configuration

Environment variables (optional):

| Variable | Purpose | Default |
|----------|---------|---------|
| `CAEK_SECRET_KEY` | Flask session secret | `change-me-in-production-please` |
| `CAEK_DATABASE_URL` | SQLAlchemy database URL | `sqlite:///caek.db` |

## Data model

- `users` — admin accounts (username + hashed password)
- `products` — name, category, price (INR), quantity, description, is_active
- `orders` — customer name/phone/notes, timestamp, total, optional link to customer record
- `order_items` — snapshot of product name / unit price / qty / line total per order
- `customers` — name, phone (unique), email, address, notes, created date

Line items snapshot the price & name at time of sale, so historical reports stay correct even if a product is later edited or removed.

Customer records are created automatically when an order is placed with a phone number. If the same phone number appears on a future order, it links to the existing customer record. Orders without a phone number remain as walk-in and are not linked.

## Daily use

- **Take an order:** Dashboard → **+ New Order** → pick products & qty → Create. Stock drops automatically.
- **Edit an order:** Orders → View → Edit (change customer name, phone, or notes).
- **Delete an order:** Orders → View → Delete. Stock is restored automatically.
- **Check today's numbers:** Dashboard widgets.
- **View customers:** Customers → see all customers with total orders and spend.
- **Export to Excel:** *Products .xlsx*, *Sales .xlsx*, or *Customers .xlsx* from the relevant pages.
- **Add a new product:** Products → *+ Add product*.
- **Add a customer manually:** Customers → *+ Add Customer*.

## Deployment notes

- For production, set `CAEK_SECRET_KEY` and run behind a WSGI server
  (e.g. `gunicorn -w 2 -b 0.0.0.0:5000 app:app`).
- Back up `caek.db` regularly — it contains all your products, orders, and customers.
- The app runs a safe, idempotent schema migration on startup, so updating to a newer version requires no manual DB changes.
