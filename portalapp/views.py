import os
import json
from django.shortcuts import render

def index(request):
	bookmarks = os.getenv("CUSTOMCONNSTR_BOOKMARKS", False)
	if bookmarks:
		context = {"bookmarks": json.loads(bookmarks)}
	else:
		context = {"bookmarks": [
			{"title": "google", "url": "https://google.com", "show_url": "google.com"},
			{"title": "hidden", "url": "/calendar/2", "show_url": "/calendar/2"},
		]}

	for i in range(len(context["bookmarks"])):
		if context["bookmarks"][i]["url"].startswith("/"):
			context["bookmarks"][i]["url"] = request._current_scheme_host + context["bookmarks"][i]["url"]

	return render(
		request = request,
		template_name = 'portal.html',
		context = context)
