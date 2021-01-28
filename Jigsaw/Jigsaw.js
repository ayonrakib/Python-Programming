// function putDice
// input: blockNumber
// return: nothing
function setIconInPuzzle(blockNumber){
    document.getElementById(blockNumber).innerHTML = currentIcon;
    validateImage();
}

// input: destinationBlockNumber, currentIcon
// return: none
// method:
//      currentMapping er destinationBlockNumber key te currentIcon value boshabo
//      currentMapping and targetMapping soman hoile:
//          alert dibo mile gese
function validateImage(){
    if(JSON.stringify(currentMapping) == JSON.stringify(targetMapping)){
        alert("Game Over!");
    }
}

function setIconInVariable(destinationBlock){
    switch(destinationBlock){
        case "sourceBlock1":
            currentIcon = "<i class='fa fa-angle-double-right'></i>";
            break;
        case "sourceBlock2":
            currentIcon = "<i class='fa fa-angle-double-down'></i>";
            break;
        case "sourceBlock3":
            currentIcon = "<i class='fa fa-angle-double-up'></i>";
            break;
        case "sourceBlock4":
            currentIcon = "<i class='fa fa-angle-double-left'></i>";
            break;
    }
}
function restartGame(){
    location.reload();
}

var currentIcon = '';

var targetMapping = {"destinationBlock1":"<i class='fa fa-angle-double-right'></i>", 
                     "destinationBlock2":"<i class='fa fa-angle-double-bottom'></i>",
                     "destinationBlock3":"<i class='fa fa-angle-double-up'></i>",
                     "destinationBlock4":"<i class='fa fa-angle-double-left'></i>",
                    }

var currentMapping = {"destinationBlock1":"", 
                      "destinationBlock2":"",
                      "destinationBlock3":"",
                      "destinationBlock4":"",
                    }

// task 1: ekta chobi gimp sue kore nije vangbo. crop kore kore jigsaw piece banabo. eisob icon use kora jabe na.