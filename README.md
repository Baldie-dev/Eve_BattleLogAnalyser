# Eve_BattleLogAnalyser

## How to use

1. Eve Battle logs can be found in `\Documents\EVE\logs\Gamelogs`
2. Before doing benchmark, please delete all files there (you can do it even if Eve is running).
3. Go attack some sites with drones
4. After you are finish, take the log file and copy it to the same folder with the script
5. Edit `CalcDPS.py` and change the name of the log file on the first line:
```
log = "Sample_Log.txt"
```
6. Run the script:
```
python CalcDPS.py
```
