function validateForm() {
    var firstName = document.getElementById("firstName").value;
    var lastName = document.getElementById("lastName").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var phone = document.getElementById("phone").value;

    // First letter capitalization for name fields
    var firstNameCapitalized = firstName.charAt(0).toUpperCase() + firstName.slice(1).toLowerCase();
    var lastNameCapitalized = lastName.charAt(0).toUpperCase() + lastName.slice(1).toLowerCase();
    document.getElementById("firstName").value = firstNameCapitalized;
    document.getElementById("lastName").value = lastNameCapitalized;

    // Check if fields are filled
    if (firstName.trim() === "") {
        alert("Please enter your first name");
        return false;
    }
    if (lastName.trim() === "") {
        alert("Please enter your last name");
        return false;
    }
    if (email.trim() === "") {
        alert("Please enter your email address");
        return false;
    }
    if (password.trim() === "") {
        alert("Please enter your password");
        return false;
    }
    if (phone.trim() === "") {
        alert("Please enter your phone number");
        return false;
    }

    // Email validation
    var emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/;
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address");
        return false;
    }

    // Phone number validation (basic validation)
    var phoneRegex = /^\d{10}$/;
    if (!phoneRegex.test(phone)) {
        alert("Please enter a valid 10-digit phone number");
        return false;
    }

    // Password validation
    var passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;
    if (!passwordRegex.test(password)) {
        alert(
            "Password must contain at least 8 characters, including at least one uppercase letter, one digit, and one special character (!@#$%^&*)"
        );
        return false;
    }

    return true;
}
