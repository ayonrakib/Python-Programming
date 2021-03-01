$(document).ready(function(){
    $("#removeFruit").click(function (){
        console.log("came in the click function");
        var parentFruitLineNumber = $(this).parent().attr('id');
        console.log(parentFruitLineNumber);
    });
    $("div").click(function(){
        console.log("clicked on div");
    })
});

function addFruit(){
    fruits.push($("#fruit").val());
    var fruitLine = "";
    var fruitLineNumber = -1;
    for(var index = 0; index < fruits.length; index++){
        fruitLineNumber += 1;
        fruitLine += getRowHeader(fruitLineNumber) + getColumnHeader(1) + getCrossIcon() + getDivEnding()  + getColumnHeader(11) + fruits[index] + getDivEnding() + getDivEnding();
    }
    $("#showFruits").html(fruitLine);
}

function getContainerHeader(){
    return `<div class = 'container'>`;
}

function getRowHeader(fruitLineNumber){
    return `<div class = "row" id="${fruitLineNumber}">`;
}

function getColumnHeader(columnWidth){
    return `<div class = "col-sm-${columnWidth}">`;
}

function getCrossIcon(){
    return `<i class="fa fa-window-close" id = "removeFruit"></i>`;
}

function getDivEnding(){
    return '</div>';
}

var fruits = [];

