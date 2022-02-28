
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
    // var javaScriptData = {
    //   firstName: redPlayerFirstName1,
    //   lastName: redPlayerLastName1,
    //   codeName: redPlayerCodeName1
    // };
    // const name = require('name');
    // const object = JSON.stringify(javaScriptData);

    // name.writeFile('players.json', object);
    // var greenPlayer2 = form.green2.value;
    // var greenPlayer3 = form.green3.value;
    // var greenPlayer4 = form.green4.value;

    // var description = document.getElementById('description');
    // fetch('/test')
    //   .then(function (response) {
    //     return response.json();
    //   }).then(function(text) {
    //     console.log('GET response:');
    //     console.log(text.greeting);
    //   });
    var javaScriptData;
    var testvar = new XMLHttpRequest();
    testvar.onreadystatechange = 
    $.ajax({
      type: 'POST',
      javaScriptData: {
        first : redPlayerFirstName1,
        last : redPlayerLastName1,
        code : redPlayerCodeName1},
        success : function (response) {},
        error : function (response) {}
    })

  // $.post("/postMethod", {
  //   javaScriptData: data
  // });
      

    console.log(javaScriptData);
    // console.log(redPlayerLastName1);
    // console.log(redPlayerCodeName1);

    // console.log(greenPlayerFirstName1);
    // console.log(greenPlayerLastName1);
    // console.log(greenPlayerCodeName1);

    
}



// (function() {
//     ("form input").keypress(function (e) {
//         if ((e.which && e.which == 13) || (e.keyCode && e.keyCode == 13)) {
//             ('button[type=submit] .default').click();
//             return false;
//         } else {
//             return true;
//         }
//     });
// });