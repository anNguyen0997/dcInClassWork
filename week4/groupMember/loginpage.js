let data = [];

let form = document.getElementById('loginForm');
submit.addEventListener('submit', function(event) {
    event.preventDefault();

    let userEmail = getEmail();
    let userFirst = getFirstName();
    let userLast = getLastName();
    let userPhone = getPhone();
    let userPassword = getPassword();

    let userData = {
        email: userEmail,
        first: userFirst,
        last: userLast,
        phone: userPhone,
        password: userPassword
    }

    data.push(userData)
    console.log(data);

    let form = document.getElementById('form');
    form.reset();

    return data;
})

function checkPassword(userEmail, userPassword) {                // checking for existing user
    let storedData = new Map()                              // storing data into a map
    storedData.set(userData)

    if (storedData.get(userEmail) == undefined) {                // checking if that username exists
        alert('No existing account with that username')
    } else if (storedData.get(userEmail) == userPassword) {      // checking if that username exists with matching password
        alert('Logged in')  
    } else {                                                    // wrong password input
        alert('Invalid password')
    }
}

function checkUsername(userEmail) {
    let usernameRegex = /^[A-Za-z0-9]+$/
    return usernameRegex.test(userEmail)
}