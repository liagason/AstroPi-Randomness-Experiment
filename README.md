# An Astro Pi Randomness Experiment in Space

## About
The code is part of a school project that participated in the Astro Pi Mission Space Lab 2019/20.
The expiriment was conducted by students of the 17th Elementary School of Agrinio and their mentor.

## Info on the project
The code collects data from the magnetometer/gyroscope/accelerometer/temperature/pressure/humidity sensors and saves them in two files (data01.csv, data03.csv). This data is used as "seed" in order to produce random integers from 0 to 9, that are saved in data02.csv and data04.csv. All values, in their raw form, are used as "seed" to produce random integers using Python's Mersenne Twister algorithm as generator. After that, these values get "hashed", using Python's SHA256 hash function, in order to get more entropic and then used, again as "seed", to produce another series of random integers between 0 and 9. The objective of this experiment is to collect data in order to analyze it back on Earth and determine if using values of natural phenomena as seed is an effective way to produce random numbers in the controlled enviroment of the ISS.
