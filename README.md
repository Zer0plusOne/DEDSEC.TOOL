
# DEDSEC.TOOL

Free use tool and open source made with the objective of achieving what I'd like to describe as a Swiss Army Knife to have all diferent functions in a easy acces tool by entering diferent inputs without the needing of having all the tools separately.

I will be adding new functions and features to make the tool more and more complete, adding the posibility to misc some functions with the objective of developing new functions.

Add to this, that the tool is inspired in the first game of "Watch Dogs" developed by Ubisoft, so the aesthetics of the tool will be related to this.

# ToDo List

This is a project actually under developement, so i leave a quick list of all the things i want to implement. With a simple color status about how the developement is going

#### Color scheme:

| Color Code         | Meaning          |
| :-----------: | :--------------       |
|🔴|Not Under developement              |
|🟠|Trying to figure how to implement   |
|🟡|Under Developement                  |
|🟢|Developed but pending of upgrades   |
|🔵|Developed and published             |

## ToDo List

|  Developement Status | Difficulty Level (Developing) | Functionality| Description |
|:--------------------:|:----------------:|--------------|-------------|
| 🔴 | Easy| **Show detailed information about the system where it runs**| This feature will provide information about the hardware, software, and system configurations of the device running the tool.|
| 🔴 | Easy | **Ping execution for specified targets**| A simple utility that allows the user to ping an IP address or domain name to check its availability and latency.|
| 🔴 | Medium| **Provide information about a specific IP**| This function will gather and display information related to the specified IP address, such as geographical location, ISP, and other relevant details.|
| 🔴 | Medium| **Scan ports of a specific IP**| This feature will check the open ports on a given IP address, helping users to identify potential vulnerabilities.|
| 🔴 | Medium| **Search relationships between web domains**| This functionality will analyze domain names and provide insights into possible connections or relationships between different domains.|
| 🔴 | Hard| **OSINT features similar to existing repositories**| This will include various OSINT functionalities such as data gathering, user tracking, and additional intelligence-gathering capabilities based on public information.|
| 🔴 | Hard| **Integration with Metasploit for reverse shells**| This feature will allow users to send reverse shells to specified IPs and ports, utilizing Metasploit’s capabilities for exploitation.|
| 🔴 | Insane| **Network traffic analysis**| This advanced feature will monitor and analyze network traffic in real-time, providing insights into data flows and potential security issues.|
| 🔴 | Insane| **Vulnerability scanning**| Implementing a tool that scans systems or networks for known vulnerabilities, helping users to enhance their security posture.|
| 🔴 | Insane| **Automated security audits** | This feature will automate the process of conducting security audits, generating reports based on the findings.|
| 🔴 | CEH| **Malware analysis**| A feature dedicated to analyzing suspected malware, determining its behavior, and identifying potential threats to systems.|
| 🔴 | CEH| **Simulation of attacks**| This will allow users to simulate various types of cyberattacks in a controlled environment to test the resilience of systems.|
| 🔴 | CEH| **Password management**| An integrated password manager that helps users store, generate, and manage passwords securely.|
| 🔴 | CEH| **Phishing module**| A feature designed to create phishing simulations for educational purposes, helping users learn to recognize and avoid phishing attacks.|
| 🔴 | CEH| **Logging monitoring**| This function will monitor system logs for suspicious activities, helping users to detect potential threats early.|
| 🔴 | CEH| **Geolocation services integration**| Integration with geolocation services to provide geographical context for IP addresses and domains.|
| 🔴 | CEH| **Training and education in cybersecurity**| Resources and tools for educating users about cybersecurity best practices and potential threats.|

## Installation

Cloning via GitHub (be sure to have installed the git suit in your device)

```bash
sudo apt-get install git
```

### CLONING

```bash
git clone https://github.com/Zer0plusOne/DEDSEC.TOOL
```

Be sure to have python V3.0 installed

```bash
sudo apt-get install python3
```

## Opening the TOOL

Be sure to be in the tool directory

```bash
cd DEDSEC.TOOL
```

Executing the tool

```bash
python3 main.py
```

If having issues with the permisions (strange but could happen)

```bash
sudo python3 main.py
```

## Usage of the tool

The usage of this tool is free now and forever, if you paid for anything related for this tool, sorry but you got scammed.

If you use this tool and like the idea please feel free to post new features, also feel free to contact me in the contact ways i have enabeled in my GitHub profile. I'll add also the @ to my discord below if you want to contact me more privately.

# MIT License

## Copyright (c) 2023 Zer0plusOne

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## License link

[MIT LICENSE LINK](https://choosealicense.com/licenses/mit/)

### Discord: @zer0who


![Logo](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c167faae-9537-4b4d-a6b3-2a3b9fa80cb2/db019p5-7a48b5b1-71af-45d9-96e5-9808cee53e70.png/v1/fill/w_1024,h_576,q_75,strp/dedsec_by_default_01101100_011-db019p5.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl0sIm9iaiI6W1t7InBhdGgiOiIvZi9jMTY3ZmFhZS05NTM3LTRiNGQtYTZiMy0yYTNiOWZhODBjYjIvZGIwMTlwNS03YTQ4YjViMS03MWFmLTQ1ZDktOTZlNS05ODA4Y2VlNTNlNzAucG5nIiwid2lkdGgiOiI8PTEwMjQiLCJoZWlnaHQiOiI8PTU3NiJ9XV19.P20RBbbtjs1KgML2Ctx9_ySYf8JWI77c1S5el8Aj6Uk)
