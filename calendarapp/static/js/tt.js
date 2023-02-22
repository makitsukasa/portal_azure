let tt_form = null;
let tt_submit = null;

window.addEventListener("load", () => {
	tt_form = document.getElementById("tt");
	tt_submit = document.getElementById("tt_submit");

	tt_submit.onclick = () => {
		const options = {
			method: "POST",
			body: new FormData(tt_form),
			credentials: 'include',
		};
		fetch("/tt/p", options).then((e) => {
			if(e.status === 200) {
				console.log(e.json());
				document.getElementById("tt_text").value = "";
				return;
			}
			alert(e.status + " " + e.statusText);
		});
	};

	tt_text.onkeydown = (e) => {
		if (!e.ctrlKey) {
			if (e.keyCode === 13) {
				return false;
			}
			return true;
		}
		if (e.keyCode !== 13) {
			return true;
		}
		if (e.srcElement.value.length > 0) {
			tt_submit.dispatchEvent(new MouseEvent("click"));
		}
		return false;
	};
});
