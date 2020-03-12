function animalTye(input) {
    let animal = input.shift();

    switch(animal) {
        case "dog":
            console.log("mammal");
            break;
        case "crocodile":
        case "tortoise":
        case "snake":
            console.log("reptile");
            break;
        default:
            console.log("unknown");
    }
}

animalTye(["dog"]);  // Expected output: mammal
animalTye(["snake"]);  // Expected output: reptile
animalTye(["cat"]);  // Expected output: unknown

