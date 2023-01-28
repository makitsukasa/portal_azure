const today = new Date();
let clockElement = null;

function updateClock () {
	var currentTime = new Date();
	// console.log(`updateclock() ${currentTime.getHours()}:${currentTime.getMinutes()}:${currentTime.getSeconds()}.${currentTime.getMilliseconds()}`);

	var YYYY = currentTime.getFullYear();
	var MM = (" " + (currentTime.getMonth() + 1)).slice(-2);
	var DD = (" " + currentTime.getDate()).slice(-2);
	var WWW = ["日", "月", "火", "水", "木", "金", "土"][currentTime.getDay()];
	var HH = (" " + currentTime.getHours()).slice(-2);
	var mm = ("0" + currentTime.getMinutes()).slice(-2);
	clockElement.innerHTML = `<span class="small">${YYYY}/</span><span>${MM}/${DD}</span><span class="small">(${WWW}) </span><span>${HH}:${mm}</span>`;

	if (HH == " 0" && mm == "00") {
		showCalendar();
	}
	var ms = currentTime.getSeconds() * 1000 + currentTime.getMilliseconds();
	setTimeout(updateClock, 60000 - ms);
 }

function isToday (date) {
	return date.getFullYear() === today.getFullYear() &&
		date.getMonth() === today.getMonth() &&
		date.getDate() === today.getDate();
}

function getWeek0WedDate () {
	// カレンダーは今週を1週目としたときの0週目の水曜日から
	const date = new Date();
	date.setDate(date.getDate() - date.getDay() - 4);
	return date;
}

function getDateStr (date, month = false) {
	if (month) {
		return (date.getMonth() + 1) + "/" + date.getDate();
	}
	return "" + date.getDate();
}

function showCalendar () {
	clockElement = document.getElementById("clock");
	var cells = document.getElementsByClassName("cell");
	var date = getWeek0WedDate();
	for (let i = 0; i < cells.length; i++) {
		let nextDate = new Date(date);
		nextDate.setDate(date.getDate() + 1);
		// 月を表示するのは0週目の水曜日か
		// 5週目の土曜日か
		// 月初か
		// 月末か
		// 当日のとき
		let month = cells[i].id == 'week0Wed' ||
			cells[i].id == 'week5Sat' ||
			date.getDate() == 1 ||
			nextDate.getDate() == 1 ||
			isToday(date);

		cells[i].querySelector(":scope > .dateStr").innerHTML = getDateStr(date, month);

		if (isToday(date)) {
			cells[i].classList.add("today");
		} else {
			cells[i].classList.remove("today");
		}

		date = nextDate;
	}
}

function init() {
	showCalendar();
	updateClock();
}

window.addEventListener("load", init);
