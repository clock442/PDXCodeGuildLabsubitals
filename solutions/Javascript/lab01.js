let convert_dict = {
    ft: {
        ft: 1,
        mi: 5280,
        m: 0.3048,
        km: 0.0003048
    },
    mi:{
        ft: 5280,
        mi: 1,
        m: 1609.34,
        km: 1.60934
    },
    m:{
        ft: 3.28084,
        mi: 0.000621,
        m: 1,
        km: 0.001
    },
    km:{
        ft: 3280.84,
        mi: 0.621,
        m: 1000,
        km: 1
    }
}

while (true) {
    alert('Welcome to unit converter. Your available units are ft, mi, m, and km.')
    let unit_from = prompt('What unit would you like to convert from: ')
    let unit_to = prompt('What unit would you like to convert to: ')
    let distance = parseInt(prompt('What is your distance: '))
    let unit_from_str = unit_from.toString()
    let unit_to_str = unit_to.toString()
    let converted_num = distance * convert_dict[unit_from_str][unit_to_str]
    alert('Your distance in ' + unit_to +' is ' + converted_num + '.')
    let repeat = prompt('Would you like to convert something else? y/n: ')
    if (repeat == 'n'){
        break
    }    
}
alert('Bye Bye.')