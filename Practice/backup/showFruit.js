function showFruits(){
    var fruit = document.getElementById("fruit").value;
    fruits.push(fruit);
    console.log(fruits);
    var currentFruit = "";
    var fruitLineNumber = 0;
    // document.getElementById('fruitList').innerHTML = fruits;
    for (var index = 0; index < fruits.length; index++){
        if (fruits[index] != undefined){
            currentFruit = currentFruit + fruitLineOpeningDiv() + fruitLineNumber + fruitLineOpeningDivSymbol() + 
                           crossIcon(fruitLineNumber) + fruitNameDivOpener() + fruits[index] + fruitNameDivEnding() + fruitLineEndingDiv() + lineBreak();
            fruitLineNumber = fruitLineNumber + 1;
        }
    }
    document.getElementById('fruitList').innerHTML = currentFruit;
}

function fruitLineOpeningDiv(){
    return "<div id ="
}

function fruitLineOpeningDivSymbol(){
    return ">"
}

function crossIcon(fruitLineNumber){
    return `
    <div id = "crossIcon" onclick = "removeFruit(${fruitLineNumber})">
        <i class="fa fa-times-circle"></i>
    </div>`;
}

function fruitNameDivOpener(){
    return "<div id = 'fruitName'>"
}

function fruitNameDivEnding(){
    return "</div>"
}

function fruitLineEndingDiv(){
    return '</div>'
}

function lineBreak(){
    return `
    <div>
    </div>`;
}

function removeFruit(fruitLineNumber){
    delete fruits[fruitLineNumber];
    document.getElementById(fruitLineNumber).innerHTML = "";
    console.log(fruits[fruitLineNumber]);
}
// submit "f"
// 1. var fruit = document.getElementById("fruit").value;
// 2. var fruit = "f"
// 3. fruits.push(fruit);
// 4. fruits.push("f");
// 5. fruits = ['f'];
// 6. console.log(fruits);
// 7. console.log(["f"]);
// 8. loop 1:
//  9. index = 0, index < 1; true
//      10. currentFruit = currentFruit + fruits[index];
//      11. currentFruit = "" + fruits[index];
//      12. currentFruit = "" + fruits[0];
//      13. currentFruit = "" + "f";
//      14. currentFruit = "f";
// document.getElementById('fruitList').innerHTML = currentFruit;
// document.getElementById('fruitList').innerHTML = "f";
// 15. submit "a"
// 16. var fruit = document.getElementById("fruit").value;
// 17. var fruit = "a";
// 18. fruits.push(fruit);
// 19. fruits.push("a");
// 20. fruits = ['f','a'];
// 21. console.log(fruits);
// 22. console.log(["f","a");
//  loop 1:
//  23. index = 0, index < 2; true
//      24. currentFruit = currentFruit + fruits[index];
//      25. currentFruit = "" + fruits[index];
//      26. currentFruit = "" + fruits[0];
//      27. currentFruit = "" + "f";
//      28. currentFruit = "f";
//  loop 2:
//  23. index = 1, index < 2; true
//      24. currentFruit = currentFruit + fruits[index];
//      25. currentFruit = "f" + fruits[index];
//      26. currentFruit = "f" + fruits[1];
//      27. currentFruit = "f" + "a";
//      28. currentFruit = "fa";
// document.getElementById('fruitList').innerHTML = currentFruit;
// document.getElementById('fruitList').innerHTML = "fa";
var fruits = [];
