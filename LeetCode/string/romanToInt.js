const romanToInt = (s) => {
    const dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    let result = 0


    for (let i=0; i < s.length - 1; i++) {

        const current = dict[s[i]]
        const next = dict[s[i+1]]

        if (next > current) {
            result = result - current
        } 
        else {
            result = result + current
        }
        
    }
    result += dict[s[s.length - 1]]; // Add the value of the last numeral
    return result;
}


console.log(romanToInt("XIV"))