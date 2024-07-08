## 🎬 Get started
### Installation
```
git clone https://github.com/FreedomIntelligence/TikTokAgent.git
cd MobileAgent
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
First, go to controller.py and change the command to suit you based on the environment you are using.
Then, run the command, set counter to the filename (test + counter) you want to begin in (you can change the filename where the data goes), the address the address to the folder MobileAgent-main, the 
```
python controller1.py --counter "_" --address "address to MobileAgent-main" --grounding "groundingdino path" --description "demographic description --adb "adb path" --api "api key"
```

```
python run_api.py --adb_path /path/to/adb --url "The url you got" --token "The token you got" --instruction "your instruction"
```
