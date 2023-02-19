let delete_buttons = null;

window.addEventListener("load", () => {
	delete_buttons = [...document.getElementsByClassName("gt_delete_button")];

	delete_buttons.forEach(button => button.onclick = (event) => {
		console.log(event);
		delete_form = event.srcElement.form;
		const options = {
			method: "POST",
			body: new FormData(delete_form),
			credentials: 'include',
		};
		fetch("/gt/d", options).then((e) => {
			if(e.status === 200) {
				console.log(e.json());
				alert("200");
				document.getElementById("tasks_iframe").contentWindow.location.reload();
				return;
			}
			alert(e.status + " " + e.statusText);
		});
	});
});
