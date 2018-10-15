# NbodySim
The goal of this code is to relatively accurately simulate a system with N bodies that have mass.
Currently I'm using Euler's method of integration so you can expect some orbital drifting because the errors won't cancel out.
The plots are also not a series of images but rather one image with drawn circles (the paths of bodies), I will change this when I figure out how disable automatic canvas rescaling in matplotlib.
You can also make a simple json file for easier input, especially if you want to change the lenght or other parameters of the simulation frequently.
