# badapy


## Overview
A python library impolementing the EUROCONTROL BADA calculations. To load OPF and APF Files as well as calculating the fuel flow and total fuel consumption for cruise flight.

- Free software: MIT license
- Documentation: Work in Progress

## Classes

- Airplane: 
- Flight

## Requirements

This library does not provide the necessary Data-Files from EUROCONTROL. They need to be obtained seperately.


## Usage


### Loading Airplanes
First we need to create and load the information of the specific airplane type provided by the EUROCONTROL dataset.
```python
import badapy as bd
B373 = bd.Airplane('B373', 'Boeing B737-300')
B373.load_information('data/OPF/')  # Eurocontrol Data location

```

### Running fuel calculations
Based on the previously loaded airplane data, the individual flights can be created.
```python
flight_1 = bd.Flight('D743', '666', B737)
flight_1.load_flightdata("/data/flightdata.csv")  # Path to file with flight data
flight_1.calculate_fuel() 

```