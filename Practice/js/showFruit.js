$(document).ready(function(){
    // jekono cross icon e click korle
    //      1. ei object er attribute id read korbo
    //      2. ei object er parent er parent ke hide
    //      3. id attribute ke slice korbo and fruitLine er por sob read korbo, oitai hobe index jeita delete korte hobr
    //      4. fruits[index] delete
    //      5. log korbo current fruits
    $(document).on('click','i', function(){
        var fruitLine = $(this).attr('id');
        $(this).parent().parent().hide();
        var index = fruitLine.slice(11);
        delete fruits[index];
        console.log("After deleting",fruits);
    })
});



// function removeFruitLine(){
//      1. jodi fruit id er value empty string na hoy:
//          1. fruits e add fruit id er value
//          2. log korbo current fruit list
//          3. fruitLine empty string
//          4. fruitLineNumber hobe -1
//          5. fruits.length porjonto iterate 0th index theke:
//              1. jodi fruits er current element undefined na hoy:
//                  1. fruitLineNumber ++
//                  2. fruitLineBanabo with cross icon and current fruits indexed string
//          6. showFruits id te fruitLine html akare boshabo
function addFruit(){
    if($("#fruit").val() != ""){
        fruits.push($("#fruit").val());
        console.log("current fruit list: ",fruits);
        var fruitLine = "";
        var fruitLineNumber = -1;
        for(var index = 0; index < fruits.length; index++){
            if(fruits[index] != undefined){
                fruitLineNumber += 1;
                fruitLine += getShowFruitBlock(fruitLineNumber) + getCrossIcon(index) + "<div>" + fruits[index] + getDivEnding() + getDivEnding();
            }
        }
        $("#showFruits").html(fruitLine);
    }
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

