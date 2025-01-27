import requests
from web3 import Web3

class ArcoOracle:
    def __init__(self, blockchain_url, contract_address, abi):
        self.web3 = Web3(Web3.HTTPProvider(blockchain_url))
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)

    def fetch_data(self, data_source_url):
        response = requests.get(data_source_url)
        if response.status_code == 200:
            return response.json()
        raise Exception("Failed to fetch data from source")

    def send_to_chain(self, key, value, private_key):
        account = self.web3.eth.account.privateKeyToAccount(private_key)
        tx = self.contract.functions.storeData(key, value).buildTransaction({
            'from': account.address,
            'nonce': self.web3.eth.getTransactionCount(account.address)
        })
        signed_tx = self.web3.eth.account.signTransaction(tx, private_key)
        return self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)