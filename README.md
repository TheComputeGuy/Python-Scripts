# Python-Scripts
1. gmail-auto-login: A script to login to GMail (can be customised for any site by changing some params) automatically and save time     (Currently works for **Chrome**). Install the latest version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and save the .py file in the same folder as the .exe of the driver. Run the script and automate your login. Don't forget to change the username and password by editing in an IDE or IDLE.
2. Webmail_notifier: A script to notify new emails in NITT Webmail on Windows using toast notifications. Uses selenium and win10toast libraries on ChromeDriver.
3. All-Zip-Extractor: A script to extract contents of all zip archives in a given directory. No additional libraries needed.
4. morse_encode_decode: A python3 program to:
                        1. Encode plain text (A-Z, a-z, 0-9, ' ', '.', ',', '?') and play using Python winsound library (**WINDOWS ONLY**)
                        2. Decode morse code to plain text (A-Z, a-z, 0-9, ' ', '.', ',', '?')
5. results: A script to parse semester results of NIT Trichy. Takes rollnumber and password as inputs. Uses requests library.
6. way2sms: A script to automate sending SMS via way2sms. Made for Festember, NIT Trichy inductions. Reads CSV files to personalise message with name and slot for inductions. Built upon [this](http://home.iitk.ac.in/~saiwal/productivity/send-sms-way2sms-python/).
7. Excel reconfigure: A script to automatically modify excel worksheets (especially form data) to make different rows for different parameters filled by the same individual. Made for separating individuals team-wise from a single google form response sheet for Festember, NIT Trichy. Uses openpyxl library.
