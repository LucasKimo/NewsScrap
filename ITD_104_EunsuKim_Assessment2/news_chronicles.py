#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 11804815 # put your student number here as an integer
student_name   = "Eunsu Kim (Lucas)" # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/) and CopyDetect
#  (https://copydetect.readthedocs.io/en/latest/index.html). [2C3202]
#
#--------------------------------------------------------------------#


#-----Task Description-----------------------------------------------#
#
#  News Chronicles
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  This assignment can be completed using these functions only.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# may be solvable with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# Import the date and time function.
# This module *may* be useful, depending on the websites you choose.
# Eg convert from a timestamp to a human-readable date:
# >>> datetime.fromtimestamp(1586999803) # number of seconds since 1970
# datetime.datetime(2020, 4, 16, 11, 16, 43)
from datetime import datetime

# A module with useful functions on pathnames including:
# normpath: function for 'normalising' a  path to a file to the path-naming
# conventions used on this computer.  Apply this function to the full name
# of your HTML document so that your program will work on any operating system.
# realpath: function to get full absolute path to a file.
# exists: returns True if the supplied path refers to an existing path
from os.path import *

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd

# NOTE: DO NOT import any other modules without the express
# permission of the client.

#-----Preamble-------------------------------------------------------#
#
# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()


#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  You are not required to use this function, but it may
# save you some effort.  Feel free to modify the function or copy
# parts of it into your own code.
#
# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.  However, the root cause of the
# problem is not always easy to diagnose, depending on the quality
# of the response returned by the web server, so the error
# messages generated by the function below are indicative only.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.

