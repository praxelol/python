# Import the necessary libraries
import requests

# Make a GET request to the specified URL and store the response
response = requests.get("https://animechan.vercel.app/api/random")

# If the request was successful, get the JSON data from the response
if response.status_code == 200:
  quote = response.json()
  print(quote)
else:
  # If the request failed, print an error message
  print("Failed to get quote:", response.status_code)
