var city = localStorage.city || 'shanghai';
document.getElementById('city').value = city;
document.getElementById('save').onclick = function() {
	localStorage.city = document.getElementById('city').value;
	alert("save success");
}