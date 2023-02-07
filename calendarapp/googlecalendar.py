import googleapiclient.discovery
import google.auth
import datetime
from calendar import monthrange
import sys
if __name__ == '__main__':
	sys.path.append(".")
	import keys
else:
	from . import keys
from pprint import pprint

def get_events():

	scopes = [
		# "https://www.googleapis.com/auth",
		"https://www.googleapis.com/auth/calendar"
	]

	gapi_creds = google.auth.load_credentials_from_file(
		keys.JSON_FILENAME,
		scopes,
	)[0]

	service = googleapiclient.discovery.build("calendar", "v3", credentials=gapi_creds)

	utcnow = datetime.datetime.utcnow()
	time_min = datetime.datetime(utcnow.year, utcnow.month, 1, 0, 0, 0)

	time_max = datetime.datetime(utcnow.year, utcnow.month,
		monthrange(utcnow.year, utcnow.month)[1], 23, 59, 59)
	try:
		events = service.events().list(
			calendarId=keys.CALENDAR_ID,
			timeMin=f"{time_min.isoformat()}Z",
			timeMax=f"{time_max.isoformat()}Z",
			singleEvents=True,
			orderBy="startTime",
		).execute()
	except Exception as e:
		print(type(e))
		print(e)
		print(e.content)
	else:
		print(events)
		return events

if __name__ == '__main__':
	get_events()
