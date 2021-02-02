$(document).ready(function(){
    // searchFriend id te click er function
    // input: none
    // return: none, just replace with the found users
    // method:
    //  1. friendName input er val read korbo
    //  2. ajax method:
    //      1. input: method: get, url: getfriends, data:{name:friendName}
    //  3. ei method er return value er jonno done method call
    //  4. input: function definition with the response value from the server
    //      1. friendsBlock hobe row header, 1st column header, image and columnend
    //      2. friends empty string
    //      3. response object(eval(response)) er len porjonto iterate:
    //          1. friends += friendsBlock + column shuru + response
    $("#searchFriend").click(function(){
        var friendName = $('#friendName').val();
        $.ajax({
            method: 'GET',
            url: '/getfriends',
            data: {name: friendName}
        }).done(function(response){
            var friendsBlock = rowBlockHeader() + columnHeader() + imageBlock() + columnFooter();
            var friends = "";
            for(var index = 0; index < eval(response).length; index++){
                friends += friendsBlock + columnHeader() + eval(response)[index] + columnFooter() + columnHeader() + addFriendButton() + columnFooter() + rowBlockFooter();
            }
            $('#friends').html(friends);
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