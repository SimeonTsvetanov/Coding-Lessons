function tickets(input, criteria) {
    // Mask
    let tickets = [];

    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = +price;
            this.status = status;
        }
    }

    input.map(data => {
        let [destination, price, status] = data.split('|');
        tickets.push(new Ticket(destination, price, status))
    });

    criteria === 'destination' ? tickets = tickets.sort((a, b) => a.destination.localeCompare(b.destination)) : 'ass';
    criteria === "price" ? tickets = tickets.sort((a, b) => a.price - b.price): 'pass';
    criteria === "status" ? tickets = tickets.sort((a, b) => a.status.localeCompare(b.status)) : 'or gas';
    return tickets;
}

console.log(tickets([
        'Philadelphia|94.20|available',
        'New York City|95.99|available',
        'New York City|95.99|sold',
        'Boston|126.20|departed'],
    'destination'));

console.log(tickets(['Philadelphia|94.20|available',
        'New York City|95.99|available',
        'New York City|95.99|sold',
        'Boston|126.20|departed'],
    'destination'));