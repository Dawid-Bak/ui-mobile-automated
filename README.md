### **UI tests automation for android applications using pytest and appium**

Appium is an HTTP server written in node.js which creates and handles multiple WebDriver sessions for platforms like iOS and Android. One of the core tenets of Appium is that test codes can be written in any framework or programming language without having to modify the apps for automation purposes. The interaction between node.js server and Selenium client libraries is what ultimately works together with the mobile application.

#### **Setting up automation environment for testing on Ubuntu 18.04 with use of Appium, pytest and real device with android.**

**1. Install node.js - without sudo**
  
Do not install node.js through apt or apt-get, which will need sudo rights and appium will not work if node.js is installed as sudo user. If you have already installed remove it using commands on terminal:	
  
    sudo apt remove nodejs
    sudo apt remove npm

**1a. Installing linuxbrew**

The way of installing node.js that worked for me was by using linuxbrew.

_Notice: Installation of node.js using brew can take as long as 20 minutes or more._
  
To install linuxbrew on your system, start from installing necessary dependencies, by running in your terminal:

	sudo apt install build-essential curl file git
  
Next run:

	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
  
Next step is to add Homebrew to PATH and to your bash shell profile script by running:

	test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
	test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
	test -r ~/.profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
	echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile

**1b. Installing node.js using brew**

Start installation process by running on your terminal:

	sudo apt install m4 ruby texinfo libbz2-dev libcurl4-openssl-dev libexpat-dev libncurses-dev zlib1g-de
  
_Notice: Node.js and npm requires GCC (GNU Compiler Collection) but it was installed in previous step with build-essential package._

Next run:

	brew install node

**2. Install Appium**

Appium can be installed and operated from terminal or we can download Appium Desktop, which is a graphical, desktop-based way to launch the Appium server. 

I've notice that performing of tests is slower when the server was started using GUI interface, compared to one started from terminal. On the other side Appium Desktop allows to easily locate selectors from the application, therefore I recommend to install it both ways.

**2a. Installation via Desktop App Download**

Simply download the latest version of Appium Desktop (in AppImage format) from the releases page.

	https://github.com/appium/appium-desktop/releases

**2b. Configuring AppImage file**

Before you can run an AppImage, you need to make it executable:

**With the GUI**

    1. Open your file manager and browse to the location of the AppImage 
    
    2. Right-click on the AppImage and click the ‘Properties’ entry
    
    3. Switch to the Permissions tab and 
    
    4. Click the ‘Is executable’ checkbox (if you are using Dolphin)
    
    5. Close the dialog 
    
    6. Double-click on the AppImage file to run 
    
**On the terminal**

	chmod a+x Name.AppImage
  
**2c. Installation via npm in terminal**

Run the command on your terminal:

	npm install -g appium

**3. Install appium-doctor**

Diagnose and fix common Node, iOS and Android configuration issues before starting Appium.

Run the command on your terminal:

	npm install appium-doctor -g
  
To start diagnostic run:

	appium-doctor --android
  
The result of the diagnosis may indicate the need to set PATH for JAVA_HOME and ANDROID_HOME. If so go to steps 3a and 3b.

**3a. Install OpenJDK 8**

Check if you have Java in your system by running command in terminal:

	java -version
  
If you don’t have it installed, than run:

	sudo apt install openjdk-8-jdk
  
If you have it installed configure the environment variables. In general, java gets installed at /usr/lib/jvm:

Run in terminal:

	nano ~/.bashrc
  
Scroll to the end of document and write:

	export JAVA_HOME="/usr/lib/jvm/folder-name-of-distiburtion"
	export PATH="$PATH:$JAVA_HOME/bin"
  
Save the document and run in terminal:

	source ~/.bashrc

**3b. Download and configure Android-SDK** 

Download sdk-tools from:

https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip

Create folder ‘android-sdk’ in directory of your choice. 

Copy ‘tools’ folder from downloaded package into the newly created ‘android-sdk’ folder.

Download platform-tools from:
	https://developer.android.com/studio/releases/platform-tools

Copy ‘tools’ folder from downloaded package into the newly created ‘android-sdk’ folder.


Configure environment variables:

Run in terminal:

    nano ~/.bashrc

Scroll to the end of document and write:

	export ANDROID_HOME="/home/user-name/location-of-folder/android-sdk"
	export ANDROID_SDK_ROOT="/home/user-name/location-of-folder/android-sdk"
	export PATH="$PATH:$ANDROID_HOME/tools/bin"	
	export PATH="$PATH:$ANDROID_HOME/platform-tools"

Save the document and run in terminal:

	source ~/.bashrc


### **Running tests on real device with android**

You can copy whole project ‘ui-mobile-automated’ from this repository and execute tests on terminal or after loading project in IDE you are using. Either way make sure to install necessary packages listed in requirements.txt, wheter globally or in virtualenv of your system or in the IDE interpreter.

#### **Steps to run tests on terminal:**

1.Enable USB Debugging on your device. 

To do that:
- go to the Settings
- touch About phone
- touch Build number several times in succession until the phone indicates you have entered developer mode
- return to the Settings
- touch Developer options
- swipe Developer options to the ON position, and enable USB debugging

2.Connect device through USB and “Allow access to phone data”

3.Confirm if the device is connected and get your device name by running in terminal:
	
	adb devices

4.Provide values for desired capabilities like:

“deviceName” in the config.py file located in project, with the name of your device,
  
“app” in the config.py file located in project, with directory of apk file in project, i.e.     
"/path/to/project/folder/ui-mobile-automated/tests/app/pierwszaApka.apk"

To start appium server simply run in terminal:

	appium

Open another terminal and set the directory which contains test files, i.e.:	
      
      /~directory/where/you/downloaded/my/repository/ui-mobile-automated/tests$

And run:

	py.test
  

Enjoy




Source:

  http://appium.io/docs/en/about-appium/getting-started/
  
  https://discourse.appimage.org/t/how-to-run-an-appimage/80
  
  https://www.toolsqa.com/mobile-automation/appium/download-and-install-nodejs/
  
  https://medium.com/testcult/configuring-appium-in-ubuntu-from-scratch-a9f8edc02d13
  
  https://confusedcoders.com/general-programming/mobile/how-to-install-appium-in-ubuntu
  
  https://docs.brew.sh/Homebrew-on-Linux
  
  https://github.com/appium/appium-doctor
