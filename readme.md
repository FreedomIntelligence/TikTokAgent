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
