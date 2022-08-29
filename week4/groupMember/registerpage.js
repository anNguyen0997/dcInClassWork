let data = [];

let submit = document.getElementById('form');
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
    alert(`${userFirst} ${userLast} is now registered`)

    let form = document.getElementById('form');
    form.reset();

    return data;
})



// function getUsername() {
//     return document.getElementById('usernameForm').value;
// }

function getEmail() {
    return document.getElementById('emailForm').value;
}

function getFirstName() {
    return document.getElementById('firstForm').value;
}

function getLastName() {
    return document.getElementById('lastForm').value;
}
function getPhone() {
    return document.getElementById('phoneForm').value;
}

function getPassword() {
    return document.getElementById('password').value;
}



function createUser(userEmail, userPassword) {
    pwCheck = /[A-Za-z0-9] +/
    if (userEmail.length == 0) {
        print('Enter a valid email')
    } else if (!pwCheck.test('password')) {
        print('Use letters and numbers for password')
    }
    newUser = {'email': userEmail, 'password': userPassword}
}

// --- Read and writing stored data -----------------------------------------------------------------------------------
function storingData() {

    const fs = require('fs');

    fs.writeFile('storedData.txt', userData, function(err) {
        if (err) {
            console.err;
            return
        } else {
            
        }
})

}









// ---  Login Page Functions -----------------------------------------------------------------------------------------
function checkPassword(userName, userPassword) {                // checking for existing user
    let storedData = new Map()                              // storing data into a map
    storedData.set(userData)

    if (storedData.get(userName) == undefined) {                // checking if that username exists
        alert('No existing account with that username')
    } else if (storedData.get(userName) == userPassword) {      // checking if that username exists with matching password
        alert('Logged in')  
    } else {                                                    // wrong password input
        alert('Invalid password')
    }
}

function checkUsername(userName) {
    let usernameRegex = /^[A-Za-z0-9]+$/
    return usernameRegex.test(userName)
}