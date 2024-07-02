![](assets/logo.png?v=1&type=image)
## Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration

<br>
<div align="center">
Junyang Wang<sup>1</sup>, Haiyang Xu<sup>2†</sup>,Haitao Jia<sup>1</sup>, Xi Zhang,<sup>2</sup>
</div>
<div align="center">
Ming Yan<sup>2†</sup>, Weizhou Shen<sup>2</sup>, Ji Zhang<sup>2</sup>, Fei Huang<sup>2</sup>, Jitao Sang<sup>1†</sup>
</div>
<div align="center">
{junyangwang, jtsang}@bjtu.edu.cn, {shuofeng.xhy, ym119608}@alibaba-inc.com
</div>
<br>
<div align="center">
<sup>1</sup>Beijing Jiaotong University    <sup>2</sup>Alibaba Group
</div>
<div align="center">
<sup>†</sup>Corresponding author
</div>

<div align="center">
<a href="README.md">English</a> | <a href="README_zh.md">简体中文</a>
<hr>
</div>
<!--
English | [简体中文](README_zh.md)
<hr>
-->

## 📢News
[6. 4] We proposed [Mobile-Agent-v2](https://arxiv.org/abs/2406.01014), a mobile device operation assistant with effective navigation via multi-agent collaboration.

## 📺Demo
https://github.com/X-PLUG/MobileAgent/assets/127390760/d907795d-b5b9-48bf-b1db-70cf3f45d155

## 📋Introduction

![](assets/role.jpg?v=1&type=image)
* A multi-agent architecture addresses the challenges of navigation in long-context input scenarios.
* An enhanced visual perception module significantly improves operation accuracy.
* Performance and speed are further enhanced with the support of GPT-4o.

## 🔧Getting Started

❗At present, only **Android OS** and **Harmony OS** (version <= 4) support tool debugging. Other systems, such as **iOS**, do not support the use of Mobile-Agent for the time being.

### Installation
```
pip install -r requirements.txt
```

### Preparation for Connecting Mobile Device with ADB

1. Download the [Android Debug Bridge](https://developer.android.com/tools/releases/platform-tools?hl=en).
2. Turn on the ADB debugging switch on your Android phone, it needs to be turned on in the developer options first.
3. Connect your phone to the computer with a data cable and select "Transfer files".
4. Test your ADB environment as follow: ```/path/to/adb devices```. If the connected devices are displayed, the preparation is complete.
5. If you are using a MAC or Linux system, make sure to turn on adb permissions as follow: ```sudo chmod +x /path/to/adb```
6. If you are using Windows system, the path will be ```xx/xx/adb.exe```

### Install the ADB Keyboard on your Mobile Device
1. Download the ADB keyboard [apk](https://github.com/senzhk/adbkeyboard/blob/master/adbkeyboard.apk) installation package.
2. Click the apk to install on your mobile device.
3. Switch the default input method in the system settings to "ADB Keyboard".

### Choose the Appropriate Execution Method for Your Needs

1. Locate the "Edit your Setting" section starting at line 22 in ```run.py```, and input your ADB path, instruction, GPT-4 API URL, and Token.

2. Choose the call method of icon caption model suitable for your device:
	-  If your device is equipped with a high-performance GPU, we recommend using the "local" method. It refers to deploying the icon caption model in your local device. If your equipment is strong enough, it often has better efficiency.
	-  If your device is not enough to run a 7B LLM, choose the "api" method. We use parallel calls to ensure efficiency.

3. Choose the caption model :
	- If you choose the "local" method, you need to choose between "qwen-vl-chat" and "qwen-vl-chat-int4", where the "qwen-vl-chat" requires more GPU memory but offers better performance compared to "qwen-vl-chat-int4". At the same time, "qwen_api" can be vacant.
	- If you choose the "api" method, you need to choose between "qwen-vl-plus" and "qwen-vl-max", where the "qwen-vl-max" requires more expenses but offers better performance compared to "qwen-vl-plus". In addition, you also need to apply for [Qwen-VL API-KEY](https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key) and input it in "qwen_api".

4. You can add operational knowledge (for example, to complete the specific steps you need to instruction) in "add_info" to help Mobile-Agent operate more accurately.

5. If you want to further improve the efficiency of Mobile-Agent, you can set "reflection_switch" and "memory_switch" to "False".
	- "reflection_switch" is used to determine whether to add the "reflection agent“ in the process. This may cause operation to fall into a dead cycle. But you can add operational knowledge to "add_info" to avoid it.
	- "memory_switch" is used to decide whether to add the "memory unit" to the process. If your instruction don't need the information that are used for subsequent operations, you can turn it off.

### Run
```
python run.py
```

## 📑Citation

If you find Mobile-Agent useful for your research and applications, please cite using this BibTeX:
```
@article{wang2024mobile2,
  title={Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration},
  author={Wang, Junyang and Xu, Haiyang and Jia Haitao and Zhang Xi and Yan, Ming and Shen, Weizhou and Zhang, Ji and Huang, Fei and Sang, Jitao},
  journal={arXiv preprint arXiv:2406.01014},
  year={2024}
}
```
