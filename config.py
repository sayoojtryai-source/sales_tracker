import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("CAEK_SECRET_KEY", "change-me-in-production-please")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "CAEK_DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'caek.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BRAND_NAME = "caek"
    BRAND_TAGLINE = "cakes. brownies. cookies."
    CURRENCY_SYMBOL = "₹"  # INR
