const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

let str = input[0];
let n = input[1];

for (let i=0; i<n; i++) {
    process.stdout.write(str);
}