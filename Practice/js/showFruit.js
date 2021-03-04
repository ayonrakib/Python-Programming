$(document).ready(function(){
    $("#removeFruit").on("click",function (){
        console.log("came in the click function of removeFruit id block");
        var parentFruitLineNumber = $(this).parent().attr('id');
        console.log(parentFruitLineNumber);
    })
    // $('i').on('click',function (){
    //     console.log($(this).attr('id'));
    // })
    $(document).on('click','i', function(){
        console.log($(this).attr('id'));
    })
});



// function removeFruitLine(){
//     console.log($(this).attr('id'));
// }

function addFruit(){
    if($("#fruit").val() != ""){
        fruits.push($("#fruit").val());
        var fruitLine = "";
        var fruitLineNumber = -1;
        for(var index = 0; index < fruits.length; index++){
            fruitLineNumber += 1;
            fruitLine += getShowFruitBlock(fruitLineNumber) + getCrossIcon(index) + "<div>" + fruits[index] + getDivEnding() + getDivEnding();
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

