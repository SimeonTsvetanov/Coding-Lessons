function ladyBugs(arr) {
    let sizeOfField = arr[0];
    let ladybugsPositions = arr[1]
        .split(' ')
        .map(Number);
    let ladybugsArray = [];

    // fill the array with 0
    for (let i = 0; i < sizeOfField; i++) {
        ladybugsArray.push(0);
    }
    // mark starting ladybugs index
    for (let i = 0; i < sizeOfField; i++) {
        let ladybugIndex = ladybugsPositions[i];
        if (ladybugIndex >= 0 && ladybugIndex < sizeOfField) {
            ladybugsArray[ladybugIndex] = 1;
        }
    }

    for (let i = 2; i < arr.length; i++) {
        // JS destructuring
        let [ladybugIndex, command, jumpLength] = arr[i].split(' ');
        ladybugIndex = +ladybugIndex;
        jumpLength = +jumpLength;

        if (ladybugsArray[ladybugIndex] !== 1 || ladybugIndex < 0 || ladybugIndex >= ladybugsArray.length) {
            continue;
        }
        // check for negative steps
        if (jumpLength < 0) {
            jumpLength = Math.abs(jumpLength);
            if (command === 'right') {
                command = 'left';
            } else if (command === 'left') {
                command = 'right';
            }
        }
        // Free Position
        ladybugsArray[ladybugIndex] = 0;
        if (command === 'right') {
            // Ladybug jumps one time
            let newPosition = ladybugIndex + jumpLength;
            // Jump another time if there is a lady bug
            if (ladybugsArray[newPosition] === 1) {
                newPosition = newPosition + jumpLength;
            }
            if (newPosition <= ladybugsArray.length) {
                ladybugsArray[newPosition] = 1;
            }

        } else {
            // Lady bug jumps to the left
            let newPosition = ladybugIndex - jumpLength;
            // Jump another time if there is a lady bug
            if (ladybugsArray[newPosition] === 1) {
                newPosition = newPosition - jumpLength;
            }
            if(newPosition >= 0 ){
                ladybugsArray[newPosition] = 1;
            }
        }

    }

    console.log(ladybugsArray.join(' '));

}
ladyBugs(   [ 5, '3',
    '3 left 2',
    '1 left -2']
);
