import unittest
import json
from icecream import ic
from classes.stats import Stats



########################################################################
############ Tests on class Stats
class TestStats(unittest.TestCase):

  stats = Stats()
  stats0 = Stats(GoalKeeping=0,
                 Defending=0,
                 Passing=0,
                 PlayMaking=0,
                 Winging=0,
                 Scoring=0,
                 SetPiecing=0)
  stats100 = Stats(GoalKeeping=100,
                   Defending=100,
                   Passing=100,
                   PlayMaking=100,
                   Winging=100,
                   Scoring=100,
                   SetPiecing=100)
  statsGoalKeeper = Stats(GoalKeeping=100,
                          Defending=50,
                          Passing=50,
                          PlayMaking=50,
                          Winging=50,
                          Scoring=50,
                          SetPiecing=50)

########################################################################
############ Tests Methods
###### Tests on average calculation of players
  def test_AvgCalculation_Player100_Error_Seeker(self):
    with self.assertRaises(Exception) as context:
      self.stats.AvgScore(Position= "Seeker")
    self.assertTrue("[Seeker] doesn't exist in the list ['GoalKeeper', 'Defender', 'BackWinger', 'MidFielder', 'Winger', 'Scorer']" in str(context.exception))
  def test_AvgCalculation_Player100_Error_Goalkeeper(self):
    with self.assertRaises(Exception) as context:
      self.stats.AvgScore(Position= "Goalkeeper")
    self.assertTrue("[Goalkeeper] doesn't exist in the list ['GoalKeeper', 'Defender', 'BackWinger', 'MidFielder', 'Winger', 'Scorer']" in str(context.exception))

  def test_AvgCalculation_Player100_All(self):
    self.assertEqual(self.stats100.AvgScore(Position= "All"), 100)
  def test_AvgCalculation_Player100_None(self):
    self.assertEqual(self.stats100.AvgScore(), 100)
  def test_AvgCalculation_Player100_GoalKeeper(self):
    self.assertEqual(self.stats100.AvgScore(Position= "GoalKeeper"), 100)
  def test_AvgCalculation_Player100_Defender(self):
    self.assertEqual(self.stats100.AvgScore(Position= "Defender"), 100)
  def test_AvgCalculation_Player100_BackWinger(self):
    self.assertEqual(self.stats100.AvgScore(Position= "BackWinger"), 100)
  def test_AvgCalculation_Player100_MidFielder(self):
    self.assertEqual(self.stats100.AvgScore(Position= "MidFielder"), 100)
  def test_AvgCalculation_Player100_Winger(self):
    self.assertEqual(self.stats100.AvgScore(Position= "Winger"), 100)
  def test_AvgCalculation_Player100_Scorer(self):
    self.assertEqual(self.stats100.AvgScore(Position= "Scorer"), 100)

###### Tests that for each player average calculation, the sum of weights equals 1
  def test_AvgCalculation_Weight_GoalKeeper(self):
    self.assertEqual(sum(self.stats.tabCalculatePlayerAvg["GoalKeeper"].values()), 1)
  def test_AvgCalculation_Weight_Defender(self):
    self.assertEqual(sum(self.stats.tabCalculatePlayerAvg["Defender"].values()), 1)
  def test_AvgCalculation_Weight_BackWinger(self):
    self.assertEqual(sum(self.stats.tabCalculatePlayerAvg["BackWinger"].values()), 1)
  def test_AvgCalculation_Weight_MidFielder(self):
    self.assertEqual(sum(self.stats.tabCalculatePlayerAvg["MidFielder"].values()), 1)
  def test_AvgCalculation_Weight_Winger(self):
    self.assertEqual(sum(self.stats.tabCalculatePlayerAvg["Winger"].values()),1)
  def test_AvgCalculation_Weight_Scorer(self):
    self.assertEqual(sum(self.stats.tabCalculatePlayerAvg["Scorer"].values()),1)

###### Tests on best position calculation
  def test_AvgCalculation_BestPosition_GoalKeeper_Error(self):
    with self.assertRaises(Exception) as context:
      self.stats.AvgScore(Position= "GoalKeeper", returnPos= True)
    self.assertTrue("When returning best position of a player, Position must be None or [ALL], Position was: [GoalKeeper]" in str(context.exception))

  def test_AvgCalculation_BestPosition_GoalKeeper(self):
    self.assertEqual(self.statsGoalKeeper.AvgScore(Position= "All", returnPos= True), "GoalKeeper")
  def test_AvgCalculation_BestPosition_GoalKeeper2(self):
    self.assertEqual(self.statsGoalKeeper.AvgScore(returnPos= True), "GoalKeeper")

###### Tests on strings
  def test_str(self):
    self.assertEqual(str(self.stats100), "GoalKeeping=100, Defending=100, Passing=100, PlayMaking=100, Winging=100, Scoring=100, SetPiecing=100")

  def test_JSON(self):
    output = {
      "Defending": 100,
      "GoalKeeping": 100,
      "Passing": 100,
      "PlayMaking": 100,
      "Scoring": 100,
      "SetPiecing": 100,
      "Winging": 100}
    self.assertEqual(self.stats100.toJSON(), json.dumps(output, default=lambda o: o.__dict__, sort_keys=True, indent=4))