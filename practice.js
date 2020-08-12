function strings(arr){
    arr = arr.sort()
    console.log(arr)
    arr.forEach( e => {
        console.log(e)
    })


}

arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

console.log(strings(arr))