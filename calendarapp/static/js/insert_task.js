let gt_form = null;
let gt_submit = null;

window.addEventListener("load", () => {
	gt_form = document.getElementById("gt");
	gt_submit = document.getElementById("gt_submit");

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
});
