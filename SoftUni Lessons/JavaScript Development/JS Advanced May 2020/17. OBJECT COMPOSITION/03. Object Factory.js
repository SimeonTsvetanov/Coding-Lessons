function objectFactory(data) {
    return JSON.parse(data).reduce((a, o) => ({...a, ...o}), {});
}

console.log(objectFactory(`[{"canMove": true},{"canMove":true, "doors": 4},{"capacity": 5}]`));
// Should Return: { canMove: true, doors: 4, capacity: 5 }

console.log(objectFactory(`[{"canFly": true},{"canMove":true, "doors": 4},{"capacity": 255},{"canFly":true, "canLand": true}]`));
// Should Return: { canFly: true, canMove: true, doors: 4, capacity: 255, canLand: true }