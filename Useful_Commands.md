# **Useful Commands**

## Flutter
### Check health state on flutter
flutter doctor


## Firebase
### Start emulators
firebase emulators:start

### Start emulators with parameters to have basic data in the generated local database
firebase emulators:start --import C:\Users\pgranger\git\testFlutterApp\emulator\data --export-on-exit

### Deploy project on server
firebase deploy --only functions


## Python unittest
### Test
**Must be on path /functions/code**
__Run all tests__
python -m unittest discover -v
__Run a single test__
python -m unittest tests.test_stats.TestStats.test_AvgCalculation_Weight_GoalKeeper