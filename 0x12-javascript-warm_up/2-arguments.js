#!/usr/bin/node
/*
Commandline arguments in js is use the process.argv
which is an array containing all arguments of the CLI.
process.argv[0] = absolute path to the node binary file
process.argv[1] = absolute file path to the .js fie
process.argv[2] = users passed in arguments.
*/
if (process.argv.length < 3){
	console.log('No argument');
}
else if (process.argv.length === 3){
	console.log('Argument found');
}
else{
	console.log('Arguments found');
}
