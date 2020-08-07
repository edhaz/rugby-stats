const extraColumns = [4, 5, 6, 7, 8, 9, 10, 11]
hideColumns()
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
    document.querySelector(`th:nth-child(${column})`).style.display = "none"
    document.querySelectorAll(`td:nth-child(${column})`).forEach(function (col) {
        col.style.display = "none"
    });
}

function showColumn(column) {
    document.querySelector(`th:nth-child(${column})`).style.display = "table-cell"
    document.querySelectorAll(`td:nth-child(${column})`).forEach(function (col) {
        col.style.display = "table-cell"
    });
}

function toggleVisibility(id) {
    let element = document.getElementById(id);
    if (element.style.display != 'none')
        element.style.display = 'none'
    else
        element.style.display = 'initial'
}
