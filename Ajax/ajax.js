// $(document).ready(function(){
//     $("#changeText").click(function(){
//         $.ajax({url:"text/sampleText.txt", success: function(result){
//             $("#changeTextWithAjax").html(result);
//         }});
//     });
// });

$(document).ready(function(){
    $("#changeText").click(function(){
        $.ajaxSetup({url: "textfile", success: function(result){
            $("#changeTextWithAjax").html(result);
            console.log(result);
        }});
        $.ajax();
    })
})

// readystate = 1 -> pathaise kina
// 2 -> erokom kisu
// 3 -> erokom kisu
// 4 -> erokom kisu
// eita check korbo. 
// ready state -> request complete hoise kina eita 4 diye bujhay, 4 paile server er sathe connection off.
// this.status -> server er kase je request korsi, or response ta ki type. 200 hoile valid, 404 hoile server er kase response nai