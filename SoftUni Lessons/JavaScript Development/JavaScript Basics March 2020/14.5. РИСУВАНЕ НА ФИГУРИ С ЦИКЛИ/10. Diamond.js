// Short link: https://git.io/Jvxr4

function diamond(input) {
    // Mask
    let n = Number(input.shift());
    let leftRight = Math.floor((n - 1) / 2);
    
    for (let i = 1; i <= (n - 1) / 2; i++) {
        let bra = '-'.repeat(leftRight) + '*';
        let mid = n - 2 * leftRight - 2;
        if (mid >= 0) { bra += '-'.repeat(mid) + "*"; }
        bra += '-'.repeat(leftRight);
        leftRight--;
        console.log(bra); 
    }

    for (let j = (n - 1) / 2; j >= 0 ; j--) {   
        let panties = '-'.repeat(leftRight) + "*";
        let mid = n - 2 * leftRight - 2;
        if (mid >= 0) { panties += '-'.repeat(mid) + "*"; }
        panties += '-'.repeat(leftRight);
        leftRight++;
        console.log(panties);
    }
}

diamond([8]);  // Should return:
// ---**---
// --*--*--
// -*----*-
// *------*
// -*----*-
// --*--*--
// ---**---

diamond([6]);  // Should return:
// --**--
// -*--*-
// *----*
// -*--*-
// --**--
