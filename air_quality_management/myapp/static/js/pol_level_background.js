var allTableCells = document.getElementsByTagName("td");
for(var i = 0, max = allTableCells.length; i < max; i++) {
    var node = allTableCells[i];

    var currentText = node.childNodes[0].nodeValue;


    if (currentText === "Very Good")
        node.style.backgroundColor = "#abd162";
    if (currentText === "Good")
        node.style.backgroundColor = "#f7d460";
    if (currentText === "Fair")
        node.style.backgroundColor = "#fc9956";
    if (currentText === "Bad")
        node.style.backgroundColor = "#f6676b";
    if (currentText === "Very Bad")
        node.style.backgroundColor = "#a37db8";
    if (currentText === "Hazardous")
        node.style.backgroundColor = "#a07684";

}