# TOC-Generator for Bear Note
TOC-Generator is a tool for generating TOC(Table of contents) for Bear Note users.

## Current Version
V1.0

### V1.0 Functionalities
* Generate Markdown TOC(Table of contents) for Bear Note (with Jump links)
* Customize the position of points in unordered list 
  
## Requirements
* beautifulsoup4==4.9.1
* PyQt5==5.15.0

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

## Install and Run
**Option1:** download and run executable files(Mac or Windows) in **/dist** folder

*For Mac Users, firstly **unzip** the file, then double click.
*There will be an alert in a pop-up window shown as:
![Screenshot](/images/Image09.png)
*Solution:System Preferences-->Security & Privacy-->General-->Open Anyway

**Option2:** download all necessary souce code files and run **main.py** 


## License
GPL v3 license
