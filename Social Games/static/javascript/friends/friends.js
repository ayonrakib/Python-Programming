$(document).ready(function(){
    $("#searchFriend").click(function(){
        var friendName = $('#friendName').val();
        // document.getElementById("friends").innerHTML = rowBlockHeader() + columnHeader() + imageBlock() + columnFooter() + columnHeader() + firstNameBlock() + " " + lastNameBlock()+ columnFooter() + columnHeader() + addFriendButton() + columnFooter() + rowBlockFooter();
        // console.log(friendName);
        // $('#friendName').val('eva');
        $.ajax({
            method: 'GET',
            url: '/getfriends',
            data: {name: friendName}
        }).done(function(response){
            var friends = "";
            
            // for(var index = 0; index < response.length; index++){
            //     friends += "a";
            // }
            console.log(response);
        });
    });
});

function rowBlockHeader(){
    return '<div class = "row">';
}

function columnHeader(){
    return '<div class = "col-sm-4 col-lg-4">';
}

function imageBlock(){
    return '<img src = "/images/tictactoe.png" height = "40px" width = "40px">';
}

function firstNameBlock(){
    return 'Rakib';
}

function lastNameBlock(){
    return 'Ayon';
}

function addFriendButton(){
    return `<button type = "button" class = "w-70 btn btn-sm btn-primary">
            Add Friend </button>`;
}

function columnFooter(){
    return '</div>';
}

function rowBlockFooter(){
    return '</div>';
}