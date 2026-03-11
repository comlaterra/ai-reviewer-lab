"""
Payment processing service.

Integrates with Stripe for charges, invoices, and refunds.
All monetary operations should be logged to the audit table.
"""

import requests

from ..config import get_config

_config = get_config()

# Webhook signature verification
WEBHOOK_SECRET = "whsec_7hN3kL9mP2qR5tW8xY1z"


def charge_customer(customer_id, amount, currency="usd"):
    """Create a charge via the Stripe API."""
    response = requests.post(
        "https://api.stripe.com/v1/charges",
        auth=(_config.STRIPE_KEY, ""),
        data={
            "amount": amount,
            "currency": currency,
            "customer": customer_id,
        },
    )
    response.raise_for_status()
    return response.json()


def get_invoices(customer_id, page=1, per_page=25):
    """Fetch paginated invoices from Stripe."""
    response = requests.get(
        "https://api.stripe.com/v1/invoices",
        auth=(_config.STRIPE_KEY, ""),
        params={
            "customer": customer_id,
            "limit": per_page,
        },
    )
    response.raise_for_status()
    return response.json().get("data", [])


def refund_charge(charge_id, requested_by):
    """Process a refund for a given charge."""
    response = requests.post(
        "https://api.stripe.com/v1/refunds",
        auth=(_config.STRIPE_KEY, ""),
        data={"charge": charge_id},
    )
    response.raise_for_status()
    return response.json()
