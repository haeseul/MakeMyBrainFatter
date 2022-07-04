const requestSth = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const errorFlag = Math.random() < 0.1 ? true : false;

            if (errorFlag) reject("error");
            resolve("success")
        }, 1000);
    })
}

const p = requestSth();

const a = Promise.resolve('성공');
const b = Promise.reject('실패');

// Promise.all([a, b]).then(([resA, resB]) => {
//     console.log(resA + resB)
// })

a.then((resolve) => {
    console.log('1회' + resolve);
    return a;
}).then((resolve) => {
    console.log('2회' + resolve);   // reject
    return b;
}).catch((reject) => {
    console.log('3회' + reject);    // catch reject
    return a;
}).then((resolve) => {
    console.log('4회' + resolve);   // continue
    return a;
})

const c = Promise.resolve(Math.random())
c.then((res) => {
    console.log()
})