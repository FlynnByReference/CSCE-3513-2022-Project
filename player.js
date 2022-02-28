
function myFunction() {
  window.location.replace("splitPlayers.html")
}

function myPlayers(form){
  var redPlayerFirstName1 = form.redf1.value;
  var redPlayerLastName1 = form.redl1.value;
  var redPlayerCodeName1 = form.redc1.value;
  // var redPlayer2 = form.red2.value;
  // var redPlayer3 = form.red3.value;
  // var redPlayer4 = form.red4.value;
  // var redPlayer5 = form.red5.value;
  var greenPlayerFirstName1 = form.greenf1.value;
  var greenPlayerLastName1 = form.greenl1.value;
  var greenPlayerCodeName1 = form.greenc1.value;
  var javaScriptData = {
    firstName: redPlayerFirstName1,
    lastName: redPlayerLastName1,
    codeName: redPlayerCodeName1
  };

  test = new XMLHttpRequest();
  test.open("POST", '/submit', true)

  test.onload = function(){
      var dataSend = JSON.parse(this.responseText)
  };
  JSON.stringify(javaScriptData)


  console.log(javaScriptData);
  sendData = JSON.stringify(javaScriptData)
  test.send(sendData)
  // console.log(redPlayerLastName1);
  // console.log(redPlayerCodeName1);

  // console.log(greenPlayerFirstName1);
  // console.log(greenPlayerLastName1);
  // console.log(greenPlayerCodeName1);

}