# Underactuated-Robot-finger
Underactuated Robot finger with 2 four-bar linkage mechanism

**INTRODUCTION**

Global Positioning System (GPS) which is a Global Navigation Satellite System (GNSS), uses satellites to measure distances for a specific position based on the trilateration method. The signals from the GPS satellite are run by atomic clocks and it contains Pseudo Random Number Sequence (PRN) and Navigation Information that includes satellite position and clock correction data. Each satellite uses a unique Pseudo Random Number (PRN) which is also known as the Course Acquisition (C/A) PRN Code. The GPGGA log contains position, time, and parameters related to the GNSS receiver. 
Under ideal conditions, the standard GNSS error for a GPS receiver is about 2 meters. With the help of Differential GNSS or Real-Time Kinematic GNSS (RTK GNSS), We can improve the accuracy to a 1 cm radius. It measures the positions and pseudoranges based on the carrier phase measurements. The repeated position determination over time supported the base station to increase the accuracy of its position measurement. GNSS signal can be received from various satellite systems by RTK GPS receivers which have multiband antennas. 
RTK corrections are the data that the "Base Station" sends to the "Rover" to enable the "Rover" to determine its location at the centimeter level. RTCM is the name of the language/protocol that is used to transmit this data. Both receivers must observe almost identical satellites to determine this RTK location. Because of this, the RTCM adjustments are only effective up to 35 kilometers from the Base Station. Corrections for RTCM/RTK are typically sent once per second. It can be transmitted by an IP network, a wireless link, or a wired serial communication.
In a nutshell, this project report's particular contributions include,
 1. Analysis of GNSS and Real-Time Kinematic GNSS.
 2. Comparing GNSS data with RTK GNSS data.
 3. Analyse moving and stationary data with the help of RTK GPS.
The remaining portion of the work is structured as follows. Section Ⅱ discusses the methodology of this report. Section Ⅲ represents our discussion of the obtained results in detail. Section Ⅳ presents the conclusion of this report.

**MATERIALS AND METHODS**

a. Computer specification

The specifications of the computer utilized are as follows.

   1. Operating System – Ubuntu 20.04 LTS
   2. RAM – 16.0 GB
   3. Processor – 11th Gen Intel(R) Core (TM) i5-11400H @ 2.70GHz
   4. System Type – 64-bit operating system, x64-based processor

b. Tools required

A Robot Operating System (ROS) is utilized to collect data from the GPS receiver. This is an open-source software development tool for the applications of robotics. Specifically, ROS Noetic Ninjemys which was released on May 23rd, 2020, is used to perform the tasks to obtain the GNSS values. This is mainly focused on the Ubuntu 20.04 releases to perform well. 
In addition to ROS Noetic Ninjemys, the following tools are used for this experiment.

	1. Python – version 3.12.2 
	2. Visual Studio Code – version 1.86 
	3. Minicom
	4. Turbo87’s Package
	5. GPS Puck
	6. Emlid flow

**Methodology**

 Initially, the workspace had been set up with the installation of ROS Noetic Ninjemys, minicom, Python, Visual Studio Code, and Turbo87’s Package. After the installations, we set up the ROS environment variables and built a catkin workspace. Then, we created a new package in the catkin workspace using the “catkin create pkg” command. 
Subsequently, we wrote a Python script to read in and parse a GNGGA string which is required for converting the string to latitude, longitude, UTC, fix quality, and HDOP parameters. Then, we converted latitude and longitude into UTM values with the help of the UTM package. Parallelly, we made a custom GPS message named “Customgps.msg” in the appropriate directory with the following fields:

	header (type: Header)
	latitude (type: float64)
	longitude (type: float64)
	altitude (type: float64)
	utm_easting (type: float64)
	utm_northing (type: float64)
	zone (type: uint8)
	letter (type: string)
	fix_quality (type: uint8)
	hdop (type: float64)
	gpgga_read (type: string)
 
Afterward, we published the custom GPS message and saved the collected data to a ROSbag. The collected ROSbag data should be converted to other file types so, we converted the data in a CSV file using a Python script to read in the bag. Later, the system had been set up to read the data from the serial port using Minicom and we wrote a launch file and made the driver accept any port. Finally, the obtained CSV file is processed to get the graph under the following conditions:

	a. Collect stationary data in an open area.
	b. Collect stationary data in an occluded area.
	c. Collect linear moving data for approximately 200 meters.
 
**RESULTS AND DISCUSSION**

The experimental results were plotted in graphical representation. Let us explore the results in detail below.

A. Graphical representation with calculations

