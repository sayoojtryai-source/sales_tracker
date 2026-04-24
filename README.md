# caek — Sales Order Admin

A small, daily-use sales order management web app for the **caek** brand
(cakes, brownies, cookies). Works on laptop and smartphone.

## Features

- Admin login (single-user by default, more can be added in the DB)
- Product management (create / edit / delete) with name, category, price, quantity, description, active flag
- Order creation with multiple line items — stock is automatically deducted
- INR pricing throughout (₹)
- SQLite database (single `caek.db` file, zero setup)
- Dashboard widgets:
  - Orders today / past days / all time
  - Sales today / past days / all time (in INR)
  - Stock on hand & low-stock alerts
- Order list filterable by **All / Today / Past**
- One-click **Excel (.xlsx)** export for products and for sales (with both order-summary and line-item sheets)
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
- `orders` — customer, timestamp, total
- `order_items` — snapshot of product name / unit price / qty / line total per order

Line items snapshot the price & name at time of sale, so historical reports stay correct even if a product is later edited or removed.

## Daily use

- **Take an order:** Dashboard → **+ New Order** → pick products & qty → Create. Stock drops automatically.
- **Check today's numbers:** Dashboard widgets.
- **Export to Excel:** Dashboard → *Products .xlsx* or *Sales .xlsx* (filter by scope).
- **Add a new product:** Products → *+ Add product*.

## Deployment notes

- For production, set `CAEK_SECRET_KEY` and run behind a WSGI server
  (e.g. `gunicorn -w 2 -b 0.0.0.0:5000 app:app`).
- Back up `caek.db` regularly — it contains all your products and orders.
