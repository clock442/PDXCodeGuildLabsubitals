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
while (true) {
    alert('Welcome to Rock, Paper, Scissors. I will pick a random choice. Try and beat me.')
    let userChoice = prompt('Chose rock, paper, scissors')
    if (!choice.includes(userChoice)){
        alert('Enter something valid.')
        continue
    }
    let computerChoice = getComputerChoice()
    alert('You ' + matrix[userChoice][computerChoice])
    let repeat = prompt('Would you like to play again? y/n')
    if (repeat == 'n'){
        break
    }
}