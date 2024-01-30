#!/usr/bin/node

const fs = require('fs');
let data = process.argv[3];

fs.writeFile(process.argv[2], data, 'utf-8');
