$(document).ready(function () {
    $('#logout-button').on('click', logout)
});


function logout() {
    localStorage.removeItem('token');
    window.location = "/login"
}