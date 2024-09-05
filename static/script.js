
// // JavaScript to toggle the visibility of divs
// const navbarButtons = document.querySelectorAll(".navbar-button");
// const pages = document.querySelectorAll(".page");

// navbarButtons.forEach(button => {
//     button.addEventListener("click", () => {
//         // Remove the "active" class from all buttons
//         navbarButtons.forEach(btn => btn.classList.remove("active"));
//         // Add the "active" class to the clicked button
//         button.classList.add("active");

//         // Hide all divs
//         pages.forEach(page => page.style.display = "none");

//         // Show the selected div based on the data-target attribute
//         const targetDivId = button.getAttribute("data-target");
//         const targetDiv = document.getElementById(targetDivId);
//         targetDiv.style.display = "block";
//     });
// });

// // // 