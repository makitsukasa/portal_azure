import googleapiclient.discovery
import google.auth
import datetime
import sys
if __name__ == '__main__':
	sys.path.append(".")
	import keys
else:
	from . import keys

def filter_func(event, date, show_hidden = False):
	if show_hidden:
		return event["date"] == date
	else:
		return event["date"] == date and (event["color"] in ["0", "6"])

def get_events(todaystr = None):
	gapi_creds = google.auth.load_credentials_from_file(
		keys.JSON_FILENAME,
		[
			# "https://www.googleapis.com/auth",
			"https://www.googleapis.com/auth/calendar",
		],
	)[0]

	service = googleapiclient.discovery.build("calendar", "v3", credentials=gapi_creds)

	if not todaystr:
		today = datetime.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
	else:
		today = datetime.datetime.fromisoformat(todaystr).replace(
			hour=0, minute=0, second=0, microsecond=0)

	date_min = today - datetime.timedelta(days=today.isoweekday() % 7 + 4)
	date_max = date_min + datetime.timedelta(days=38, hours=23, minutes=59, seconds=59)

	try:
		events = service.events().list(
			calendarId=keys.CALENDAR_ID,
			timeMin=f"{date_min.isoformat()}Z",
			timeMax=f"{date_max.isoformat()}Z",
			singleEvents=True,
			orderBy="startTime",
		).execute()
		holyday_events = service.events().list(
			calendarId=keys.HOLIDAY_CALENDAR_ID,
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
		events = [{
			"date" : datetime.date.fromisoformat(e["start"]["date"]),
			"summary" : e["summary"],
			"color" : e.get("colorId", "0"),
		} for e in events["items"]] + [{
			"date" : datetime.date.fromisoformat(e["start"]["date"]),
			"summary" : e["summary"],
			"color" : e.get("colorId", "6"),
		} for e in holyday_events["items"]]

		ret = {"day" + str(i): "" for i in range(39)}
		for i in range(39):
			date = datetime.date.fromisoformat(
				(date_min + datetime.timedelta(days=i)).isoformat()[:10])
			events_today = list(filter(lambda e: filter_func(e, date), events))
			# print(date.isoformat(), ":" , len(events_today), "schedules")
			# [print(e) for e in events_today]
			ret["day" + str(i)] = [{
				"color" : e["color"],
				"summary" : e["summary"],
			} for e in events_today]
		return ret

if __name__ == '__main__':
	# get_events()
	[print(e) for e in get_events()]
	# [print(e) for e in get_events("2023-02-01")]
