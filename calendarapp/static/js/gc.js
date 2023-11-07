let gc_form = null;
let gc_submit_p = null;

function fillForm (id, color, text, datestr){
	document.getElementById("gc_color").value = color;
	document.getElementById("gc_text").value = text;
	document.getElementById("gc_date").value = datestr;
	document.getElementById("gc_id").value = id;
	if (id.length == 0) {
		document.getElementById("gc_id").type = "hidden";
	} else {
		document.getElementById("gc_id").type = "text";
	}
}

window.addEventListener("load", () => {
	gc_form = document.getElementById("gc");
	gc_submit_c = document.getElementById("gc_submit_c");
	gc_submit_u = document.getElementById("gc_submit_u");
	gc_submit_d = document.getElementById("gc_submit_d");
	gc_text = document.getElementById("gc_text");

	gc_submit_c.onclick = () => {
		gc_submit_c.value = "⏳";
		const options = {
			method: "POST",
			body: new FormData(gc_form),
			credentials: 'include',
		};
		fetch("/calendar/c", options).then((e) => {
			if(e.status === 200) {
				console.log(e.json());
				document.getElementById("gc_text").value = "";
				document.getElementById("gc_date").value = "";
				gc_submit_c.value = "⌛";
				document.location.reload();
				return;
			}
			alert(e.status + " " + e.statusText);
		});
	};

	gc_submit_u.onclick = () => {
		gc_submit_u.value = "⏳";
		const options = {
			method: "POST",
			body: new FormData(gc_form),
			credentials: 'include',
		};
		fetch("/calendar/u", options).then((e) => {
			if(e.status === 200) {
				console.log(e.json());
				document.getElementById("gc_text").value = "";
				document.getElementById("gc_date").value = "";
				gc_submit_u.value = "⌛";
				document.location.reload();
				return;
			}
			alert(e.status + " " + e.statusText);
		});
	};

	gc_submit_d.onclick = () => {
		gc_submit_d.value = "⏳";
		const options = {
			method: "POST",
			body: new FormData(gc_form),
			credentials: 'include',
		};
		fetch("/calendar/d", options).then((e) => {
			if(e.status === 200) {
				console.log(e.json());
				document.getElementById("gc_text").value = "";
				document.getElementById("gc_date").value = "";
				gc_submit_d.value = "⌛";
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
			gc_submit_p.dispatchEvent(new MouseEvent("click"));
		}
		return false;
	};
});
