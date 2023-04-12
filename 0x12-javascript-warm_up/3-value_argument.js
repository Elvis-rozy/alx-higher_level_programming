#!/usr/bin/node
const variable = process.argv[2];
if (process.argv.length >== 3){
	console.log(variable);
}
else {
	console.log('No argument');
}
