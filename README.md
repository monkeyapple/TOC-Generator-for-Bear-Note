# TOC-Generator for Bear Note
TOC-Generator is a tool for generating TOC(Table of contents) for Bear Note users.

## Current Version
V1.0

### V1.0 Functionalities
* Generate Markdown TOC(Table of contents) for Bear Note (with Jump links)
* Customize the position of points in unordered list 
  

## How to Install & Run
**Option1:**
* Clone or download the git repository
```
$ git clone https://github.com/monkeyapple/TOC-Generator-for-Bear-Note.git
```
* Create and activate a virtual environment:
```
$ virtualenv venv
$ source venv/bin/activate
```
* Install the requirements inside the app folder
```
$ pip install -r requirements.txt
```
* Run the main.py file
```
$ python main.py
```
**Option2:** download and run executable files(Mac or Windows) in **/dist** folder

*For Mac Users, firstly **unzip** the file, double click and a pop-up dialog box with message shown as:
![Screenshot](/images/Image09.png)
*Solution:System Preferences-->Security & Privacy-->General-->Open Anyway

## User Interface
![Screenshot](/images/Image08.png)

## How to use
1. Copy Note's Identifier: Bear Note-->Menu-->Note-->Copy Note's Identifier
2. Export Note into HTML file: Bear Note-->File-->Export Notes-->HTML file
3. Input Indentifier and import HTML file into TOC-Generator
4. (optional) Customize points before Headings
5. Run and Copy generated TOC, then paste it into Bear Note
![Screenshot](/images/Image04.png)

**Example of result**
![Screenshot](/images/Image03.png)


## License
GPL v3 license
