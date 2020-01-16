In my test two file that contain list of countries in Json and xml format are compared. 
These files were taken from https://github.com/obikag/iso-3166-country-codes
In term of executing time json is faster than the xml.
json reading time is 0.093 second while xml took 0.141 second (see the screenshot).
Based on my reasoning, I think Json is faster because it has more simple structure than xml.
As a result, the system has less things to do when executing program to read json file.
Compared to json, xml structure are more complicated. 
What I mean by complicated here is that xml has more string of character that contain the same information as it json counterpart.
In conclusion, use json to structuring information for faster executing time rather than xml.
