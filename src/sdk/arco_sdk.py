class ArcoSDK:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, url):
        response = requests.get(f"{self.api_url}/fetch-data", params={"url": url})
        return response.json()

    def process_data(self, data):
        response = requests.post(f"{self.api_url}/process-data", json={"data": data})
        return response.json()

    def store_data(self, key, value, private_key):
        response = requests.post(f"{self.api_url}/store-data", json={
            "key": key,
            "value": value,
            "private_key": private_key
        })
        return response.json()