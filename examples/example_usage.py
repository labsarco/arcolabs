from sdk.arco_sdk import ArcoSDK

sdk = ArcoSDK(api_url="http://localhost:5000")

# Fetch data
data = sdk.fetch_data("https://example.com/api/data")
print("Fetched Data:", data)

# Process data using DeepSeek
refined_data = sdk.process_data(data)
print("Refined Data:", refined_data)

# Store data on-chain
tx_hash = sdk.store_data(key="example_key", value="example_value", private_key="<PRIVATE_KEY>")
print("Transaction Hash:", tx_hash)