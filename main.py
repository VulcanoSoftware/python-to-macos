import requests

url = 'https://raw.githubusercontent.com/VulcanoSoftware/ets2-setup-tool/refs/heads/main/config.cfg'
bestandspad = 'config.cfg'
response = requests.get(url)
print(response)
