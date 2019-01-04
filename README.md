# NbodySim

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/63f8fa523dfb40809a4aadc4180fdd01)](https://app.codacy.com/app/andrija.radica/NbodySim?utm_source=github.com&utm_medium=referral&utm_content=xXxGandalf420xXx/NbodySim&utm_campaign=Badge_Grade_Settings)

The goal of this code is to relatively accurately simulate a system with N bodies that have mass.
Currently I'm using Euler's method of integration so you can expect some orbital drifting because the errors won't cancel out.
The plots are live with the option to save them (a folder is automagically generated).
You can also make a simple json file for easier input, especially if you want to change the lenght or other parameters of the simulation frequently.
TODO: 
- Barnes-Hut implementation - from O(n^2) to O(n) complexity
- faster output, option to save raw data for later plots
- gui?