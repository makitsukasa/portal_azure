let gt_form = null;
let gt_submit = null;

window.addEventListener("load", () => {
	gt_form = document.getElementById("gt");
	gt_submit = document.getElementById("gt_submit");
	gt_text = document.getElementById("gt_text");

	gt_submit.onclick = () => {
		const options = {
			method: "POST",
			body: new FormData(gt_form),
			credentials: 'include',
		};
		fetch("/gt/p", options).then((e) => {
			if(e.status === 200) {
				console.log(e.json());
				document.getElementById("gt_text").value = "";
				document.getElementById("tasks_iframe").contentWindow.location.reload();
				return;
			}
			alert(e.status + " " + e.statusText);
		});
	};

	gt_text.onkeydown = (e) => {
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
			gt_submit.dispatchEvent(new MouseEvent("click"));
		}
		return false;
	};
});
