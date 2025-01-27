from flask import Flask, request, jsonify
from oracles.arco_oracle import ArcoOracle
from deepseek_integration.deepseek_adapter import DeepSeekAdapter

app = Flask(__name__)

# Initialize components
oracle = ArcoOracle(blockchain_url="<BLOCKCHAIN_URL>", contract_address="<CONTRACT_ADDRESS>", abi="<CONTRACT_ABI>")
deepseek = DeepSeekAdapter(api_key="<DEEPSEEK_API_KEY>")

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    url = request.args.get('url')
    data = oracle.fetch_data(url)
    return jsonify(data)

@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.json.get('data')
    refined_data = deepseek.filter_data(data)
    return jsonify({"refined_data": refined_data})

@app.route('/store-data', methods=['POST'])
def store_data():
    key = request.json.get('key')
    value = request.json.get('value')
    private_key = request.json.get('private_key')
    tx_hash = oracle.send_to_chain(key, value, private_key)
    return jsonify({"transaction_hash": tx_hash.hex()})

if __name__ == '__main__':
    app.run(debug=True)