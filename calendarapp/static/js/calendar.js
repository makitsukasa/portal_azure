let today = null;
let clockElements = [];

function updateClock () {
	let currentTime = new Date();
	// console.log(`updateclock() ${currentTime.getHours()}:${currentTime.getMinutes()}:${currentTime.getSeconds()}.${currentTime.getMilliseconds()}`);

	let YYYY = currentTime.getFullYear();
	let MM = (" " + (currentTime.getMonth() + 1)).slice(-2);
	let DD = (" " + currentTime.getDate()).slice(-2);
	let WWW = ["日", "月", "火", "水", "木", "金", "土"][currentTime.getDay()];
	let HH = (" " + currentTime.getHours()).slice(-2);
	let mm = ("0" + currentTime.getMinutes()).slice(-2);

	let MM_DD = MM + "/" + DD;

	if (clockElements[1].innerHTML != MM_DD) {
		if (WWW == "日") {
			document.location.reload();
		} else {
			showCalendar();
		}
	}

	clockElements[0].innerHTML = YYYY + "/";
	clockElements[1].innerHTML = MM_DD;
	clockElements[2].innerHTML = "(" + WWW + ") ";
	clockElements[3].innerHTML = HH + ":" + mm;

	let ms = currentTime.getSeconds() * 1000 + currentTime.getMilliseconds();
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
	today = new Date();
	clockElements = [
		document.getElementById("clock_year"),
		document.getElementById("clock_date"),
		document.getElementById("clock_dayofweek"),
		document.getElementById("clock_time"),
	];
	let cells = document.getElementsByClassName("cell");
	let date = getWeek0WedDate();
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

window.addEventListener("load", () => {
	showCalendar();
	updateClock();
});
