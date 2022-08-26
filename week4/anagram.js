// When given two strings from the user, write a function that checks if each string is an anagram of the other. If yes, return true, otherwise false

let string1 = 'Abcde';
let string2 = 'edCab';

function anagram(string1, string2) {
    // let dict1 = {};
    // let dict2 = {};
    // for (let i = 0; i < string1.length; i++) {
    //     if (dict1.string1[i] == undefined){
    //         console.log('We here')
    //         dict1[string1[i]] = 1;
    //     }
    //     else {
    //         dict1[string1[i]]++;
    //     }
    // }

    // for (let i = 0; i < string2.length; i++) {
    //     if (!string2[i] in dict2){
    //         dict2[string2[i]] = 1;
    //     }
    //     else {
    //         dict2[string2[i]]++;
    //     }
    // }
    // console.log(dict1)
    // console.log(dict2)


    
    if (string1.length != string2.length){
        return false;
    }

    else{
        let newString1 = string1.split('').sort().join('').toLower;
        let newString2 = string2.split('').sort().join('').toLower;
        if (newString1 == newString2) {
            return true;
        }
        else {
            return false;
        }
    }
    
}

console.log(anagram(string1, string2))