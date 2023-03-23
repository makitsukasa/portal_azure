let gc_form = null;
let gc_submit = null;

window.addEventListener("load", () => {
	gc_form = document.getElementById("gc");
	gc_submit = document.getElementById("gc_submit");
	gc_text = document.getElementById("gc_text");

	gc_submit.onclick = () => {
		gc_submit.value = "✓";
		const options = {
			method: "POST",
			body: new FormData(gc_form),
			credentials: 'include',
		};
		fetch("/calendar/p", options).then((e) => {
			if(e.status === 200) {
				console.log(e.json());
				document.getElementById("gc_text").value = "";
				document.getElementById("gc_date").value = "";
				gc_submit.value = "submit";
				document.location.reload();
				return;
			}
			alert(e.status + " " + e.statusText);
		});
	};

	gc_text.onkeydown = (e) => {
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
			gc_submit.dispatchEvent(new MouseEvent("click"));
		}
		return false;
	};
});
