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

function get_by_id(el_id) {
	return document.getElementById(el_id);
}

var currently_displayed = get_by_id('tab_default_content');

var tab_to_content = {};
tab_to_content['standard'] = get_by_id('tab_standard_content');
tab_to_content['optimization'] = get_by_id('tab_optimizations_content');
tab_to_content['processor'] = get_by_id('tab_processor_content');
tab_to_content['dependent'] = get_by_id('tab_dependent_content');

function change_tab(tab) {
	currently_displayed.style.display = "none";
	tab_to_content[tab.id].style.display = "";
	currently_displayed = tab_to_content[tab.id];
}

var select_processor = document.getElementById('Processor');

function update_dependent() {
	var selected_option = select_processor.value;
	var desc = get_by_id('dep_desc');
	var op1 = get_by_id('dep_op_1');
	var op2 = get_by_id('dep_op_2');
	var op3 = get_by_id('dep_op_3');
	switch (selected_option) {
		case "-mmcs51":
			desc.innerHTML = "Memory model:";
			op1.innerHTML = "Small";
			op1.value = "--model-small";
			op2.innerHTML = "Medium";
			op2.value = "--model-medium";
			op3.innerHTML = "Large";
			op3.value = "--model-large";
			break;
		case "-mz80":
			desc.innerHTML = "Z80 options:";
			op1.innerHTML = "Save BC";
			op1.value = "--callee-saves-bc";
			op2.innerHTML = "Reserve iy";
			op2.value = "--reserve-regs-iy";
			op3.innerHTML = "Never omit the frame pointer";
			op3.value = "--fno-omit-frame-pointer";
			break;
		case "-mstm8":
			desc.innerHTML = "Memory model:";
			op1.innerHTML = "Default";
			op1.value = "";
			op2.innerHTML = "Medium";
			op2.value = "--model-medium";
			op3.innerHTML = "Large";
			op3.value = "--model-large";
			break;
	}
}

select_processor.addEventListener('change', update_dependent());
update_dependent();