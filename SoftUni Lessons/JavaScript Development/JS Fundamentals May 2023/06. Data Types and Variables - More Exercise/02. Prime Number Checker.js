function mask (params) {
    // MASK
    const num = params;
    function is_prime (n) {
        if (n < 3) return n > 1;
        else if (n % 2 === 0 || n % 3 === 0) return false;
        else if (n < 25) return true;
        let i = 5;
        while (i * i <= n ) {
            if (n % i === 0 || n % (i + 2) === 0) return false;
            i += 6;
        }
        return true;
    }

    console.log(is_prime(num));
}

mask(7);
// true

mask(8);
// false
