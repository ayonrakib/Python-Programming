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
    //      1. friendNumber = 1
    //      2. friendsBlock hobe row header, 1st column header, image and columnend
    //      3. friends empty string
    //      4. response object(eval(response)) er len porjonto iterate and friendNumber++:
    //          1. friends += friendsBlock + column shuru + response[index]['name'] + column shesh + column shuru + addfreind(response[index]['email']) + column shesh + column shuru + blockFriend + column shesh+ row shesh
    //      5. friends id te friends boshabo page reload chara
    $("#searchFriend").click(function(){
        var friendName = $('#friendName').val();
        $.ajax({
            method: 'GET',
            url: '/getfriends',
            data: {name: friendName}
        }).done(function(response){
            var currentUserEmail = eval(response)[0];
            var friendNumber = 1;
            var friendsBlock = rowBlockHeader(friendNumber) + columnHeader() + imageBlock() + columnFooter();
            var friends = "";
            if (eval(response).length >=1){
                for(var index = 1; index < eval(response).length; index++, friendNumber++){
                    friends += friendsBlock + columnHeader() + eval(response)[index]["name"] + columnFooter() + columnHeader() + button(`${eval(response)[index]["email"]}`,"Add Friend", currentUserEmail, `${eval(response)[index]["email"]}`) + columnFooter() + columnHeader() + button("blockFriend","Block") + columnFooter() + rowBlockFooter();
                }
            }
            $('#friends').html(friends);
        });
    });
    $.ajax({
        method: 'GET',
        url: 'getpendingrequests',
        data: {}
    }).done(function(response){
        console.log(response);
    })
        // $("#pendingRequests").html($(this).parent().parent());
        // $(this).parent().parent().appendTo("#pendingRequests");
        // $(this).attr({
        //     id: "removeFriend",
        // });
        // $(this).html("Remove");
        // $(this).parent().parent().hide();

    // })
    $(document).on('click', '#removeFriend', function(){
        $(this).parent().parent().hide();
        $.ajax({
            method: 'GET',
            url: '/remove',
            data:{
                'userWhoRemoved' : 'a',
                'userToBeRemoved': 'b'
            }
        }).done(function(response){
            console.log(response);
        })
    })
    $(document).on('click', '#blockFriend', function(){
        $(this).parent().parent().hide();
    });
});

function rowBlockHeader(friendNumber){
    return `<div class = "row" id = friendNumber${friendNumber}>`;
}

function columnHeader(){
    return '<div class = "col-sm-3 col-lg-3" id = "">';
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

function button(buttonId, buttonValue, user, userToBeAdded){
    return `<button type = "button" id = ${buttonId} onclick = "addFriend('${user}', '${userToBeAdded}')" class = "w-70 btn btn-sm btn-primary">
            ${buttonValue} </button>`;
}

function columnFooter(){
    return '</div>';
}

function rowBlockFooter(){
    return '</div>';
}

function addFriend(currentUserEmail, userToBeAdded){
    console.log(currentUserEmail);
    console.log(userToBeAdded);
    $.ajax({
        method: 'GET',
        url: 'addfriend',
        data: {
            'currentUserEmail' : currentUserEmail,
            'userToBeAdded' : userToBeAdded
        }
    }).done(function(response){
        console.log("addfriend response:  ");
        console.log(response);
    })
}