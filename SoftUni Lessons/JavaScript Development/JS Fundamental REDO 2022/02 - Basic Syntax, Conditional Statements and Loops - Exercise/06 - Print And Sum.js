function print_and_sum(start, end) {
    let nums = []
    for(let num = start; num <= end; num++) { nums.push(num); }
    console.log(nums.join(' '));
    console.log(`Sum: ${nums.reduce( (x,y) => x+y, 0)}`);
}

print_and_sum(5, 10);