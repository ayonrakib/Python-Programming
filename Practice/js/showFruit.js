$(document).ready(function(){
    // jekono cross icon e click korle
    //      1. fruitline e ei object er id nibo
    //      2. ei object er parent er parent ke hide
    //      3. index hobe fruitline ke slice korbo "removeFruit" er por theke
    //      4. fruits[index] list theke delete
    //      5. log korbo fruits
    //      6. modifiedFruits ke abar empty banabo
    //      7. fruits er sob index er jonno:
    //          1. jodi currentIndex index er soman na hoy and fruits[currentIndex] empty na hoy:
    //              1. modifiedFruits e add korbo fruits[currentIndex]
    //      8. fruits hobe modifiedFruits er soman
    //      9. log korbo fruits
    //      10. showUpdatedFruits()
    $(document).on('click','i', function(){
        var fruitLine = $(this).attr('id');
        $(this).parent().parent().hide();
        var index = fruitLine.slice(11);
        delete fruits[index];
        console.log("After deleting: ",fruits);
        modifiedFruits = [];
        for(var currentIndex = 0; currentIndex < fruits.length; currentIndex++){
            if ((currentIndex != index) && (fruits[currentIndex] != undefined)){
                modifiedFruits.push(fruits[currentIndex]);
            }
        }
        
        fruits = modifiedFruits;
        console.log("the modified correct fruits list is: " + fruits);
        showUpdatedFruits();
    })
});

// addFruits
// input: none
// return: none
// method:
//      1. jodi fruit id er object er value empty string na hoy:
//          1. fruits e push korbo fruit id object er value
//          2. log korbo fruits
//          3. showUpdatedFruits()
function addFruit(){
    if($("#fruit").val() != ""){
        fruits.push($("#fruit").val());
        console.log("current fruit list: ",fruits);
        showUpdatedFruits();
    }
}

// showUpdatedFruits
// input: none
// return: none, just show updated fruits
// method:
//      1. fruitLine empty string
//      2. fruitlineNumber -1
//      3. fruits er sob index er jonno:
//          1. fruitLineNumber ++
//          1. fruitLine += fruitBlock + cross icon + fruits[index] block;
//      4. showFruits id er object e html akare boshabo fruitLine 
function showUpdatedFruits(){
    var fruitLine = "";
    var fruitLineNumber = -1;
    for(var index = 0; index < fruits.length; index++){
            fruitLineNumber += 1;
            fruitLine += getShowFruitBlock(fruitLineNumber) + getCrossIcon(index) + "<div>" + fruits[index] + getDivEnding() + getDivEnding();
    }
    $("#showFruits").html(fruitLine);
}

function getContainerHeader(){
    return `<div class = 'container'>`;
}

function getShowFruitBlock(fruitLineNumber){
    return `<div class = "showFruitBlock" id = "fruitLine${fruitLineNumber}">`;
}

function getCrossIcon(fruitLineNumber){
    return `<div>
                <i class="fa fa-window-close crossIcon" id = "removeFruit${fruitLineNumber}">
                </i>
            </div>`;
}

function getDivEnding(){
    return '</div>';
}

var fruits = [];

var modifiedFruits = [];