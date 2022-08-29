let data = [];


let form = document.getElementById('form');
let  login = document.getElementById('loginForm');
login.addEventListener('submit', function(event) {
event.preventDefault();

    let userEmail = getEmail();
    // let userFirst = getFirstName();
    // let userLast = getLastName();
    // let userPhone = getPhone();
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
    // alert(`${userFirst} ${userLast} is now registered`)

    form.reset();

    return data;
})




function getEmail() {
    return document.getElementById('emailForm').value;
}

// function getFirstName() {
//     return document.getElementById('firstForm').value;
// }

// function getLastName() {
//     return document.getElementById('lastForm').value;
// }
// function getPhone() {
//     return document.getElementById('phoneForm').value;
// }

function getPassword() {
    return document.getElementById('password').value;
}



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