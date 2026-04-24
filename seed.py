"""Seed the database with a few sample products for quick onboarding.

Usage:
    python seed.py
"""
from decimal import Decimal

from app import create_app
from models import Product, db

SAMPLES = [
    ("Classic Chocolate Brownie", "Brownies", Decimal("80.00"), 25, "Fudgy, rich, single-origin cocoa."),
    ("Walnut Brownie", "Brownies", Decimal("95.00"), 18, "Loaded with roasted walnuts."),
    ("Red Velvet Cupcake", "Cakes", Decimal("120.00"), 30, "Cream cheese frosting."),
    ("Chocolate Truffle Cake (500g)", "Cakes", Decimal("650.00"), 6, "Rich dark chocolate truffle."),
    ("Butter Cookies (pack of 12)", "Cookies", Decimal("180.00"), 40, "Classic buttery shortbread."),
    ("Choco-chip Cookies (pack of 6)", "Cookies", Decimal("140.00"), 35, "Melt-in-the-mouth chocolate chip."),
]


def main() -> None:
    app = create_app()
    with app.app_context():
        added = 0
        for name, category, price, qty, desc in SAMPLES:
            if Product.query.filter_by(name=name).first():
                continue
            db.session.add(
                Product(
                    name=name,
                    category=category,
                    price=price,
                    quantity=qty,
                    description=desc,
                    is_active=True,
                )
            )
            added += 1
        db.session.commit()
        print(f"Seeded {added} product(s). Total products: {Product.query.count()}")


if __name__ == "__main__":
    main()