def download(url = 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
             target_filename = 'Latest',
             filename_extension = 'xml',
             char_set = 'UTF-8'):

    # Import the function for opening online documents
    from urllib.request import urlopen

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError as message: # probably a syntax error
        print("\nCannot find requested document '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print("\nAccess denied to document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except URLError as message: # probably the wrong server address
        print("\nCannot access web server at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None
    except Exception as message: # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              "the document at URL '" + str(url) + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters")
        print("Error message was:", message, "\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None


    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except Exception as message:
        print("\nUnable to write to file '" + \
              target_filename + "'")
        print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents
#
#--------------------------------------------------------------------#




#-----Student's Solution---------------------------------------------#
#
# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain at least seven (7)
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
import webbrowser
import os


news_archive = 'NewsArchive'

# Create a window
window = Tk()
window.geometry('700x500')

# Give the window a title and bg color
window.title('ITD_104')
window['bg'] = 'white'


# Put BBC logo
logo_image = PhotoImage(file = 'TheNewYorkTimes.png')
Label(window, image = logo_image).pack()


# Label
label_title = Label(window,
                    text = 'CURRENT AFFAIRS',
                    font = ('Times New Roman', 37),
                    fg = 'black', 
                    width = 23).pack()

label_barrior = Label(window,
                      text = '-' * 130,
                      fg = 'black',
                      bg = 'white').pack()

label_inst1 = Label(window, text = 'Choose archive to scrape',
                    bg = 'white',
                    font = ('Arial', 17),
                    width = 23).place(x = 50, y = 170)

label_inst2 = Label(window, text = 'Click to check latest news',
                    bg = 'white',
                    font = ('Arial', 17),
                    width = 23).place(x = 400, y = 300)

# function for scraping and displaying summary
def open_selected_files():
    selected_indices = item.curselection()
    print(selected_indices[0])
    file_path = ''
    xml_file_path = ''
    if selected_indices[0] == 0:
        xml_file_path = "C://ITD_104_EunsuKim_Assessment2/NewsArchive/NewYorkTimes_world_14October2023.xml"
        
    elif selected_indices[0] == 1:
        xml_file_path = "C://ITD_104_EunsuKim_Assessment2/NewsArchive/NewYorkTimes_world_15October2023.xml"
        
    elif selected_indices[0] == 2:
        xml_file_path = "C://ITD_104_EunsuKim_Assessment2/NewsArchive/NewYorkTimes_world_16October2023.xml"
        
    elif selected_indices[0] == 3:
        xml_file_path = "C://ITD_104_EunsuKim_Assessment2/NewsArchive/NewYorkTimes_world_17October2023.xml"

    elif selected_indices[0] == 4:
        xml_file_path = "C://ITD_104_EunsuKim_Assessment2/NewsArchive/NewYorkTimes_world_18October2023.xml"

    elif selected_indices[0] == 5:
        xml_file_path = "C://ITD_104_EunsuKim_Assessment2/NewsArchive/NewYorkTimes_world_19October2023.xml"

    elif selected_indices[0] == 6:
        xml_file_path = "C://ITD_104_EunsuKim_Assessment2/NewsArchive/NewYorkTimes_world_20October2023.xml"

    elif selected_indices[0] == 7:
        xml_file_path = "C://ITD_104_EunsuKim_Assessment2/Latest.xml"
        
    try:
        source = open(xml_file_path, 'r', encoding='UTF-8').read()
        print('File opend successfully.')
    
    except:
        print('File doesn\'t exist.')


    # beginning of the sample
    template_start = '''<!DOCTYPE html>

    <html>
        <head>
            
            <style>
                body {background-color:white; margin-left:10%; margin-right:10%}
			
            </style>
        </head>
        <body>            
            <p align = "center" >
            <img src="./TheNewYorkTimes.png"
                alt = "NYT logo">
            </p>
            
            <h1 align = "center">
            World News
            </h1>
            
            <h3 align = "center">
            pubd
            </h3>
            <p>
            <b>News source:</b> <a href="https://www.nytimes.com/section/world"> https://www.nytimes.com/section/world </a> <br>
            <b>Chronicler:</b> Eunsu Kim</p>
	
    '''
    # details
    template = '''
            
	
        
            
            <p style="border:2px solid; height:1.5px">
            <p></p>
            </p>
            
            <h3 align="center">
            <b>Story Heading</b>
            </h3>

            <p align="center">
            <image src="image url",
            height=664
            width=1000
            alt = "1st image">
            </p>

            <p>
            synopsis(summary)
            </p>

            <p><strong>Full story: </strong><a href="feed link"> full story link </a><br>
            <strong>Dateline: </strong> published date
            </p>
    '''

    # end
    template_end ='''
             <p style="border:2px solid; height:1.5px">
            <p></p>
        </body>
 
    </html>'''

    # title
    title = '''<item>
          <title>([A-Za-z -:]+)</title>'''



    itemRegex = '''<item>([\s\S ]*?)<\/item>'''

    items = findall(itemRegex, source)

    print(items[0])

    target_file = 'News_summary.html'
    sample_file = open(target_file, 'w', encoding = 'UTF8')

    allRegex = '([\s\S ]*?)'

    # write template_start html and edit in News_summary.html
    DateRegex = '''<lastBuildDate>([\s\S ]*?)[0-9]{2}:[0-9]{2}:[0-9]{2}'''
    Date = findall(DateRegex, source)
    sample_file.write(template_start.replace('pubd', Date[0]))

    
    # write template html and edit in News_summary.html
    
    
    for itemm in items[:5]:
        titleRegex = '<title>([\s\S ]*?)</title>'
        title = findall(titleRegex, itemm)
        descriptionRegex = '<description>([\s\S ]*?)</description>'
        description = findall(descriptionRegex, itemm)
        imageRegex = 'url="([\s\S ]*?)"'
        image = findall(imageRegex, itemm)
        fullstoryRegex = 'href="([\s\S ]*?)"'
        fullstory = findall(fullstoryRegex, itemm)
        pubdateRegex = '<pubDate>([\s\S ]*?)</pubDate>'
        pubdate = findall(pubdateRegex, itemm)
        print(title)
        print(description)
        
        sample_file.write(template.replace('Story Heading', title[0]).replace("synopsis(summary)", description[0])
                          .replace("image url", image[0]).replace("feed link", fullstory[0])
                          .replace("full story link", fullstory[0]).replace("published date", pubdate[0]))
    
    sample_file.write(template_end)

    print('\n', target_file)

    sample_file.close()
    
 
    # after creating the html, update the file_path to that new html file
    file_path = "News_summary.html"

    # open the newly created html created path
    webbrowser.open(file_path)
   

# Function for 'Load latest News' button 
def latest():
    download()
    item.delete(7, END)

    file_path = "Latest.xml"

    with open(file_path, 'r', encoding='UTF8') as file:
        lines = file.readlines()
        for line in lines:
            item.insert(END, ' Latest')

    
# Listbox
item = Listbox(window, height = 8, width = 30,
                 font = ('Arial', 15),
                 bg = '#f1f3f5')
##file_path = ["D:/ITD104/Assessment2/NewsArchive"]
##for name in file_path:
##    item.insert('end', name)
##for file_path in html_file_paths:
##    item.insert(END, file_path)

                 
item.insert(0, ' Sat, 14 October 2023')
item.insert(1, ' Sun, 15 October 2023')
item.insert(2, ' Mon, 16 October 2023')
item.insert(3, ' Tue, 17 October 2023')
item.insert(4, ' Wed, 18 October 2023')
item.insert(5, ' Thu, 19 October 2023')
item.insert(6, ' Fri, 20 October 2023')
##item.insert(7, ' Latest News')

item.place(x = 50, y = 210)

# Button
Scrape_button = Button(window,
                    text = 'Scrape and Display summary',
                    font = ('Arial', 13),
                    height = 2,
                    command=open_selected_files)
Scrape_button.place(x = 100, y = 410)

Latest_button = Button(window,
                        text = 'Load latest News',
                        font = ('Arial', 13),
                        height = 2,
                        command = latest)

Latest_button.place(x = 480, y = 350)                        


window.mainloop()











################ PUT YOUR SOLUTION HERE #################
pass


#--------------------------------------------------------------------#

