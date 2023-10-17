import json
import random
from icecream import ic


########################################################################
########################################################################
############ Class for player stats
class Stats:
  
########################################################################
########################################################################
###### Table of available positions and stats
  lisPositions = ["GoalKeeper", "Defender", "BackWinger", "Midfielder", "Winger", "Scorer"]
  lisStats = ["GoalKeeping", "Defending", "Passing", "PlayMaking", "Winging", "Scoring", "SetPiecing"]

###### Try with pandas dataframe ?
###  tabAvgWeights = {
####                 GoalKeeping, Defending, Passing, PlayMaking, Winging, Scoring, SetPiecing
###    "GoalKeeper": [   .5     ,    .1    ,  .1    ,    .05    ,  .05   ,  .05   ,   .15],
###    "Defender"  : [   .05    ,    .5    ,  .2    ,     .1    ,  .05   ,  .05   ,   .05],
###    "BackWinger": [   .05    ,    .4    ,  .15   ,     .1    ,   .2   ,  .05   ,   .05],
###    "MidFielder": [   .05    ,    .1    ,  .25   ,    .35    ,   .1   ,   .1   ,   .05],
###    "Winger"    : [   .05    ,    .1    ,   .2   ,     .2    ,  .35   ,  .05   ,   .05],
###    "Scorer"    : [   .05    ,    .05   ,  .15   ,    .15    ,  .15   ,   .4   ,   .05]
###  }
###  tabAvgWeights = pd.DataFrame(data= tabAvgWeights, index = lisStats)

########################################################################
########################################################################
###### Table to calculate player average stats
  tabCalculatePlayerAvg = {  # Table to calculate player average stats
      "GoalKeeper": {
          "GoalKeeping": .5,
          "Defending": .1,
          "Passing": .1,
          "PlayMaking": .05,
          "Winging": .05,
          "Scoring": .05,
          "SetPiecing": .15
      },
      "Defender": {
          "GoalKeeping": .05,
          "Defending": .5,
          "Passing": .2,
          "PlayMaking": .1,
          "Winging": .05,
          "Scoring": .05,
          "SetPiecing": .05
      },
      "BackWinger": {
          "GoalKeeping": .05,
          "Defending": .4,
          "Passing": .15,
          "PlayMaking": .1,
          "Winging": .2,
          "Scoring": .05,
          "SetPiecing": .05
      },
      "MidFielder": {
          "GoalKeeping": .05,
          "Defending": .1,
          "Passing": .25,
          "PlayMaking": .35,
          "Winging": .1,
          "Scoring": .1,
          "SetPiecing": .05
      },
      "Winger": {
          "GoalKeeping": .05,
          "Defending": .1,
          "Passing": .2,
          "PlayMaking": .2,
          "Winging": .35,
          "Scoring": .05,
          "SetPiecing": .05
      },
      "Scorer": {
          "GoalKeeping": .05,
          "Defending": .05,
          "Passing": .15,
          "PlayMaking": .15,
          "Winging": .15,
          "Scoring": .4,
          "SetPiecing": .05
      }
  }

########################################################################
########################################################################
###### Init function
  def __init__(self,
               GoalKeeping=None,
               Defending=None,
               Passing=None,
               PlayMaking=None,
               Winging=None,
               Scoring=None,
               SetPiecing=None):
    self.GoalKeeping = GoalKeeping
    self.Defending = Defending
    self.Passing = Passing
    self.PlayMaking = PlayMaking
    self.Winging = Winging
    self.Scoring = Scoring
    self.SetPiecing = SetPiecing


########################################################################
########################################################################
###### Generate player stats
  def generatePlayerStats(self, Position = None):
#### Initial checks
    if Position == None: #If no position was given in input
      Position = random.choice(list(self.tabGeneratePlayer.keys())) #We generate a position
    elif Position not in list(Stats.tabGeneratePlayer.keys()): #If the input position is unknown
      raise Exception(f"[{Position}] doesn't exist in the list {list(Stats.tabCalculatePlayerAvg.keys())}")
#### Generate stats
    for keyPosition in list(Stats.tabGeneratePlayer.keys()): #Loop through each position
      if keyPosition == Position: #If the position is the same as the input
        for stat in Stats.lisStats: #Loop through each stat
          self.stat=

########################################################################
########################################################################
###### Calculate the average score of player
  def Salary(self, BaseSalary=0):
    return BaseSalary + self.GoalKeeping + self.Defending + self.Passing + self.PlayMaking + self.Winging + self.Scoring + self.SetPiecing

########################################################################
########################################################################
###### Calculate the average score of player
  def AvgScore(self, Position = None, returnPos = False):
#### Initial checks of inputs
    if Position is None or Position.upper() == "ALL": # No input for position means ALL
      Position = "ALL"
    elif Position not in list(Stats.tabCalculatePlayerAvg.keys()): #If the input position is not in the table tabCalculatePlayerAvg
      raise Exception(f"[{Position}] doesn't exist in the list {list(Stats.tabCalculatePlayerAvg.keys())}")
    if returnPos is True and Position != "ALL": #When returning BestPosition, always calculate every possible positions (with ALL)
      raise Exception(f"When returning best position of a player, Position must be None or [ALL], Position was: [{Position}]")
#### Calculation of the average score of the player
    if Position.upper() == "ALL": #If we dont have any input for position (or "all")
      Position = Stats.tabCalculatePlayerAvg.keys() #We will calculate the best average score of the given player
    AvgScoreBest = None #Init
    PositionBest = None #Init
    for keyPosition in Stats.tabCalculatePlayerAvg: #loop through each position of the table [GoalKeeper, Defender, BackWinger, MidFielder, Winger, Scorer]
      if keyPosition in Position: #If we find the position in the list
        AvgScore = .0 #Init average score
        for keyStat in Stats.tabCalculatePlayerAvg[keyPosition]: #Loop through each stats [GoalKeeping, Defending, Passing, PlayMaking, Winging, Scoring, SetPiecing]
          AvgScore += Stats.tabCalculatePlayerAvg[keyPosition][keyStat] * self.__getattribute__(keyStat) #Update average score
        if AvgScoreBest is None or AvgScore > AvgScoreBest: #If the current average score is better than the best one
          AvgScoreBest = AvgScore #Store new best average score
          PositionBest = keyPosition #Store the best position
#### End function
    if AvgScoreBest is None: #This error shouldn't arrive
      raise Exception(f"Average Score cannot be calculated for Position input = {Position}")
      #return f"ERROR Unhandled: Average Score cannot be calculated for Position input = {Position}"
    if returnPos is True: #If we want to return the best position instead of average score
      return PositionBest
    return AvgScoreBest

########################################################################
########################################################################
###### String and JSON methods
  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
  
  def __str__(self):
    return f"GoalKeeping={self.GoalKeeping}, Defending={self.Defending}, Passing={self.Passing}, PlayMaking={self.PlayMaking}, Winging={self.Winging}, Scoring={self.Scoring}, SetPiecing={self.SetPiecing}"

