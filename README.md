# BlueQubit Hackathon 2025
I recently took part in BlueQubit's Quantum Peaked Circuits Hackathon.
I'm still just an enthusiast and by no means a professional, but I was able to get the first two problems correct (full marks 🥳 - first submissions) using this simple code.

## Problem One
I just tried to 'translate' the `.qasm` code into Python code that I could then send to the computer and emulate.
This was a fair bit of trial and error, but I managed to get it in the end.

## Problem Two
I tried the same approach as the problem above, but I quickly gave up as the `.qasm` file was around 2,000 lines long.
Instead, I made a 'converter' program which tries to convert the `.qasm` file into a qiskit circuit in Python (DISCLAIMER: this 'converter' will not work on all `.qasm` files but was intended only for the one given in the problem).
This (surprisingly) worked and although it took around a minute to simulate, it gave me the correct peak bitstring.

# Note
Importantly, this code is very likely not the best or most optimal way to find these solutions.
Once the hackathon was over and we were free to discuss, others mentioned that they used Bloch Spheres and other much more advanced techniques to find the peak bitstring - this is just a demonstration of how I did it for anyone interested.

Included in the repository are the two folders for the two problems, each of which has the solution in a Python program called `<ProblemNumber>.py`, along with the respective `.qasm` file and any other code I used to get to the solution.

That's it (I think)!
