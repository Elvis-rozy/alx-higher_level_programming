#!/usr/bin/node
/*Commandline arguments in javascript use the process.argv
which contains arguments in the CLI.from process.argv[0] - 
process.argv[2] being the user paseed in the arguments.
*/
if (process.argv.length < 3) {
	console.log('No argument');
}
else if (process.argv.length === 3){
	console.log('Argument found');
}
else {
	console.log('Arguments found');
