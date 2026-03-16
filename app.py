import requests

def check_server(url):
	try:
		response = requests.get(url, timeout=5)
		return response.status_code == 200
	except:
		return False

def main():
	with open("servers.txt") as file:
		servers = file.readlines()

	for server in servers:
		server = server.strip()
		if check_server(server):
			print(f"{server} - ONLINE")
		else:
			print(f"{server} - OFFLINE")

if __name__ == "__main__":
	main()