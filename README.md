# Underactuated Robot finger with 2 four-bar linkage mechanism 

**INTRODUCTION**
	In industries, Robots play a major role in manufacturing units, especially using the Robotics Arm. In the Robotic arm, the Robotic hand (end effector) is being researched to perform various tasks in manufacturing sectors beyond the application of pick and place operations. 
	In the project, we are going to explore the finger mechanism in a robotic hand as an end effector to replicate the human finger behavior to perform various tasks widely.
	Conventionally, to replicate the finger mechanism for a robot likely to behave as a human finger, every joint needs to be motorized to operate and it seems to be more complicated in design. 
	To simplify the mechanism, many research articles have been gone through and a detailed study in the journal paper “An open-source anthropomorphic robot hand system: HRI hand” by authors Hyeonjun Park and Donghan Kim. Based on this study, a 3D model Robotic finger has been developed and possesses two four-bar linkage mechanisms to replicate the human finger mechanism with only one linear actuator as shown in Fig. 1. 
Unlike fully actuated robotic hands (which have numerous actuators for each finger joint) or simple grippers (with minimal actuators), under-actuated hands strike a balance. They typically have fewer motors (sometimes just one) to open and close the fingers. Springs are cleverly employed to couple joint motions. The developed robotic finger is analyzed and the degree of freedom, Forward kinematics (numerically), range of motion, and singularities and also developed a CAD model of the finger. Let us dive deeper into the analysis of upcoming topics. The 3D Model video uploaded in the following: https://youtu.be/K_wE9uUbY3Q

![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/46c19eb2-764c-4679-a3fd-378aee977ca2)

Fig.1. 3D CAD model of Robot fingers

**DEGREE OF FREEDOM - ANALYSIS**

	The degree of freedom for the robotic finger can be analyzed using planar Grubler’s formula as follows.
	Number of links, N = 6 (links) + 1(ground) = 7
	Joints, 		     J = 8 (Revolute joints)
			  ∑fi = 8×1 = 8
        Substituting the above values into the planar version of Grubler's formula,
			 Dof = 3(N-1-J) + ∑fi = 3(7-1-8)+8 = 2
	Therefore, This mechanism possesses 2 degrees of freedom by planar Grubler's formula, though it is underactuated by 1 link based on the robotic finger linkages as shown in Fig. 2.

![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/38593efb-8c06-4ba6-9207-f813f0b1449d)

Fig. 2. Robot finger links

CAD MODEL:
	The 3D model of the Robotic finger has been developed and analyzed in SolidWorks as shown in Fig. 3 and 4.

  ![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/9816a3bb-55a1-4022-85f1-92c0884eac0a)
  
Fig.3. Isometric view of Robot fingers                                

![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/53b69901-75e0-4580-a7c4-a4813ebce198)

Fig.4. Front view of Robot fingers

**FORWARD KINEMATICS - NUMERICAL METHOD**
	The forward kinematics of the finger are analyzed numerically using motion analysis simulation in SolidWorks.
	The following graphs are analyzed and recorded in detail,
●	Linear Displacement, inch (as shown in Fig. 5)
●	Angular Velocity, deg/sec (as shown in Fig. 6)
●	Angular Acceleration, deg/s2  (as shown in Fig. 7)

 ![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/4d6f6950-29b1-42e2-9996-073907974d64)

Fig.5. Linear Displacement graph

 ![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/819054ef-65d4-4a2c-bd42-bebcb5e6c598)

Fig.6. Angular Velocity graph

 ![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/de525c09-a860-4070-8f61-2f0d5edc9019)

Fig.7. Angular Acceleration graph

**RANGE OF MOTION**
	Using Motion analysis simulation in SolidWorks, the Range of Motion was calculated for the robotics finger as shown in Fig. 8.

 ![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/e9d4e289-0e41-4334-91f8-c67dc1919343)

Fig.8. Range of Motion

 ![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/3828c75f-4de5-49e1-8c8a-44923d3b5f29)

Fig.9. 3D axis graph for the Range of Motion

Also Plotted the 3D axis graph for the Range of motion achieved by the Robotic finger as shown in Fig. 10.

**SINGULARITIES**
	When the Robotic finger is fully stretched out in a vertical direction as shown in Fig. 10, It cannot rotate backward side beyond that stretched. It leads to singularity for the robotic finger and also the fingertip bends to the optimum distance because of the singularity design as well as the length covered by the linear motion of the actuator.
 
![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/b6bda650-f0ad-4666-96f7-e39f384e487a)
![image](https://github.com/annadurai-ka/Underactuated-Robot-finger/assets/156352281/52a149af-7808-4e0f-9677-c60797a8dac6)

Fig.10. Singularities



