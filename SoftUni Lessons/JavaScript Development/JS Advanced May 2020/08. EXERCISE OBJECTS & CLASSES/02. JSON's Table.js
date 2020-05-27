function jsonsTable(input) {
    // Mask - https://git.io/JfreM
    let employees = [];
    input.map(data => employees.push(JSON.parse(data)));
    let result = '<table>\n';
    employees.forEach(employee => {
        result += `\t<tr>\n` + Object.values(employee).map(value => result += `\t\t<td>${value}</td>\n`) + `\t</tr>\n`;
    })
    result += '</table>';
    console.log(result);
}

jsonsTable([
    '{"name":"Pesho","position":"Promenliva","salary":100000}',
    '{"name":"Teo","position":"Lecturer","salary":1000}',
    '{"name":"Georgi","position":"Lecturer","salary":1000}']
);
// Should return:
// <table>
//  <tr>
//      <td>Pesho</td>
//      <td>Promenliva</td>
//      <td>100000</td>
//  </tr>
//  <tr>
//      <td>Teo</td>
//       <td>Lecturer</td>
//      <td>1000</td>
//  </tr>
//  <tr>
//      <td>Georgi</td>
//      <td>Lecturer</td>
//      <td>1000</td>
//  </tr>
// </table>
