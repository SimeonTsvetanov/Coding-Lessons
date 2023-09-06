function mask (params) {
    // MASK
    const c = params;
    const y = c * 100;
    const d = Math.trunc(y * 365.2422);
    const h = 24 * d;
    const m = 60 * h;

    console.log(`${c} centuries = ${y} years = ${d} days = ${h} hours = ${m} minutes`);
}

mask(1);
// 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes

mask(5);
// 5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes
