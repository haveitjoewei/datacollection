# datacollection

# Purpose
To compile and organize various course information from the XDF website, which is written using HTML and CGI scripts.

# How
Using python and its HTML Parser, we are able to extract the information from the XDF website. I’ve written four scripts with the different functions of :

	•	Fetching the names of the cities in China (souCity.py)
	•	Fetching the different course categories in each city (souCategory.py)
	•	Follow the fetched categories to compile a list of course names (souCourse.py)
	•	Using the course names to find the exact locations of each class. (souClass.py)

I created an excel sheet to save this information. 

This excel sheet includes:
	* City Name
	* Class Code
	* Course Name
	* Scheduling of the course
	* Age Category
	* Class Size
	* Price
	* Class Location


# Excel Content

* Course Count: How many courses have been grabbed from the website
* City Name: Where the course is located
* City Code: Identification number for a city
* Category: Which category the course is listed under. This includes (Elementary School, Middle School, High School, College, Adult, International, Language, Summer School, etc)
* Course Code: Unique identification number for each course
* Course Name: Name of the course
* Grade ID: Unique identification number for the category and grade level of the course. 
* Subject: Course subject
* Subject level: Specifies the subject level (Basic, advanced, etc)
* Boarding/Day: “1” refers to day school, “2” refers to boarding school 
* Class Capacity: Number of people that can be enrolled in the course
* +/- : “1” means class capacity is flexible and can be greater than what is indicated. “0” means that there is a solid cap.
* Start Date: When the course starts.
* End Date: When the course ends.
* Season: Refers to one of the four school seasons or special holidays during the which the course is held
* Status: Indicates whether the course is still open to registration, is full, started, or ended.
* Duration: How long the class lasts.
* Number of Sessions: How many sessions the course has.
* Location: Location
* Price: Price of the course.
