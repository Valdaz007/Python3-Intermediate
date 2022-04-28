import requests

def main():
	# Send a 'GET' Request to the Server
	data_set = requests.get("server-url")
	
	# Print Data to the Console
	print(data_set.json())

if __name__ == "__main__":
    main()
