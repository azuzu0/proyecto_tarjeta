// var tarjeta = document.getElementById("tarjeta");
// var lector = document.getElementById("lector");

// tarjeta.addEventListener("dragstart", function(e) {
// 	e.dataTransfer.setData("text", e.target.id);
// });

// lector.addEventListener("dragover", function(e) {
// 	e.preventDefault();
// });

// lector.addEventListener("drop", function(e) {
// 	e.preventDefault();
// 	var data = e.dataTransfer.getData("text");
// 	if (data == "tarjeta") {
// 		lector.innerHTML = "OK";
// 	}
// });

// function enviarOK() {
// 	var xhr = new XMLHttpRequest();
// 	xhr.open("POST", "/", true);
// 	xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
// 	xhr.send(JSON.stringify({ mensaje: "OK" }));
//   }

var tarjeta = document.getElementById("tarjeta");
var lector = document.getElementById("lector");
var numeroInput = document.getElementById("numeroInput");

tarjeta.addEventListener("dragstart", function(e) {
	e.dataTransfer.setData("text", e.target.id);
});

lector.addEventListener("dragover", function(e) {
	e.preventDefault();
});

lector.addEventListener("drop", function(e) {
	e.preventDefault();
	var data = e.dataTransfer.getData("text");
	if (data == "tarjeta") {
		var numero = document.getElementById("numero").value;
		lector.innerHTML = numero;
		numeroInput.value = numero;
	}
});
