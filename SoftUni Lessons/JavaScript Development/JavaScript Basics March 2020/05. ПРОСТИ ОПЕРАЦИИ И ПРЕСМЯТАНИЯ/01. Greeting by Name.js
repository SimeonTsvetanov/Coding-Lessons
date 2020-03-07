function greeting(input) {
    let name = input.shift();
    // let sayHello = "Hello, " + name + "!";
    console.log(`Hello, ${name}!`);

    // Same code but in Python: 
    //print(f"Hello, {input()}!")
}

greeting(["Simeon Tsvetanov"]);
