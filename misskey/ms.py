import os
import requests

MISSKEY_TOKEN = os.getenv("CUSTOMCONNSTR_MISSKEY_TOKEN")

def note(body=None):
	if not body:
		return False
	headers = {"Content-Type": "application/json"}
	json = {
		"i": MISSKEY_TOKEN,
		"text": body,
		# "visibility": "followers",
	}
	response = requests.post(
		"https://misskey.io/api/notes/create",
		headers = headers,
		json = json,
	)
	if "error" in response.json():
		print(response.json())
		return False
	return True
