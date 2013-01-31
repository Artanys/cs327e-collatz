Project #1: Collatz
Date: Wed, 30 Jan 2013, 8pm

Course Name: CS327e
Unique: 53355

First Name: Jordan
Last Name: Naumann
EID: jtn395
E-mail: jordan.naumann@gmail.com
Estimated number of hours: 3
Actual    number of hours: 12

Turnin CS Username: jtn395
GitHub ID: Artanys
GitHub Repository Name: cs327e-collatz

Comments: 
Program itself did not take very long at all to write. Most of my time was spent figuring out Github and trying to get my UTCS accound activated on the linux machines. I used Visual Studio 2012 and their Python add-in to write my code, as well as conduct profiling during execution. Fastest time was 2.36 on Sphere, which was strangely before the added performance improvements. Perhaps my improvements, which added .06 seconds to the time, are only noticed when the inputs to the program overlap (e.g. "1000 10000\n5000 10000\n").

In attempting to run my solution for V2 of the problem, I received a timout error. I then implemented a meta-cache as described in class by calculating max cycle lengths for groups of numbers. In my case, the granularity was 125 numbers (e.g. max cycle for 1-125, 126-250, etc.), all the way to 1 million. My program became at least 10 times faster for V1 of the problem, as times varied from .27 seconds down to .08 seconds. I still could not get my solution to solve V2. I was told that Sphere expects certain values to overflow the bounds of a 32-bit signed int (which is what python uses, and then converts to a long (bignum) upon overflow). I couldn't jerry-rig my solution to simulate overflow in time to submit.

---------------
Code of Conduct
---------------

I attest that I have written every line of code that I have submitted
and I take full responsibility for the origin of all the code submitted.
In particular, if any of the code was originally written in a previous
semester or another course I will so acknowledge via e-mail to the
grader.
