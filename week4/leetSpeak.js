// write a function leetspeak which is given a string, and returns the leetspeak equivalent of the string. 
// to convert text to its leetspeak version, make the following substitutions

let leetConvert = (str) => {
    let leetMap = new Map();

    leetMap.set = ('A', '4');
    leetMap.set = ('B', '8');
    leetMap.set = ('E', '3');
    leetMap.set = ('G', '6');
    leetMap.set = ('I', 'l');
    leetMap.set = ('L', '1');
    leetMap.set = ('O', '0');
    leetMap.set = ('S', '5');
    leetMap.set = ('T', '7');
    leetMap.set = ('Z', '2');
    
    let leetString = str.toUpperCase().split('');
    for (i = 0; i < leetString.length; i++) {
        if (leetMap.get(leetString[i]) == undefined) {
            continue;
        } else {
            leetString[i] = leetMap.get(leetString[i])
        }
    }

    return leetString.join('')
}

let testString = 'an'
console.log(leetConvert(testString))