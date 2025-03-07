from Simulation import Simulation
import sys

def main():
  ### Main loop
  simulation = None
  while True:
    command = int(input("Insert a command: \n"))
    if command == 1:
      simulation = setupBuilding(simulation)
    elif command == 2:
      viewBuildingState(simulation)
    elif command == 3:
      playSimulation(simulation)
    elif command == 4:
      exit()

#### Commands:

def setupBuilding(simulation):
    if simulation == None:
      floorNumber = int(input("Enter Floor quantity:\n"))
      roomNumber = int(input("Enter Room quantiy per floor:\n"))
      responce = f"""The building will have {floorNumber} floors and {roomNumber} rooms in each floor, is this correct?
      y for yes, n for no.
      """
      command = input(responce)
      if command == "y":
        simulation = Simulation(floorNumber, roomNumber)
        return simulation
    else:
      print("There is already a building in place")
    return None
def viewBuildingState(simulation):
  if simulation != None:
    simulation.building.display()
  else:
    print("There is no building in place")

def playSimulation(simulation):
  if simulation != None:
    simulation.playSimulationTurn()
  else:
    print("There is no building in place")

def exit():
  sys.exit()

######## Other commands

def saveState():
  pass

def loadState():
  pass







if __name__ == "__main__":
  main()