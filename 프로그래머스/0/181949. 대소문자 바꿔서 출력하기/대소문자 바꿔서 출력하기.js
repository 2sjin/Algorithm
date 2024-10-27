const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

for (let i=0; i<input.length; i++) {
    let ch = input[i]
    if (ch === ch.toUpperCase())
        ch = ch.toLowerCase();
    else
        ch = ch.toUpperCase();
        process.stdout.write(ch);
}