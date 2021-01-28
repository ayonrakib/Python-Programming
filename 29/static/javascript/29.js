function restartGame(){
    location.reload();
}


function getPlayerNumber(playerId){
    return playerNumberMapping[playerId];
}


function getSlotNumber(playerId){
    return slotNumberMapping[playerId];
}


function getOtherPlayers(playerId){
    for(var index = playerId, count = 1, currentIndex = index ; count < 4 ; count++,index++){
        if (index > 3){
            currentIndex = index-4;
        }
        else{
            currentIndex = index;
        }
        otherPlayers.push(playerIds[currentIndex]);
    }
    // console.log(otherPlayers);
    return otherPlayers;
}


function assignCardsToAllPlayers(){
    for(var playerId = 1; playerId < 5; playerId++){
        var playerNumber = getPlayerNumber(playerId);
        while(playerCardsMapping[playerNumber].length <= 7){
            var randomCard = Math.floor(Math.random() * (31 - 0 + 1) ) + 0;
            if(selectedCards.includes(totalCards[randomCard])){
                continue;
            }
            else{
                playerCardsMapping[playerNumber].push(totalCards[randomCard]);
                selectedCards.push(totalCards[randomCard]);
            };
        };
    };
    // console.log(playerCardsMapping["firstPlayer"]);
    // console.log(playerCardsMapping["secondPlayer"]);
    // console.log(playerCardsMapping["thirdPlayer"]);
    // console.log(playerCardsMapping["fourthPlayer"]);
};
function checkIfAllCardsAreJack(firstCard, secondCard, thirdCard, fourthCard, playerNumber){
    if (firstCard.includes("jack") && secondCard.includes("jack") && thirdCard.includes("jack") && fourthCard.includes("jack")){
        isGameOver = true;
        alert(`${playerNumber} got four jacks!`);
        restartGame();
    }
}
function showCurrentUserBiddingCards(playerId, slotNumber){
    var playerNumber = getPlayerNumber(playerId);
    // var slotNumber = getSlotNumber(playerId);
    var firstCard = "images/"+ playerCardsMapping[playerNumber][0];
    var secondCard = "images/"+ playerCardsMapping[playerNumber][1];
    var thirdCard = "images/"+ playerCardsMapping[playerNumber][2];
    var fourthCard = "images/"+ playerCardsMapping[playerNumber][3];
    checkIfAllCardsAreJack(firstCard, secondCard, thirdCard, fourthCard, playerNumber);
    if (!isGameOver){
        document.getElementById(slotNumber+"SlotFirstCard").innerHTML = `<img src= '${firstCard}' alt="card" width="80" height="80"></img>`;
        document.getElementById(slotNumber+"SlotSecondCard").innerHTML = `<img src= '${secondCard}' alt="card" width="80" height="80"></img>`;
        document.getElementById(slotNumber+"SlotThirdCard").innerHTML = `<img src= '${thirdCard}' alt="card" width="80" height="80"></img>`;
        document.getElementById(slotNumber+"SlotFourthCard").innerHTML = `<img src= '${fourthCard}' alt="card" width="80" height="80"></img>`;
    }
}


function showOtherUsersBiddingCards(otherPlayerIds){
    var secondPlayer = otherPlayerIds[0];
    showCurrentUserBiddingCards(secondPlayer, "second");
    var thirdPlayer = otherPlayerIds[1];
    showCurrentUserBiddingCards(thirdPlayer, "third");
    var fourthPlayer = otherPlayerIds[2];
    showCurrentUserBiddingCards(fourthPlayer, "fourth");
    // var firstCard = "images/"+ playerCardsMapping[playerNumber][0];
    // var secondCard = "images/"+ playerCardsMapping[playerNumber][1];
    // var thirdCard = "images/"+ playerCardsMapping[playerNumber][2];
    // var fourthCard = "images/"+ playerCardsMapping[playerNumber][3];
    // checkIfAllCardsAreJack(firstCard, secondCard, thirdCard, fourthCard, playerNumber);
    // if (!isGameOver){
    //     document.getElementById("firstSlotFirstCard").innerHTML = `<img src= '${firstCard}' alt="card" width="80" height="80"></img>`;
    //     document.getElementById("firstSlotSecondCard").innerHTML = `<img src= '${secondCard}' alt="card" width="80" height="80"></img>`;
    //     document.getElementById("firstSlotThirdCard").innerHTML = `<img src= '${thirdCard}' alt="card" width="80" height="80"></img>`;
    //     document.getElementById("firstSlotFourthCard").innerHTML = `<img src= '${fourthCard}' alt="card" width="80" height="80"></img>`;
    // }
};

function provideCards(playerId){
    playerNumber = getPlayerNumber(playerId);
    // console.log(playerNumber);
    assignCardsToAllPlayers();
    // console.log(playerNumber);
    // console.log(playerCardsMapping[playerNumber]);
    // console.log(selectedCards);
    var otherPlayerIds = getOtherPlayers(playerId);
    console.log(otherPlayerIds);
    console.log(otherPlayerIds[0]);
    showCurrentUserBiddingCards(playerId, "first");
    showOtherUsersBiddingCards(otherPlayerIds);
    
}

var totalCards = ["jackOfClubs.png","nineOfClubs.png","aceOfClubs.png","tenOfClubs.png","kingOfClubs.png","queenOfClubs.png","eightOfClubs.png","sevenOfClubs.png",
                  "jackOfDice.png","nineOfDice.png","aceOfDice.png","tenOfDice.png","kingOfDice.png","queenOfDice.png","eightOfDice.png","sevenOfDice.png",
                  "jackOfSpades.png","nineOfSpades.png","aceOfSpades.png","tenOfSpades.png","kingOfSpades.png","queenOfSpades.png","eightOfSpades.png","sevenOfSpades.png",
                  "jackOfHearts.png","nineOfHearts.png","aceOFHearts.png","tenOfHearts.png","kingOfHearts.png","queenOfHearts.png","eightOfHearts.png","sevenOfHearts.png"];

var firstPlayerCards = [];

var secondPlayerCards = [];

var thirdPlayerCards = [];

var fourthPlayerCards = [];

var playerCardsMapping = {"firstPlayer" : firstPlayerCards,
                          "secondPlayer" : secondPlayerCards,
                          "thirdPlayer" : thirdPlayerCards,
                          "fourthPlayer" : fourthPlayerCards};

var playerNumberMapping = { 1 : "firstPlayer",
                            2 : "secondPlayer",
                            3 : "thirdPlayer",
                            4 : "fourthPlayer"};

var slotNumberMapping = { 1 : ["secondSlot", "thirdSlot", "fourthSlot"],
                          2 : ["thirdSlot", "fourthSlot", "firstSlot"],
                          3 : ["fourthSlot", "firstSlot", "secondSlot"],
                          4 : ["firstSlot","secondSlot", "thirdSlot"]};

var playerToSlotMapping = { "firstSlot" : "firstPlayer",
                            "secondSlot" : "secondPlayer",
                            "thirdSlot" : "thirdPlayer",
                            "fourthSlot" : "fourthPlayer" };

var selectedCards = [];

var playerIds = [1,2,3,4];

var otherPlayers = [];

var relativeImageURL = "D:/Python Programming/29/images";

var isGameOver = false;