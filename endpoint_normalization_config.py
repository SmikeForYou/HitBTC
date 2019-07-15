endpoints_config = [
    {
        "method": "GET",
        "uri": '/account/transactions',
        "normalization_rules": {
            "timestamp": "updatedAt",
            "assetName": "currency",
            "type": "type",
            "quantity": "amount",
            "price": {
                "default": 1,
            },
            "fee": "fee"
        }
    },
    {
        "method": "GET",
        "uri": "/history/trades",
        "normalization_rules": {
            "timestamp": "timestamp",
            "assetName": "symbol",
            "type": "side",
            "quantity": "quantity",
            "price": "price",
            "fee": "fee"
        }
    }
]
