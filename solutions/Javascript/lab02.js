let choice = ['rock', 'paper', 'scissors']

function getComputerChoice() {
    let cIndex = parseInt(Math.random()*3)
    return choice[cIndex]
}

let matrix = {
    rock: {
        rock: 'Tie',
        paper: 'Lose',
        scissors: 'Win'
    },
    paper: {
        rock: 'Win',
        paper: 'Tie',
        scissors: 'Lose'
    },
    scissors: {
        rock: 'Lose',
        paper: 'Win',
        scissors: 'Tie'
    }
}

let user_input = document.querySelector('#user_input')
let play_bt = document.querySelector('#play_bt')
let output_div = document.querySelector('#output_div')

play_bt.onclick = function() {
    let computerChoice = getComputerChoice()
    let hand = user_input.value;
    if (!choice.includes(hand)){
        output_div.innerText = 'Enter something Valid'
    }else {
        output_div.innerText = 'You ' + matrix[hand][computerChoice]
    }
}

// while (true) {
//     alert('Welcome to Rock, Paper, Scissors. I will pick a random choice. Try and beat me.')
//     let userChoice = prompt('Chose rock, paper, scissors')
//     if (!choice.includes(userChoice)){
//         alert('Enter something valid.')
//         continue
//     }
//     let computerChoice = getComputerChoice()
//     alert('You ' + matrix[userChoice][computerChoice])
//     let repeat = prompt('Would you like to play again? y/n')
//     if (repeat == 'n'){
//         break
//     }
// }