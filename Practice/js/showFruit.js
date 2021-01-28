// js document ready function
// input: function definition
// return: whatever i write in JS
// method: submitButton id ete click:
//      input: function definition
//      return:  column e fruit name show korbe with cross icon
//      method:
//          fruits list e push fruitName id er value
//          fruit ""
//          id 0
//          fruits length porjonto iterate 0 index theke:
//              fruit += getFruitLineHeader() + getFruitLineHeaderId(id) + getCrossIconheader() + getCrossIcon() + getCrossIconFooter() + getFruitNameHeader() +  fruits[index] + getFruitNameFooter()  + getFruitLineFooter();
//              id ++
//          fuitBlock er innerhtml = fruit
//      method: hideFruit
//      input: function definition
//      return: nothing, just hide() that row
//      method:
//          

// document.ready jei function ta input nise, oi function tar block konta


// $(document).ready() ekta function

// kisu event ase jeita user event raise kore, jemon onclick, onkeyup onkeydown-interface diye ja kisu kori, user event toiri kore.
// ar kisu event ase jeigula browser raise kore-kisu event code raise kore. ekta event arekta event raise korte paare.
// browser raise event-johkon ekta werbpage r sob resource(js,css etc.) load hoy, tokhon event load hoy-browser specific event.
// $(document).ready()-ekta function input nicche, eibar document er je loading event raise kore-shei event er sathe ei function attach kore
// jokhon e page load hobe(DOM banabe), tokhon e onclick expression -> onclick="showFruit()" -> evaluate hobe
// expression evaluate howa mane - click event er sathe showFruit() function ta attach korbe
// attach kora mane ->  eventToFunction = {"submitButtonId-click":[]} ->
// ei dictionary te key er value te jei list ase, oitar element hishabe function showFruit() append korbe, so:
// eventToFunction = {"submitButtonId-click":[showFruit()]}


// eikhane, js file load howar sathe sathe ready() function ta call korbe
// window.load type event er sathe ready() function ta attach korbe -> jquery kohkoni function chalaite parbe na
// ami browser ke bole dei tumi ei kaaj ta ei time e koiro-jokhon sob load shesh hobe, tokhon ei function chalaba
// tumi ei kaaj ta ei time e koiro-eitar mane hocche event er sathe function ta attach koro and ekta dict er value te append
// ready functione r uddessho hoilo-onload er event e attach korbe
// kon event e kon function cholbe-eita JS JQuery chalaite parbe na, bole dite parbe konta kokhon cholbe
// ei chalanor kaaj ta browser chalabe
$(document).ready(function(){
    $("#submitButton").click(function(){
        fruits.push(document.getElementById("fruitName").value);
        var fruitLineWithCrossIcon = "";
        var id = 1;
        // console.log(fruits); 
        for(var index = 0; index < fruits.length;index++){
            fruitLineWithCrossIcon += getFruitLineHeader() + getFruitLineHeaderId(id) + getCrossIconheader(id) + getCrossIcon() + getCrossIconFooter() + getFruitNameHeader() +  fruits[index] + getFruitNameFooter()  + getFruitLineFooter();
            id += 1;
        };
        document.getElementById("fruitBlock").innerHTML = fruitLineWithCrossIcon;
    });
    $(`#cross${id}`).click(function(){
        // $("#hideElement").hide();
        alert("Clicked cross");
    });
    $(`${id}`).click
});

function getFruitLineHeader(){
    return "<div class = 'fruitLine row'";
}

function getFruitLineHeaderId(id){
    return `id = line${id}>`;
}

function getCrossIconheader(id){
    return `<div class = 'crossIcon col-sm-1' id =cross${id}>`;
}

function getCrossIcon(){
    return "<i class='fa fa-times'></i>";
}

function getCrossIconFooter(){
    return "</div>";
}

function getFruitNameHeader(){
    return "<div class = 'fruitNameBlock col-sm-11'>";
}

function getFruitNameFooter(){
    return "</div>";
}

function getFruitLineFooter(){
    return "</div>";
}

var fruits = [];

