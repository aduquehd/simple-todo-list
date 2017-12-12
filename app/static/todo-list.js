$(document).ready(function () {
    if (!localStorage.getItem('token')) {
        window.location = "/login"
    }
    loadOnReadyFunctions();
});

function loadOnReadyFunctions() {
    getTodoList(getTodoListSuccess, getTodoListError);
    $('#create-new-todo').on('click', createTodoList);
    $('#refresh-todo-list').on('click', function () {
        getTodoList(getTodoListSuccess, getTodoListError);
    });
    $('.todo-list-checkbox-item').change(updateTodoList);

    $(document).on("click", "input[type='checkbox']", updateTodoList);
}

function updateTodoList() {
    let todoListId = $(this).attr('data-id');
    let data = {
        status: $(this).is(":checked")
    };
    updateTodoListApi(todoListId, data, updateTodoListSuccess, updateTodoListError);
}

function updateTodoListSuccess() {
    getTodoList(getTodoListSuccess, getTodoListError);
}

function updateTodoListError() {
    $('#new-todo').val("");
    getTodoList(getTodoListSuccess, getTodoListError);
}

function createTodoList() {
    let data = {
        description: $('#new-todo').val()
    };
    createTodoListApi(data, createTodoListSuccess, createTOdoListError())
}

function createTodoListSuccess() {
    $('#new-todo').val("");
    getTodoList(getTodoListSuccess, getTodoListError);
}

function createTOdoListError() {
    getTodoList(getTodoListSuccess, getTodoListError);
}

function getTodoListSuccess(data) {
    $('#todo-list-table').empty();
    let count = 1;
    $.each(data, function (i, value) {
        let status = "";

        if (value.status) {
            status = "checked"
        }

        let htmlText = "";
        htmlText += "<tr>";
        htmlText += `<th scope="row">${count}</th>`;
        htmlText += `<td>${value.description}</td>`;
        htmlText += `<td><input style="cursor:pointer;" class="todo-list-checkbox-item" data-id="${value.id}" class="form-check-input" ${status} type="checkbox" value=""></td>`;
        htmlText += "</tr>";
        $('#todo-list-table').append(htmlText);
        count++;
    });
}

function getTodoListError(data) {
}