let token = localStorage.getItem("token");

function authenticateUser(data, successCallBack, errorCallBack) {
    $.ajax({
        type: "POST",
        url: "/api/v1/auth",
        dataType: "json",
        data: data,
        success: successCallBack,
        error: errorCallBack
    })
}

function getTodoList(successCallBack, errorCallBack) {
    $.ajax({
        type: "GET",
        beforeSend: function (xhr) {
            xhr.setRequestHeader('Authorization', `Bearer ${token}`);
        },
        url: "/api/v1/todo-list",
        dataType: "json",
        success: successCallBack,
        error: errorCallBack
    })
}

function createTodoListApi(data, successCallBack, errorCallBack) {
    $.ajax({
        type: "POST",
        beforeSend: function (xhr) {
            xhr.setRequestHeader('Authorization', `Bearer ${token}`);
        },
        data: data,
        url: "/api/v1/todo-list",
        dataType: "json",
        success: successCallBack,
        error: errorCallBack
    })
}

function updateTodoListApi(todoListId, data, successCallBack, errorCallBack) {
    $.ajax({
        type: "PUT",
        beforeSend: function (xhr) {
            xhr.setRequestHeader('Authorization', `Bearer ${token}`);
        },
        data: data,
        url: `/api/v1/todo-list/${todoListId}`,
        dataType: "json",
        success: successCallBack,
        error: errorCallBack
    })
}

function createUser(data, successCallBack, errorCallBack) {
    $.ajax({
        type: "POST",
        url: "/api/v1/user",
        dataType: "json",
        data: data,
        success: successCallBack,
        error: errorCallBack
    })
}