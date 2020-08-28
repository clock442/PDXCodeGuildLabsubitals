let rotNum = document.querySelector('#rotNum')
let inputText = document.querySelector('#inputText')
let run_bt = document.querySelector('#run_bt')
let outputDiv = document.querySelector('#outputDiv')
let alphabet = 'abcdefghijklmnopqrstuvwxyz'

run_bt.onclick = function() {
    let outputText = ''
    let inputText2 = inputText.value.toLowerCase()
    let rotValue = parseInt(rotNum.value)
    for (i in inputText2){
        if (inputText2[i] ==' '){
            outputText += ' '
        }else if (!alphabet.includes(inputText2[i])){
            continue
        }else {
            console.log(alphabet.indexOf(inputText2[i]))
            outputText += alphabet[Math.abs((alphabet.indexOf(inputText2[i]) + rotValue))%alphabet.length]
        }
    }
    outputDiv.innerText = outputText
}

let rotNumBack = document.querySelector('#rotNumBack')
let inputTextBack = document.querySelector('#inputTextBack')
let run_bt_back = document.querySelector('#run_bt_back')
let outputDivBack = document.querySelector('#outputDivBack')
let alphabetBack = 'zyxwvutsrqponmlkjihgfedcba'

run_bt_back.onclick = function() {
    let outputText = ''
    let inputText2 = inputTextBack.value.toLowerCase()
    let rotValue = parseInt(rotNumBack.value)
    for (i in inputText2){
        if (inputText2[i] ==' '){
            outputText += ' '
        }else if (!alphabetBack.includes(inputText2[i])){
            continue
        }else {
            console.log(alphabetBack.indexOf(inputText2[i]))
            outputText += alphabetBack[Math.abs((alphabetBack.indexOf(inputText2[i]) + rotValue))%alphabet.length]
        }
    }
    outputDivBack.innerText = outputText
}