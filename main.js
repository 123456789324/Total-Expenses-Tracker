// Get HTML Elements
let form = document.getElementById("expenseForm");
let expenseList = document.getElementById("expenseList");

// Add Expense
form.addEventListener("submit", function(event) {

    event.preventDefault();

    let date = document.getElementById("date").value;
    let category = document.getElementById("category").value;
    let description = document.getElementById("description").value;
    let amount = Number(document.getElementById("amount").value);

    // Check Amount
    if (amount <= 0) {
        alert("Please enter a valid amount!");
        return;
    }

    // Create New Table Row
    let row = document.createElement("tr");

    row.innerHTML = `
        <td>${date}</td>
        <td>${category}</td>
        <td>${description}</td>
        <td>Rs. ${amount}</td>
        <td>
            <button onclick="deleteExpense(this)">Delete</button>
        </td>
    `;

    // Add Row to Table
    expenseList.appendChild(row);

    alert("Expense Added Successfully!");

    // Clear Form
    form.reset();

});


// Delete Expense
function deleteExpense(button) {

    let row = button.parentElement.parentElement;

    row.remove();

}


// Search Expense
let search = document.getElementById("search");

search.addEventListener("input", function() {

    let value = search.value.toLowerCase();

    let rows = expenseList.getElementsByTagName("tr");

    for (let i = 0; i < rows.length; i++) {

        let text = rows[i].innerText.toLowerCase();

        if (text.includes(value)) {
            rows[i].style.display = "";
        } 
        else {
            rows[i].style.display = "none";
        }

    }

});