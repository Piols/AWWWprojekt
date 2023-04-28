function init() {
	document.body.classList.add('dark_theme');
}

function change_theme() {
	if (document.body.classList.contains('dark_theme')) {
		document.body.classList.remove('dark_theme');
		document.body.classList.add('light_theme');
	} else {
		document.body.classList.remove('light_theme');
		document.body.classList.add('dark_theme');
	}
}
