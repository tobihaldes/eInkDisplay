# Project: E-Ink Smart Display 
The ‘E-Ink Smart Display’ is an open source project that is being developed by students at DHBW Heilbronn as part of the Project Conception module until the end of the 6th semester. The aim is to realise a smart display that can present various information via an e-ink display using interface queries.

# A brief overview of the APIs implemented in the project
![API](https://github.com/tobihaldes/eInkDisplay/assets/165897037/4c04f5b3-3efd-4f3e-9c81-d4414eddf892)

# The core functions of the display include
### Weather display: 
Presentation of weather information using icons, numbers and text. 
### Date display: 
Display of the current date in dd.mm.yyyy format. 
### Clock: 
Synchronised time based on the atomic clock for maximum accuracy. 
### Calendar: 
Visualisation of important dates such as birthdays, doctor's appointments and deadlines.
### Stock Price Display:
Display of current stock prices.
### News Feed:
Display of current news in text form.
### To-Do List:
Display of a list of tasks.
### Wi-Fi Connectivity

## Installing: 
A step by step series of examples that tell you how to get a development env running:

### Setting Up Thonny for Raspberry Pi Pico Development

#### Step 1: Downloading and Installing Thonny
1. Visit the official Thonny website: [Thonny.org](https://thonny.org/)
2. Download the appropriate version of Thonny for your operating system.
3. Follow the installation instructions provided on the website to install Thonny. Choose the 'Standard' initial settings during installation.

#### Step 2: Connecting the Raspberry Pi Pico
1. Ensure that MicroPython is already installed on your Raspberry Pi Pico. If not, follow the instructions on the [Raspberry Pi website](https://www.raspberrypi.org/documentation/microcontrollers/micropython.html) to install it.
2. Connect the Raspberry Pi Pico to your PC using a micro USB cable. Your PC should recognize the Pico as a removable storage device.

#### Step 3: Configuring Thonny for Raspberry Pi Pico
1. Open Thonny.
2. From the bottom-right of the Thonny window, click on the interpreter currently selected (usually Python 3). A new window will pop up.
3. In the new window, select 'MicroPython (Raspberry Pi Pico)' from the list of interpreters.
4. Confirm that the port listed is the one connected to your Raspberry Pi Pico and click 'OK'.

#### Step 4: Accessing Files on the Raspberry Pi Pico
1. To view files stored on the Pico, go to the 'View' menu and select 'Files'. This will open a file explorer pane in Thonny.
2. In the file explorer pane, files and folders on the Pico will be indicated by parentheses. Files and folders not in parentheses are located on your local machine.

#### Step 5: Editing and Running Code
1. You can now create new Python scripts or edit existing ones directly in Thonny.
2. To run the code on your Raspberry Pi Pico, simply click the 'Run' button in Thonny.
3. Your code will execute directly on the Raspberry Pi Pico, and you'll be able to interact with it through the Thonny interface.

#### Tips
- Remember to save your work frequently to the Pico or locally, as per your project requirements.
- Use the 'Stop' button in Thonny to halt the execution of scripts if needed.

#### Troubleshooting
- If the Raspberry Pi Pico is not recognized by your PC, try reconnecting it or using a different USB cable.
- Ensure that the correct drivers are installed if your PC does not recognize the Pico.

### Contributing: 
Learn more about contributing to this Project in the [CONTRIBUTING.md](CONTRIBUTING.md) file

### Authors: 
Tobias Haldenwanger, Leon Karais, Jorim Bonk, Paul Schlestein, Lionel Mössinger

### Licence: 
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
