$(document).ready(function () {
    if (localStorage.getItem('token')) {
        window.location = "/todo-list"
    }
    loadOnReadyFunctions();
});

function loadOnReadyFunctions() {
    $('#login-button').on('click', onLoginButtonClick);
}


function onLoginButtonClick() {
    console.log("on login button click");
    let email = $('#email').val();
    let password = $('#password').val();
    if (email && password) {
        let userData = {
            email: email,
            password: password,
        };
        authenticateUser(userData, onAuthenticateUserSuccess, onAuthenticateUserError)
    }
}

function onAuthenticateUserSuccess(data) {
    localStorage.setItem("token", data.token);
    window.location = "/todo-list"
}

function onAuthenticateUserError(data) {
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