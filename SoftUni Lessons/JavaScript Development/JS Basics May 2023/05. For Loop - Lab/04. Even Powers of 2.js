function evenPowersOfTwo(...params) {
    let n = Number(params.shift());
    let num = 1;
    for (let i = 0; i <= n; i += 2) {
      console.log(num);
      num = num * 2 * 2;
    }
}

evenPowersOfTwo(1)

// Fuck that task!