import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import CartAbandonmentUrgencyDiscountOptimizerClient

def main():
    client = CartAbandonmentUrgencyDiscountOptimizerClient()
    res = client.optimize_cart_recovery_incentive(cart_value_usd=850.0, gross_margin_pct=0.42, hours_since_abandonment=18)
    print("=== Cart Abandonment Urgency Discount Optimizer Output ===")
    print(f"Cart: ${res['original_cart_value_usd']} (Abandoned: {res['hours_since_abandonment']}h)")
    print(f"Optimal Discount: {res['recommended_discount_percentage']} (-${res['discount_savings_usd']})")
    print(f"Recovery Price: ${res['checkout_recovery_price_usd']} | Retained Margin: ${res['retained_merchant_margin_usd']}")
    print(f"Voucher Code: {res['ephemeral_voucher_code']}")

if __name__ == '__main__':
    main()
