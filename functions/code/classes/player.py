from stats import Stats
from datetime import datetime, timedelta
import json
import random
from icecream import ic


########################################################################
########################################################################
############ Class for player
class Player:

########################################################################
########################################################################
###### Table to generate player stats
  tabGeneratePlayer = { #Table to generate player stats
    "GoalKeeper": {
      "GoalKeeping": {"min": 10, "max": 30},
      "SetPieces": {"min": 0, "max": 20}},
    "Defender": {
      "Defending": {"min": 10, "max": 30},
      "PlayMaking": {"min": 0, "max": 20}},
    "BackWinger": {
      "Defending": {"min": 10, "max": 30},
      "Winging": {"min": 0, "max": 20}},
    "Midfielder": {
      "PlayMaking": {"min": 10, "max": 30},
      "Defending": {"min": 0, "max": 20}},
    "Winger": {
      "Winging": {"min": 10, "max": 30},
      "PlayMaking": {"min": 0, "max": 20}},
    "Scorer": {
      "Scoring": {"min": 10, "max": 30},
      "PlayMaking": {"min": 0, "max": 20}},
  }

########################################################################
########################################################################
###### Generate new player
  def create(self, FirstName, LastName, Position=None, Age=None, ClubId=None):
###### Initial Checks
### FirstName checks
    if FirstName is None:
      raise Exception(f"ERROR: LastName is mandatory when generating player element (Class Player)")
### LastName checks
    if LastName is None:
      raise Exception(f"ERROR: LastName is mandatory when generating player element (Class Player)")
### Age checks
    if Age is None:
      Age = random.randint(17, 35)
    elif Age < 17 or Age > 35:
      raise Exception(f"ERROR: Age [{Age}] is not between 17 and 35")
### Position checks
    if Position is None:
      Position = random.choice(list(self.tabGeneratePlayer.keys()))
    elif Position not in self.tabGeneratePlayer:
      raise Exception(f"ERROR: Position [{Position}] doesn't exists in the list of possible positions")
###### Calculations
### Age calculation
    if Age is None:
      Age = random.randint(17, 35)
    DateBirth = datetime.now() - timedelta(days= int(Age * 112)) # (1 game season = 16 real life weeks = 112 real life days)
### Stats calculation
    PlayerStats = Stats().generatePlayerStats(Position, Player.tabGeneratePlayer[Position])
### Salary calculation
    Salary = Stats.Salary(BaseSalary= 500)

###### Store data
    self.FirstName = FirstName
    self.LastName = LastName
    self.DateBirth = DateBirth
    self.Salary = Salary

########################################################################
########################################################################
###### Player stats calculation

########################################################################
########################################################################
###### Init method
  def __init__(self,
               FirstName=None,
               LastName=None,
               DateBirth=None,
               Country=None,
               ClubId=None,
               ClubArrival=None,
               Salary=None,
               Form=None,
               Stamina=None,
               Experience=None,
               Stats=None,
               Position=None,
               PlayerId=None,
               isCreation=False):
    self.FirstName = FirstName
    self.LastName = LastName
    self.DateBirth = DateBirth
    self.Country = Country
    self.ClubId = ClubId
    self.ClubArrival = ClubArrival
    self.Salary = Salary
    self.Form = Form
    self.Stamina = Stamina
    self.Experience = Experience
    self.Stats = Stats

    if self.FirstName is None:
      raise Exception("ERROR: LastName is mandatory when generating player element (Class Player)")
    if self.LastName is None:
      raise Exception("ERROR: LastName is mandatory when generating player element (Class Player)")
    if self.DateBirth is None:
    


  def __str__(self):
    return f"{self.FirstName} {self.LastName} {self.DateBirth} {self.Country} {self.ClubId} {self.ClubArrival} {self.Salary} {self.Form} {self.Stamina} {self.Experience}"
