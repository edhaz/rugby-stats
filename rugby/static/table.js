const extraColumns = [4, 5, 6, 7, 8, 9, 10, 11]
toggleVisibility('reduce')

function handleColumns() {
    if (document.getElementById('expand').style.display != 'none')
        showColumns()
    else
        hideColumns()
    toggleVisibility('expand')
    toggleVisibility('reduce')
}


function hideColumns() {
    extraColumns.forEach(function (column) {
        hideColumn(column);
    })
}

function showColumns() {
    extraColumns.forEach(function (column) {
        showColumn(column);
    })
}

function hideColumn(column) {
    document.querySelector(`th:nth-child(${column})`).style.maxWidth = 0;
    document.querySelector(`th:nth-child(${column})`).style.padding = 0;
    document.querySelector(`th:nth-child(${column})`).style.borderWidth = 0;
    document.querySelectorAll(`td:nth-child(${column})`).forEach(function (col) {
        col.style.maxWidth = 0;
        col.style.padding = 0;
        col.style.borderWidth = 0;
    });
}

function showColumn(column) {
    document.querySelector(`th:nth-child(${column})`).style.maxWidth = "100px";
    document.querySelector(`th:nth-child(${column})`).style.padding = "7px";
    document.querySelector(`th:nth-child(${column})`).style.borderWidth = "1px";
    document.querySelectorAll(`td:nth-child(${column})`).forEach(function (col) {
        col.style.maxWidth = "100px";
        col.style.padding = "7px";
        col.style.borderWidth = "1px";
    });
}

function toggleVisibility(id) {
    let element = document.getElementById(id);
    if (element.style.display != 'none')
        element.style.display = 'none'
    else
        element.style.display = 'initial'
}
