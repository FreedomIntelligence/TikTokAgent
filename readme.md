This is the code to mimic the scrolling of different demographics, detect inappropriate content that they might encounter, and assess its impact on them


## 🎬 Get started
### Installation
```
git clone https://github.com/FreedomIntelligence/TikTokAgent.git
cd MobileAgent-main
pip install -r requirements.txt
```
### Connecting to Mobile Device
1. Obtain and Install ADB:
Download the Android Debug Bridge (ADB) tool from the official Android developer website.

2. Enable Developer Options on Your Android Device

3. Activate USB Debugging:
In Developer Options, find and enable "USB debugging".

4. Connect Your Android Device:
Use a USB cable to connect your Android device to your computer. When prompted on your device, select "File Transfer" mode.

5. Verify ADB Connection:
Open a terminal or command prompt on your computer and type:
```
/path/to/adb devices
```
if your device is listed then it was successful

7. Set Proper Permissions (macOS/Linux only):
On macOS or Linux, you may need to set execution permissions for ADB. Use this command
```
sudo chmod +x /path/to/adb
```

Windows-Specific Note:
On Windows systems, you'll use "adb.exe" instead. The command might look like:
```
C:\path\to\adb.exe devices
```

### Run
Next, go to ProgramController.py and change the command to suit you based on the environment you are using. You may also change addresses and files in the MobileAgent-main folder and the run.py file to match the ProgramController's code.
Then, run the command, set the counter to the number in the filename (test + counter) you want to begin in (you can change the filename where the data goes), the address to the folder MobileAgent-main, the groundingdino path, the demographic description of the person, and the API key that you have been provided.
```
python ProgramController.py --counter _num_ --address /path/to/MobileAgent-main --grounding /path/to/GroundingDINO --description "demographic description" --adb /path/to/adb --api "your api key"
```

### Impact Assessment
```
python FindingTheEffects.py --filePath /path/to/MobileAgent-main --startingNum _num_ --api "your api key" --description "demographic description" 
```

### Accessing Historical Database
```
python HistoricalDatabase.py --filePath /path/to/MobileAgent-main --startingNum _num_ --part "What part you are looking for (ex. Thought, Action)"
```
