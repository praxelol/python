import requests
import tkinter as tk

# Define the API endpoint for scanning URLs
API_ENDPOINT = 'https://urlscan.io/api/v1/scan/'

# Define the function for scanning URLs
def scan_url(url):
    # Make the request to the API endpoint
    response = requests.post(API_ENDPOINT, json={'url': url})

    # Parse the response data
    data = response.json()

    # Return the scan results
    return data['data']

# Define the GUI
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('URL Scanner')

        # Create the URL entry field
        self.url_entry = tk.Entry(self)
        self.url_entry.pack(side='top')

        # Create the Scan button
        self.scan_button = tk.Button(self, text='Scan URL', command=self.on_scan)
        self.scan_button.pack(side='top')

        # Create the results text field
        self.results_text = tk.Text(self)
        self.results_text.pack(side='top')

    # Define the function for handling the Scan button click
    def on_scan(self):
        # Get the URL to scan from the entry field
        url = self.url_entry.get()

        # Scan the URL
        scan_results = scan_url(url)

        # Show the scan results in the results text field
        self.results_text.insert('end', str(scan_results))

# Run the app
app = App()
app.mainloop()
