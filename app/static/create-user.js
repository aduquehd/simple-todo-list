$(document).ready(function () {
    if (localStorage.getItem('token')) {
        window.location = "/todo-list"
    }
    loadCreateUserOnReadyFunctions();
});

function loadCreateUserOnReadyFunctions() {
    $('#create-user').on('click', onCreateUserButtonClick);
}


function onCreateUserButtonClick() {
    let email = $('#email').val();
    let password = $('#password').val();
    let firstName = $('#first-name').val();
    let lastName = $('#last-name').val();
    if (email && password && firstName && lastName) {
        let userData = {
            email: email,
            password: password,
            first_name: firstName,
            last_name: lastName,
        };
        createUser(userData, onCreateUserSuccess, onCreateUserError)
    }
}

function onCreateUserSuccess(data) {
    window.location = "/login"
}

function onCreateUserError(data) {
    if ('message' in data.responseJSON) {
        if (typeof(data.responseJSON['message']) === "string") {
            toastr.warning(data.responseJSON['message'])
        } else {
            $.each(data.responseJSON['message'], function (key, value) {
                toastr.warning(value)
            })
        }
    }
}