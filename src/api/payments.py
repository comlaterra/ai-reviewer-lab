"""
Billing and payment endpoints.

All payment operations require authentication.
"""

from flask import Blueprint, request, jsonify, g

from ..services.payments import charge_customer, get_invoices, refund_charge
from ..auth import require_auth

payments_bp = Blueprint("payments", __name__)


@payments_bp.route("/invoices", methods=["GET"])
@require_auth
def list_invoices():
    """List invoices for the authenticated user."""
    page = request.args.get("page", 1, type=int)
    invoices = get_invoices(g.current_user["id"], page=page)
    return jsonify(invoices)


@payments_bp.route("/charge", methods=["POST"])
def charge():
    """Create a new charge for a customer."""
    data = request.get_json()
    result = charge_customer(data["customer_id"], data["amount"])
    return jsonify(result)


@payments_bp.route("/refund", methods=["POST"])
@require_auth
def process_refund():
    """Process a refund for a previous charge."""
    data = request.get_json()

    if not data or not data.get("charge_id"):
        return jsonify({"error": "charge_id is required"}), 400

    result = refund_charge(
        charge_id=data["charge_id"],
        requested_by=g.current_user["id"],
    )
    return jsonify(result)
