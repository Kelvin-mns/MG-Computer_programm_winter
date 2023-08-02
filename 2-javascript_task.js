function generateRandomNumber() {
    const randNumber = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(Math.ceil(Math.random() * 9) + 1));
    });
    randNumber.then((res) => {
        console.log(rest);
    }).catch(err => {
        console.log('Enter While showing results: ' + err);
    })
}
// b
let something = async () => {
    try {
        await generateRandomNumber()
    } catch (err) {
        console.log("Error occured")
    }
}
