
// $(document).ready(function(){
//     console.log($("a").attr("target"))
//     $("h1").css("color","blue")

    // $("button").click(function(){
    //     $(".first").toggle(1000)
    // });
// $(document).ready(function(){
//     $("button").click(function(){
//         newText = $("#dib1").html("<p> hey there </p>");
//         console.log(newText)

//     })

// });

// function addition(number1, number2){
//     return number1 + number2
// }
// console.log(addition(20, 30))

// //  function = input name jodi number hoy tahole error dekhabe 
// function myfunction(){
//     var name = document.getElementById("nm").value ;
//     try {
//         if(isNaN(name) == false) throw "its a number";
//         else{
//             document.getElementById("p1").innerHTML = name;
//         }

//     }
    
//     catch(err) {
//         document.getElementById("p1").innerHTML = err;
//     }
// }
// var object1 = document.getElementById("dib1");
// console.log(object1);

$(document).ready(function(){
    $("#hideParagraphButton").on('click',function(){
        $("p").hide();
    })
})