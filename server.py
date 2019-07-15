from flask import Flask, request, jsonify
from endpoint_normalization_config import endpoints_config
from api_fetcher import TransactionsFetcher

app = Flask(__name__)


@app.route('/txs')
def txs():
    fetchers = []
    for each in endpoints_config:
        fetchers.append(TransactionsFetcher(**each).normalize())
    return jsonify(sum(fetchers, []))
