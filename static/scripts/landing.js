// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
    // Get the "Sign In" button element
    const signInButton = document.getElementById("signInButton");

    // Add a click event listener to the "Sign In" button
    if (signInButton) {
        signInButton.addEventListener("click", () => {
            // Redirect to the login page
            window.location.href = "/login";
        });
    }

    // Get the "Sign Up" button element
    const signupButton = document.getElementById("signupButton");

    // Add a click event listener to the "Sign Up" button
    if (signupButton) {
        signupButton.addEventListener("click", () => {
            // Redirect to the sign-up page
            window.location.href = "/signup";
        });
    }
});
