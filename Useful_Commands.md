# **Useful Commands**

## Flutter
### Check health state on flutter
flutter doctor


## Firebase
### Start emulators
firebase emulators:start

### Start emulators with parameters to have basic data in the generated local database
firebase emulators:start --import C:\Users\pgranger\git\testFlutterApp\emulator\data --export-on-exit
firebase emulators:start --import C:\Users\pgranger\git\testFlutterApp\emulator\data

### Deploy project on server
firebase deploy --only functions

## Python venv
### Activate venv
.\venv\Scripts\Activate

## Python unittest
### Test
**Must be on path /functions/code**
__Run all tests__
python -m unittest discover -v
__Run a single test__
python -m unittest tests.test_stats.TestStats.test_AvgCalculation_Weight_GoalKeeper