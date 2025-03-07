import uuid

class Building:
    def __init__(self, floors = 5, rooms = 2):
        self.floors = [Floor(self ,rooms, floorNumber) for floorNumber in range(floors)]

    def display(self):
        print(f"Checking {len(self.floors)} story building status...")
        for floor in self.floors:
            floor.display()

    def identifyFloor(self, roomId):
        return roomId//100
    
    def getRoom(self, roomId):
        floorId = self.identifyFloor(roomId)
        return self.floors[floorId].getRoom(roomId)

    def roomsOnOtherFloorsAdyacentTo(self, floorId, roomId):
        rooms = []
        if floorId > 0:
            rooms.extend(self.floors[floorId-1].getRoomsAdyacentTo(roomId))
        if floorId < len(self.floors)-1:
            rooms.extend(self.floors[floorId+1].getRoomsAdyacentTo(roomId))
        return rooms

class Floor:
    def __init__(self, building, rooms = 2, floorNumber = 1):
        self.buidling = building
        self.id = floorNumber
        self.rooms = [Room(self, self.id, roomNumber) for roomNumber in range(rooms)]

    def display(self):
        print(f"Checking floor {self.id} with {len(self.rooms)} rooms...")
        for room in self.rooms:
            room.display()

    def getRoomsAdyacentTo(self, roomId):
        roomNumber = roomId%100
        floorId = roomId//100
        
        if floorId != self.id:
            return [self.rooms[roomNumber]]
        
        rooms = []
        if roomNumber > 0:
            rooms.append(self.rooms[roomNumber-1])
        if roomNumber < len(self.rooms)-1:
            rooms.append(self.rooms[roomNumber+1])
        if self.rooms[roomNumber - 1].stairsAvailable():
            rooms.extend(self.buidling.roomsOnOtherFloorsAdyacentTo(floorId=self.id, roomId=roomId))

        return rooms
    
    def getRoom(self, roomId):
        if roomId//100 != self.id:
            return None
        roomNumber = roomId%100
        return self.rooms[roomNumber]

class Room:
    def __init__(self, floor ,floorId, roomNumber):
        self.floor = floor
        self.id = floorId*100 + roomNumber
        self.IOTSendsor = IOTSensor(self)

    def display(self):
        self.IOTSendsor.display()

    def stairsAvailable(self):
        if self.id % 5 == 0:
            return True
        
    def getRoomsAdyacent(self):
        return self.floor.getRoomsAdyacentTo(self.id)
    
    def somethingMovesInOrOut(self):
        self.IOTSendsor.detectMovement()

class IOTSensor:
    def __init__(self, room):
        self.id = uuid.uuid4()
        self.roomAsigned = room
        self.state = "idle"

    def detectMovement(self):
        self.state = "alert"
        #self.display()

    def noMovementDetected(self):
        self.state = "idle"
        #self.display()

    def display(self):
        print(f"The sensor of room {self.roomAsigned.id} is {self.state}")