from Simulation import Simulation
import sys

def main():
  ### Main loop
  simulation = None
  help = """
  Commands:
  create - Create a building
  check - Check building status
  play - Play simulation
  exit - Exit program
  """
  print(help)
  while True:
    command = input("Insert a command: \n")
    if command == "create":
      simulation = setupBuilding(simulation)
    elif command == "check":
      viewBuildingState(simulation)
    elif command == "play":
      playSimulation(simulation)
    elif command == "exit":
      exit()
    else:
      print("Invalid command")
      print(help)

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
    choice = input("Enter if you want to check floor status, a specific room or the whole building: [b/f/r]\n")
    ## TODO: create method for geting floor and room status
    choice = choice.lower()
    choice = choice.strip()
    if choice == "f":
      floor = int(input("Enter the floor number:\n"))
      simulation.displayFloor(floor)
    elif choice == "r":
      room = int(input("Enter the room number:\n"))
      simulation.displayRoom(room)
    elif choice == "b":
      simulation.displayBuilding()
    else:
      print("Invalid choice")
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