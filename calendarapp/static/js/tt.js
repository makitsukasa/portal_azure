let mn_form = null;
let mn_submit = null;

window.addEventListener("load", () => {
	mn_form = document.getElementById("mn");
	mn_submit = document.getElementById("mn_submit");

	mn_submit.onclick = () => {
		mn_submit.value = "✓";
		const options = {
			method: "POST",
			body: new FormData(mn_form),
			credentials: 'include',
		};
		fetch("/mn/n", options).then((e) => {
			if(e.status === 200) {
				console.log(e.json());
				document.getElementById("mn_text").value = "";
				mn_submit.value = "submit";
				return;
			}
			alert(e.status + " " + e.statusText);
		});
	};

	mn_text.onkeydown = (e) => {
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
			mn_submit.dispatchEvent(new MouseEvent("click"));
		}
		return false;
	};
});
