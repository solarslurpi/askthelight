

function showLoader() {
    clearPage();
    const loader = document.getElementById("loader");
    loader.classList.add("show");
}

function hideLoader() {
    const loader = document.getElementById("loader");
    loader.classList.remove("show");
}

function formStarting() {
    // add loading overlay
    var loadingOverlay = document.createElement('div');
    loadingOverlay.classList.add('loading-overlay');
    loadingOverlay.innerHTML = '<div class="loader"><span></span><span></span><span></span><span></span></div>';
    document.body.appendChild(loadingOverlay);
    clearPage()

    // submit form
    document.getElementById('form').submit();
}


function clearPage() {
    // document.getElementById("error").textContent = "";
    // document.getElementById("topic").textContent = "";
    // document.getElementById("title").textContent = "";
    // document.getElementById("words").textContent = "";
    // document.getElementById("response").textContent = "";
}

// clear the page when it first loads
document.addEventListener('DOMContentLoaded', clearPage);

// Attach event listener to the form
document.querySelector('form').addEventListener('submit', (event) => {
// Prevent the default form submission behavior
event.preventDefault();
// Get the user input from the form
const userInput = document.getElementById('topic').value;
// Make a GET request to the server with the user input as the query parameter
const url = `/api/query?input=${encodeURIComponent(userInput)}`;
// Show the loader while waiting for the response
showLoader();
fetch(url)
    .then(response => response.text())
    .then(data => {
    // Display the response data in the HTML page
    const responseElement = document.getElementById("response");
    responseElement.innerHTML = data;
    // Hide the loader
    hideLoader();
    // Clear the form input after displaying the response
    document.getElementById("topic").value = "";
    })
    .catch(error => {
    // Display the error message in the HTML page
    const errorElement = document.getElementById("error");
    errorElement.innerHTML = error;
    // Hide the loader
    hideLoader();
    });
});
  