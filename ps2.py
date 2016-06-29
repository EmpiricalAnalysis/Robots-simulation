# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

#import numpy as np

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        
        # 0 in floorArea means that the tile has not been cleaned
        
        self.floorArea = [[0 for x in range(height)] for x in range(width)] 
        #self.floorArea = np.zeros( (width, height) ) 
        
        #raise NotImplementedError
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        
        #self.floorArea[pos.getX(), pos.getY()] = 1
        self.floorArea[int(pos.getX())][int(pos.getY())] = 1
        
        #raise NotImplementedError

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        
        #return self.floorArea[m, n] == 1
        return self.floorArea[m][n] == 1
        
        #raise NotImplementedError
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        
        #return self.floorArea.size
        return len(self.floorArea) * len(self.floorArea[0])
        
        #raise NotImplementedError

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        
        nCleanTiles = 0
        
        #for i in self.floorArea.shape[0]:
        #    nCleanTiles += sum(self.floorArea[i, :])
        
        #print len(self.floorArea)
        #print range(len(self.floorArea))
        
        for i in range(len(self.floorArea)):
            nCleanTiles += sum(self.floorArea[i][:])
        
        return nCleanTiles
        
        #raise NotImplementedError

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        
        #random.seed(0)
        
        return Position(random.random()*len(self.floorArea), random.random()*len(self.floorArea[0]))
        
        #raise NotImplementedError

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        
        #print len(self.floorArea)
        #print len(self.floorArea[0])
        
        
        #if pos.getX() < 0 or pos.getX() >= self.floorArea.shape[0]:
        if pos.getX() < 0 or pos.getX() >= len(self.floorArea):
            return False
            
        #if pos.getY() < 0 or pos.getY() >= self.floorArea.shape[1]:
        if pos.getY() < 0 or pos.getY() >= len(self.floorArea[0]):
            return False
        
        return True
        
        #raise NotImplementedError


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        
        self.room = room
        self.speed = speed
        
        self.pos = self.room.getRandomPosition()
        self.room.cleanTileAtPosition(self.pos)
        
        self.dir = random.random()* 360.0
        
        #raise NotImplementedError

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        
        return self.pos
        
        #raise NotImplementedError
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        
        return self.dir
        
        #raise NotImplementedError

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        
        self.pos = position
        
        #raise NotImplementedError

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        
        self.dir = direction
        
        #raise NotImplementedError

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        #print "robot speed is: " + str(self.speed)
        
        newPos = self.pos.getNewPosition(self.dir, self.speed)
        newDir = self.dir
        
        #print "newPos is: "+str(newPos)
        #print "newDir is: "+str(newDir)
                    
        while not self.room.isPositionInRoom(newPos):
            newDir = random.random()*360.0
            newPos = self.pos.getNewPosition(newDir, self.speed)
            
        self.pos = newPos
        self.room.cleanTileAtPosition(self.pos)
        self.dir = newDir
        
        #raise NotImplementedError

# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    trialSteps = []
    
    for i in range(num_trials):
        
        #print "i = " + str(i)
        room = RectangularRoom(width,height)
        nTiles = room.getNumTiles()
            
        robotList = []
        nCleaned = 0
        nSteps = 0
        
        for j in range(num_robots):
            robotList.append(robot_type(room, speed))
            nCleaned += 1
        
        """
        # The following codes are useful to calculat #s conforming to the problem 
        # guidelines, but they yield the wrong results when submitted to test cases.
        # For test cases, simply use updatePositionAndClean()
        
        nSteps = 1
        while nCleaned/float(nTiles) < min_coverage:
            nSteps += 1
            for j in range(num_robots):
                #robotList[j].updatePositionAndClean() 
                jRobot = robotList[j]
                newPos = jRobot.getRobotPosition().getNewPosition(jRobot.getRobotDirection(), speed)
                newDir = jRobot.getRobotDirection()
                nSteps += 1
                while not room.isPositionInRoom(newPos):
                    newDir = random.random()*360.0
                    newPos = jRobot.getRobotPosition().getNewPosition(newDir, speed)
                    #nSteps += 1
                jRobot.setRobotPosition(newPos)
                room.cleanTileAtPosition(jRobot.getRobotPosition())
                jRobot.setRobotDirection(newDir)
            
            nCleaned = room.getNumCleanedTiles()
        """
        while nCleaned/float(nTiles) < min_coverage:
            nSteps += 1
            for j in range(num_robots):
                robotList[j].updatePositionAndClean()
            nCleaned = room.getNumCleanedTiles()
        
        #print nSteps
  
        trialSteps.append(nSteps)
    
        #print sum(trialSteps)
 
    return math.floor(sum(trialSteps) / float(num_trials))
                
    
    #raise NotImplementedError

# Uncomment this line to see how much your simulation takes on average
#print  runSimulation(1, 1.0, 5, 5, 0.78, 30, StandardRobot)
#print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        newDir = random.random()*360.0
        newPos = self.pos.getNewPosition(newDir, self.speed)
        
        #print "newPos is: "+str(newPos)
        #print "newDir is: "+str(newDir)
                    
        while not self.room.isPositionInRoom(newPos):
            newDir = random.random()*360.0
            newPos = self.pos.getNewPosition(newDir, self.speed)
            
        self.pos = newPos
        self.room.cleanTileAtPosition(self.pos)
        self.dir = newDir
        
        #raise NotImplementedError
        
#testRobotMovement(RandomWalkRobot, RectangularRoom)


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#showPlot1("time steps to clean 80% of room vs. # of Robots", "# of Robots", "time steps to clean 80% of room")


#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
#showPlot2("time steps to clean 80% of room vs. Aspect Ratio of Room", "Aspect Ratio of Room", "time steps to clean 80% of room")
