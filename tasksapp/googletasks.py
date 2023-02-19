import os.path
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def auth():
	import pydata_google_auth
	scoped_credentials = pydata_google_auth.get_user_credentials(
		["https://www.googleapis.com/auth/tasks"],
		client_id="hoge-piyo.apps.googleusercontent.com",
		client_secret="hogehoge",
		credentials_cache=pydata_google_auth.cache.ReadWriteCredentialsCache(dirname=os.path.abspath("."), filename="pydata_google_credentials.json")
	)

def get_tasklist_ids():
	CRED_INFO = json.loads(os.getenv("CUSTOMCONNSTR_GOOGLE_TASKS_CRED_INFO", ""))
	creds = Credentials.from_authorized_user_info(
		info = CRED_INFO,
		scopes = ["https://www.googleapis.com/auth/tasks",],
	)

	try:
		service = build("tasks", "v1", credentials=creds)
		items = service.tasklists().list().execute().get("items", [])

		if not items:
			print("No tasklists found.")
			return

		print("tasklists:")
		for item in items:
			print(item["title"], item["id"])

	except HttpError as e:
		print(e)

def list_tasks():
	CRED_INFO = json.loads(os.getenv("CUSTOMCONNSTR_GOOGLE_TASKS_CRED_INFO", ""))
	TASK_LIST_ID = os.getenv("CUSTOMCONNSTR_GOOGLE_TASK_LIST_ID", "")
	creds = Credentials.from_authorized_user_info(
		info = CRED_INFO,
		scopes = ["https://www.googleapis.com/auth/tasks",],
	)

	try:
		service = build("tasks", "v1", credentials=creds)
		items = service.tasks().list(
			tasklist = TASK_LIST_ID,
			showCompleted = False,
			showDeleted = False,
		).execute().get("items", [])

		if not items:
			print("No tasks found.")
			return []

		items = sorted(items, key=lambda t: t["position"])

		return [{
			"title" : i["title"],
			"id" : i["id"],
			"notes" : i.get("notes", ""),
		} for i in items]

	except HttpError as e:
		print(e)

def insert_task(title):
	CRED_INFO = json.loads(os.getenv("CUSTOMCONNSTR_GOOGLE_TASKS_CRED_INFO", ""))
	TASK_LIST_ID = os.getenv("CUSTOMCONNSTR_GOOGLE_TASK_LIST_ID", "")
	creds = Credentials.from_authorized_user_info(
		info = CRED_INFO,
		scopes = ["https://www.googleapis.com/auth/tasks",],
	)

	try:
		service = build("tasks", "v1", credentials=creds)
		service.tasks().insert(
			body = {
				"kind": "tasks#task",
				"title": title,
				"notes": "",
			},
			tasklist = TASK_LIST_ID,
		).execute().get("items", [])

		return True

	except HttpError as e:
		print(e)
		return False

if __name__ == "__main__":
	# auth()
	[print(t) for t in list_tasks()]
	# insert_task("test ほげほげ")