The Obtained error values are:

	1. Average error from centroid for open data: 0.06118047828460524 m 
	2. Average error from centroid for occluded data: 0.8012467376398961 m
 
To quantify the error from the centroid to the measured positions for both the open and occluded stationary RTK datasets, a comparable methodology is applied. Initially, the centroid of each dataset is determined through the calculation of mean values for the easting and northing coordinates. Subsequently, the Euclidean distance from each data point to its respective centroid is computed. The final step involves averaging these distances, yielding a singular error value for each dataset. This process provides a succinct and effective means of assessing the accuracy of measured positions concerning the centroid in both open and occluded stationary RTK datasets.
![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/b49ca3b4-e488-446b-87a8-cfe9cb27c24a)
Fig 1: RTK – Differences in Easting vs. Northing (Stationary and Occluded)
![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/4ff09e02-6092-41a3-82b0-4859b8047d64)
Fig 2: RTK - Histogram of Euclidean Distances to Centroid.

![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/48c7b565-0ff4-4402-812e-3f400014128d)
Fig 3: RTK - Stationary Altitude VS Time

![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/ab6d7051-5140-470c-b40c-cc3c8878776e)
Fig 4: RTK Northing vs. Easting with Best Fit line

The obtained error value from the above Fig. 4 is as follows:
Root Mean Squared Error (RMSE) from Line of Best Fit to Walking Data: 0.12850647818168368 m.

![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/e1f94363-fdbe-4452-8102-0cbb6bff7735)
Fig 5: RTK - Moving Altitude VS Time

To compute the quantitative (numerical) error from the centroid to the measured positions for both the open and occluded stationary datasets, adhere to the following procedure:

1. Compute the centroid of each dataset.
	a. Calculate the mean value of the easting and northing coordinates for each dataset to determine the centroid.
	b. Centroid Formula:

	  1. Centroid (Cx, Cy) = (1/n) * Σ(xi, yi) for i = 1 to n, where n is the number of points in the dataset.
	  2. Cx = (1/n) * Σ(xi) and Cy = (1/n) * Σ(yi)
3. Determine the Euclidean distance from each point to the centroid.
	  a. For each point (xi, yi), compute the distance to the centroid (Cx, Cy) using the Euclidean distance formula.
	  b. Euclidean Distance Formula: Distance = √((xi - Cx)^2 + (yi - Cy)^2)
4. Calculate the average distances to obtain a singular error value for each dataset.
	  a. After determining the distance from each point to the centroid, average these distances to derive a singular error value for each dataset.
	  b. Average Error Formula: Average Error = (1/n) * Σ(Distance) for i = 1 to n, where n is the number of points in the dataset.

![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/7cde764a-422c-4b7e-8489-8057d6824d65) 
Fig 6: GPS Puck - Stationary northing vs. easting graph

The Obtained error values are:

	1. Average error from centroid for open data: 8.497042283267776 m.
	2. Average error from centroid for occluded data: 17.23220719015375 m.
 
The process involves fitting a line to the walking data, predicting the dependent variable based on this line, calculating the error between predicted and actual values, and obtaining the average error using the Euclidean distance. These steps provide a comprehensive assessment of the accuracy of the line of best fit for the walking dataset with the help of the NumPy tool.

![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/fd9f714d-bf7a-459d-8daa-72ece6d2708d)
Fig 7: GPS Puck - Northing vs. Easting graph with Best Fit line

The obtained error value from the above Fig. 4 is as follows:
Root Mean Squared Error (RMSE) from Line of Best Fit to Walking Data: 1.3673692478628254 m.

**CONCLUSION**

In conclusion, this report extensively delved into the analysis of Global Navigation Satellite System (GNSS) data, particularly focusing on the comparison between Global Positioning System (GPS) and Real-Time Kinematic GNSS (RTK GNSS). The investigation included the examination of stationary and moving datasets, exploring the impact of different environmental conditions on the accuracy of position fixes. Key findings revealed significant disparities between standalone GPS and RTK GNSS, with RTK exhibiting superior accuracy in both open and occluded areas. The study further highlighted the dynamic nature of GPS navigation with the receiver, emphasizing the challenges introduced during movement, such as multipath interference and signal blockage, leading to increased error values in the walking datasets.
In summary, the experiment successfully showcased the efficacy of RTK GNSS in enhancing positional accuracy, especially in challenging environments. The observed errors in stationary and moving datasets underscore the importance of considering environmental factors in GNSS applications. These findings contribute valuable insights into optimizing GPS navigation systems, providing a foundation for future enhancements and advancements in the realm of satellite-based positioning technologies.
