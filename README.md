# NbodySim
The goal of this code is to relatively accurately simulate our Solar system, or any system with gravitationally attracted objects.

It's still a lot of work in progress! This was an older project but I decided to make it human readable.
so I wrote it from scratch again :D

It doesn't containt key features such as initial parameter loading from a file (json or something nice), and frame export (data and plots). 

And example of what I would like it to do in the next version is to read something like this and do its magic...

{
    "header": {
        "type": "input",
        "engineVersion": 0.1,
        "framesToCalculate": 365,
        "frameDuration": 86400,
        "units": {
            "mass": "kg",
            "coordinates": ["cartesian", "m"],
            "velocity": "m/s"
        }
    },
    "objects": {
        "Earth": {
            "mass": 5.9722E24,
            "coordinates": [149597870700, 0, 0],
            "velocity": [0, 30000, 0]},
        "Moon": {
            "mass": 7.34767309E22,
            "coordinates": [149597870700, 384400000, 0],
            "velocity": [-900, 30000, 0]
        },
        "Sun": {
            "mass": 1.9891E30,
            "coordinates": [0, 0, 0],
            "velocity": [0, 0, 0]
        }
    }  
}

