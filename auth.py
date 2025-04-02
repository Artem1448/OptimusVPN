from yoomoney import Authorize

Authorize(
    client_id="6D196F0EE5B5B38096E46C2325828F8FBE7886A1E36A9A1506E1CDA09804B58C",
    client_secret="CD5269103534D68975789CF20BBD8EC47448E08EF6E8CB1ECF4F324A8C68370085FEB7D63DC26AB9E6A322BBBE0D335B94233EAC36041038794592566C8E4228",
    redirect_uri="https://yoomoney.ru",
    scope=[
        "account-info",
        "operation-history",
        "payment-p2p",
    ]
)