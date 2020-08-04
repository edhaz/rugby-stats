const extraColumns = [4, 5, 6, 7, 8, 9, 10, 11]
hideColumns()

function hideColumns(button) {
    extraColumns.forEach(function (column) {
        hideColumn(column);
    })
    document.getElementById('expand').disabled = false;
    document.getElementById('reduce').disabled = true;
}

function showColumns(button) {
    extraColumns.forEach(function (column) {
        showColumn(column);
    })
    document.getElementById('expand').disabled = true;
    document.getElementById('reduce').disabled = false;
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