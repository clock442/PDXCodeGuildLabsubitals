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
            outputText += ''
        }else if (alphabet.includes(inputText2[i])){
            console.log(alphabet.indexOf(inputText2[i]))
            outputText += alphabet[(alphabet.indexOf(inputText2[i]) + rotValue)%alphabet.length]
        }
    }
    outputDiv.innerText = outputText
}