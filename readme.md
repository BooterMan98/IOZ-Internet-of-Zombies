# IoZ - Internet of Zombies

> A simple simpulator that tracks the zombie outbreak as it expands on a building with the help of some IoT Sensors!

## How to run:

1. Clone this repo and `cd` into the proyect folder.
2.   ```$ python3 ./main.py```

## What can you do?

These are the commands you can use. when runing the simulator you'll be asked to enter a command, enter the folowing numbers to do the following actions.

- 1: Generate a building with `n` floors and `m` rooms per floor
- 2: Check the status of each room by it's sensor
- 3: Pass the time. Make the inevitable happen and let the zombies advance through the building
- 4 Exit the simulation

## Assumptions and Restrictions

- **Floors** can have **up to 99 rooms**
- Rooms that end with 0 or 5 have stairs, so zombies can go up or down
- **Floors and Rooms go from 0 and up**. That is, buildings with 5 rooms with 5 floors will have the floor 0 and room 0,  the top floor will be the 4th floor and the last room wil end in 4 as in `room 404`.
- Zombies can move and expand to rooms that have already a zombie in it
- Sensors only detects when a zombie is entering a room. its state will remain alert till the next turn happens and will return to idle if no zombie moves in again. This also means that the original room it's unknown


## Implementation

There are 6 classes implemented for this proyect:  

`Building`,
`Floor`,
`Room`,
`IOTSensor`,
`Simulator` and
`Zombie`

The `Building`,
`Floor`,
`Room` and 
`IOTSensor` instances are the building infrastructure, so they only manage information about the building itself, which is mainly used for retrieving information about sensors and adyacent rooms.  
The `Zombie` instances only move between rooms or expands to new roms with new instances in that case.

So, as zombies doesn't know anything about sensors, how does the sensor knows a zombie entered a room?  In real life, the sensor is reading constantly with the data it gathers and when it detects something it raises and alert and changes it's state. This is *simulated* here through the `Simulation` instance. Whenever a zombie tell the simulator that it wants to move to a room, the Zombie gets moved to the room and the simulator tells the respecting `Sensor` the movement has been made by calling a function.
