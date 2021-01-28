// proti line er pore semicolon likhbo
// switch khub specific. switch e shudhu ektai value check kora jaay, so jeikhane switch likha jaay tokhon sheita korte hobe
function sayHello() {
    alert("This is from the external file!");
 }

 function showVariables(){
     var name = "Ayon in show variable function";
     var age = 10;
     var isFat = true;
     document.write("name = ", name,"age= ", age,"Is he fat?= ", isFat);
 }

 function showMyName(){
     var name = "ayon in show name function";
     document.write(name);
 }

 function increaseAge(){
    //  ++age
    // if (age>10){
    //     document.getElementById("para").innerHTML = 'Yes,age is 20' 
    // }
    // else{
    //     document.getElementById("para").innerHTML = 'No, age is not 20.'
    // }
    // switch(age){
    //     case 20:
    //         document.getElementById("para").innerHTML = 'Yes,age is 20';
    //         break; 
    //     case 21:
    //         document.getElementById("para").innerHTML = 'Yes,age is 21';
    //         break; 
    //     default:
    //         document.getElementById("para").innerHTML = 'No, age is not 20.';
    // }
    // var fruits = ['mango','apple','banana']
    // for(index in fruits){
    //     document.write('the fruit is: '+fruits[index] + "<br>")
    // }

 }
 function firstFunction(name){
    return "modified " + name;
}

function secondFunction(){
    function getSquare(){
        return 5*5
    }
    document.getElementById("para").innerHTML = getSquare();
}

function onSubmitForm(){
    return true;
}

var name = "Global Name Ayon";
var age = 20;

// 4 = 100
// Not of 4 = Not of 100 = 011

/* twos complement of 5:
    +5 = 101
    NOT bits of +5 = 010
    add 1 to it = 011
*/

/* how to say Not of 4 is -5?
    Not of 4 is 011. Subtract 1 from it, becomes 010.
    reverse all bits -> 101 -> 5 in decimal.
    so, Not of 4 is -5.
*/
