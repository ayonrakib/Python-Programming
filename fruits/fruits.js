$(document).ready(function(){
    // fruits empty list global var, made whenever dom is loaded
    // add fruits
    // input: none
    // return: none, just show fruits
    // method:
    //      1. addFruitButton button e click korle:
    //          1. fruitName er value nibo

    //          3. fruitName fruits e push
    //          4. log korbo current fruits list
    //          5. show fruits function call with fruits list as parameter
    var fruits = [];
    $("#addFruitButton").on('click',function(){
        var fruitName = $("#fruitName").val();
        fruits.push(fruitName);
        console.log("after adding fruit, current fruitlist is: ", fruits);
        // var fruitsLine = "";
        // for(var index = 0; index < fruits.length; index++){
        //     fruitsLine += getDivHeader("row") + getDivHeader("col-sm-1") + getCrossIcon(index) + getDivEnding() + getDivHeader("col-sm-11") + `${fruits[index]}` + getDivEnding() + getDivEnding();
        // }
        // $("#showFruitBlock").html(fruitsLine);
        showFruits(fruits);
    })
    // 1. document er icon e click korle:
    //      1. fruit index nibo element er id theke
    //      2. fruits list theke kete nibo ei index er fruit ta
    //      3. log korbo current fruit list
    //      4. showFruits function call korbo with fruits list as parameter
    $(document).on('click','i',function(){
        var fruitIndex = $(this).attr('id');
        fruits.splice(fruitIndex,1);
        console.log("after removing fruit, current fruit list is: ",fruits);
        // var fruitsLine = "";
        // for(var index = 0; index < fruits.length; index++){
        //     fruitsLine += getDivHeader("row") + getDivHeader("col-sm-1") + getCrossIcon(index) + getDivEnding() + getDivHeader("col-sm-11") + `${fruits[index]}` + getDivEnding() + getDivEnding();
        // }
        // $("#showFruitBlock").html(fruitsLine);
        showFruits(fruits);
    })
})

function getDivHeader(divClass){
    return `<div class = ${divClass}>`;
}

function getCrossIcon(fruitId){
    return `<i class="fas fa-times-circle" id = ${fruitId}></i>`;
}

function getDivEnding(){
    return `</div>`;
}

// showFruits
// input: fruits list
// return: nothing, just display fruits list
// method:
//      1. fruits line empty string
//      2. fruits er sob index er jonno:
//          1. fruits line e add korbo -> notun row banabo, first column e cross icon index id shoho and 2nd column e fruit name oi index e
//      3. show fruits block e html akare display korbo fruits line
function showFruits(fruits){
    var fruitsLine = "";
    for(var index = 0; index < fruits.length; index++){
        fruitsLine += getDivHeader("row") + getDivHeader("col-sm-1") + getCrossIcon(index) + getDivEnding() + getDivHeader("col-sm-11") + `${fruits[index]}` + getDivEnding() + getDivEnding();
    }
    $("#showFruitBlock").html(fruitsLine);
}