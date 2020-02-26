function getLength() {
	var sequence = document.getElementById("seq");
	var string=sequence.value;
	var out = "";
	var lines =[];
	lines = string.split("\n");
	for (var i=0; i< lines.length; i++){
		if (lines[i][0]==">"){
			out+=lines[i]+" ";
		} else{
			out += lines[i].length + "\n";
		}
	}
	alert(out)
}
