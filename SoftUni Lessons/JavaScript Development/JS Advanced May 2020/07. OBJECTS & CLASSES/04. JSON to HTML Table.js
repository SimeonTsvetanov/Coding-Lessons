function solve(data) {
    // Not mine solution... But this task is Stupid...
    function escapeHtml(unsafe) {
        return unsafe.toString()
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#39;");
    }

    const products = JSON.parse(data);
    let result = `<table>\n   <tr>`

    const keys = Object.keys(products[0]);
    result = keys.reduce((acc, key) => {
        acc += `<th>${escapeHtml(key)}</th>`;
        return acc;
    }, result)

    result += `</tr>\n`;


    for (const product of products) {
        result += `   <tr>`;
        for (const key of keys) {
            result += `<td>${escapeHtml(product[key])}</td>`;
        }
        result += `</tr>\n`;
    }

    return result += `</table>`;
}
