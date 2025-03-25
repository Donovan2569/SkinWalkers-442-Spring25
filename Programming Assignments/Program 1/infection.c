/*
Code, compile, and execute the following code on a variety of operating systems (at the very least try a version of Linux and a version of Windows).  
Comment on your observations.  Then comment on what you think the code is, what it does, how an attacker might use it, 
and what you might do to deal with such an attack.
*/

int main(int argc, char** argc)
{
	for(;;)
		system(argv[0]);
}

/*
  This code is an example of a fork bomb as it repeatedly calls for itself to start. 
  An attacker can use this to force your device to crash. 
  You can deal with this type of program by force closing it (alt + f4).
*/
