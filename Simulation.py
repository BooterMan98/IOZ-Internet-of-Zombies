import random
import BuildingStructure

class Simulation:
  def __init__(self, floors, rooms):
    self.building = BuildingStructure.Building(floors, rooms)
    self.zombies =[Zombie(self)]
    self.zombies[0].currentRoom = self.getinitialRoomForOutbreak()

  def getinitialRoomForOutbreak(self):
    return self.building.floors[0].rooms[0].id

  def playSimulationTurn(self):
    zombiesCopy = self.zombies.copy()
    for zombie in zombiesCopy:
      action = zombie.doSomething()
      if action[0] == "expand":
        for room in action[1]:
          newZombie = Zombie(self)
          newZombie.currentRoom = room.id
          room.somethingMovesInOrOut()
          self.zombies.append(newZombie)
          #print(f"Zombies have expanded to room {room.id}")
      elif action[0] == "move":
        room = self.building.getRoom(action[1])
        #print(f"Zombie has moved to room {room.id}")
        room.somethingMovesInOrOut()
      else:
        pass

  def getRoomDestinations(self, roomId):
    room = self.building.getRoom(roomId)
    return room.getRoomsAdyacentTo(roomId)
  
  def displayBuilding(self):
    self.building.display()

  def displayFloor(self, floorId):
    self.building.displayFloor(floorId)

  def displayRoom(self, roomId):
    self.building.displayRoom(roomId)
  

class Zombie:
  def __init__(self, simulation):
    self.simulation = simulation
    self.currentRoom = None



  def doSomething(self):
    rooms = []
    if self.currentRoom is None:
      return None
    else:
      rooms = self.simulation.building.getRoom(self.currentRoom).getRoomsAdyacent()
      if len(rooms) == 0:
        return
    doImoveOrExpand = bool(random.getrandbits(1))
    if doImoveOrExpand:
      self.currentRoom = rooms[random.randint(0, len(rooms)-1)].id
      return ("move", self.currentRoom)
    else:
      return ("expand", rooms)