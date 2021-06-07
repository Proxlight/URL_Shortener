function generateQRCode() {
	var data = document.getElementById("data").value
	eel.generate_qr(data)(setOutput)
}

function setOutput(outputText) {
	document.getElementById("output").value = outputText
}