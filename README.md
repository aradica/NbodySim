# NbodySim

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/01d6dc700cda45039cb16f661422389a)](https://www.codacy.com/app/andrija.radica/NbodySim?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=xXxGandalf420xXx/NbodySim&amp;utm_campaign=Badge_Grade)

The goal of this code is to relatively accurately simulate a system with N bodies that have mass.
Currently I'm using Euler's method of integration so you can expect some orbital drifting because the errors won't cancel out.
The plots are live with the option to save them (a folder is automagically generated).
You can also make a simple json file for easier input, especially if you want to change the lenght or other parameters of the simulation frequently.
TODO: 
- Barnes-Hut implementation - from O(n^2) to O(n) complexity
- faster output, option to save raw data for later plots
- gui?
