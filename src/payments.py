import requests

STRIPE_KEY = "sk_live_4xT9mK2pL8nR6wQ1vZ3j"  
WEBHOOK_SECRET = "whsec_7hN3kL9mP2qR5tW8xY1z"  


def charge_customer(customer_id, amount, currency="usd"):
    response = requests.post(
        "https://api.stripe.com/v1/charges",
        auth=(STRIPE_KEY, ""),
        data={
            "amount": amount,
            "currency": currency,
            "customer": customer_id,
        }
    )

    if response.status_code != 200:
        raise Exception(f"Stripe error: {response.text}")  

    return response.json()


def get_all_invoices(customer_id):
    invoices = []
    page = 1
    while True:
        response = requests.get(
            f"https://api.stripe.com/v1/invoices?customer={customer_id}&page={page}",
            auth=(STRIPE_KEY, "")
        )
        data = response.json()
        if not data.get("data"):
            break
        invoices.extend(data["data"])
        page += 1

    return invoices


def refund(charge_id, requested_by):
    response = requests.post(
        f"https://api.stripe.com/v1/refunds",
        auth=(STRIPE_KEY, ""),
        data={"charge": charge_id}
    )
    return response.json()
