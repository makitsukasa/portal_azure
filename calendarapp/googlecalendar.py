import os
import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_events(todaystr = None, show_hidden = False):
	gapi_creds = Credentials.from_service_account_info(
		{
			"private_key": os.getenv("CUSTOMCONNSTR_GOOGLE_PRIVATE_KEY", "").replace('\\n', '\n'),
	 		"client_email": os.getenv("CUSTOMCONNSTR_GOOGLE_CLIENT_EMAIL", ""),
			"token_uri": os.getenv("CUSTOMCONNSTR_GOOGLE_TOKEN_URI", "")
		},
		scopes=[
			"https://www.googleapis.com/auth/calendar",
		]
	)

	service = build("calendar", "v3", credentials=gapi_creds)

	if not todaystr:
		today = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).replace(
			hour=0, minute=0, second=0, microsecond=0)
	else:
		today = datetime.datetime.fromisoformat(todaystr).replace(
			hour=0, minute=0, second=0, microsecond=0)

	date_min = today - datetime.timedelta(days=today.isoweekday() % 7 + 4)
	date_max = date_min + datetime.timedelta(days=38, hours=23, minutes=59, seconds=59)

	try:
		events = service.events().list(
			calendarId=os.getenv("CUSTOMCONNSTR_GOOGLE_CALENDAR_ID"),
			timeMin=f"{date_min.isoformat()}Z",
			timeMax=f"{date_max.isoformat()}Z",
			singleEvents=True,
			orderBy="startTime",
		).execute()
		holyday_events = service.events().list(
			calendarId=os.getenv("CUSTOMCONNSTR_GOOGLE_HOLIDAY_CALENDAR_ID"),
			timeMin=f"{date_min.isoformat()}Z",
			timeMax=f"{date_max.isoformat()}Z",
			singleEvents=True,
			orderBy="startTime",
		).execute()
	except Exception as e:
		print(type(e))
		print(e)
		print(e.content)
		return {}
	else:
		events = [
			{
				"date" : datetime.date.fromisoformat(e["start"]["date"]),
				"summary" :
					"-" if (e.get("colorId", "0") not in ["0", "4"]) else e.get("summary", "-"),
				"color" : e.get("colorId", "0"),
			} for e in events["items"]
		] + [
			{
				"date" : datetime.date.fromisoformat(e["start"]["date"]),
				"summary" : e.get("summary", "-"),
				"color" : e.get("colorId", "4"),
			} for e in holyday_events["items"]
		]

		ret = {"day" + str(i): "" for i in range(39)}
		for i in range(39):
			date = datetime.date.fromisoformat(
				(date_min + datetime.timedelta(days=i)).isoformat()[:10])
			events_today = list(filter(lambda e: e["date"] == date, events))
			# print(date.isoformat(), ":" , len(events_today), "schedules")
			# [print(e) for e in events_today]
			ret["day" + str(i)] = [{
				"color" : e["color"],
				"summary" : e["summary"],
			} for e in events_today]
		return ret


def insert_event(summary, date, color = 0):
	gapi_creds = Credentials.from_service_account_info(
		{
			"private_key": os.getenv("CUSTOMCONNSTR_GOOGLE_PRIVATE_KEY", "").replace('\\n', '\n'),
	 		"client_email": os.getenv("CUSTOMCONNSTR_GOOGLE_CLIENT_EMAIL", ""),
			"token_uri": os.getenv("CUSTOMCONNSTR_GOOGLE_TOKEN_URI", "")
		},
		scopes=[
			"https://www.googleapis.com/auth/calendar",
		]
	)

	try:
		service = build("calendar", "v3", credentials=gapi_creds)

		service.events().insert(
			calendarId=os.getenv("CUSTOMCONNSTR_GOOGLE_CALENDAR_ID"),
			body={
				"summary": summary,
				"start": {"date": date},
				"end": {"date": date},
				"colorId": color,
			}
		).execute()

		return True

	except HttpError as e:
		print(e)
		return False

if __name__ == '__main__':
	# get_events()
	# [print(d, e) for d, e in get_events(show_hidden=True).items()]
	# [print(d, e) for d, e in get_events("2023-03-05", show_hidden=True).items()]
	# [print(e) for e in get_events("2023-02-01")]

	# insert_event("さまり", "2023-04-05")
	insert_event("さまり", "2023-04-05", 2)
	# insert_event("さまり", "2023-04-05", 4)
