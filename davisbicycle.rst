==========================
Davis Instrumented Bicycle
==========================

Steer Torque
============

Literature Review
*****************
There are very few published studies that measure or attempt to measure steer torque on a bicycle or lightweight single track vehicle. There are a more analytical studies that attempt to predict steer torques. The following lists some that I have read.

Steer torque from models
------------------------
`Limebeer2006 <resolveuid/e3329e0d28ba360667c5fd57947c8441#Limebeer2006>`_

Limebeer and Sharp show a graph of steer torque for the benchmark bicycle model on page 47 for step inputs of steer torque that range from -0.5 to 2.5 Nm for extreme roll and steer angles.

`Sharp2007 <resolveuid/e3329e0d28ba360667c5fd57947c8441#Sharp2007>`_

Robin Sharp uses a multi-degree of freedom motorcycle model and an LQR controller with preview to control a motorcycle moving at 30 m/s through a 4 meter lane change and a 250 meter S-turn. For the lane change he gets torques ranging from about -20 Nm to 55 Nm for a more aggressive control and -4 to 6 Nm for less aggressive control. The S-turn gives torques from -40 Nm to 70 Nm with a sharp peak in torque in the middle of the S-turn.

`Sharp2007a <resolveuid/e3329e0d28ba360667c5fd57947c8441#Sharp2007a>`_

Robin Sharp uses the benchmark bicycle model and an LQR controller with preview to follow a randomly generated path that has about 2 meter lateral deviations. The bicycle is traveling at 10 m/s and the steer torque ranges from about -15 to 15 Nm. Medium control reduces the torques to under +/- 10 Nm. Straight line to circle path maneuvers show torques ranging from -0.5 to 0.5 Nm for loose controls and -2.5 to 2.5 for medium controls.

`Sharp2008a <resolveuid/e3329e0d28ba360667c5fd57947c8441#Sharp2008a>`_

Robin Sharp used the benchmark bicycle model and an LQR controller with preview to make a bicycle track a 4 meter lane change at 6 m/s. During this manuever, the steer toque ranged from about -1 to 1 Nm. He also showed a very fine steer torque variation in the range of 0 to 0.0025 Nm about 10 meters before the start of the lane change.

`Peterson2009 <resolveuid/e3329e0d28ba360667c5fd57947c8441#Peterson2009>`_

Peterson and Hubbard show the steady turning required steering torques for the benchmark bicycle on page 7. The torques for lean angles from 0 to 10 degrees and steer from 0 to 45 degrees are under 3 Nm.

Experimental Steer Torque
-------------------------
`Cain2010 <resolveuid/e3329e0d28ba360667c5fd57947c8441#Cain2010>`_

Stephen Cain built an instrumented bicycle with a steer torque measuring device and studied steady turns.

`Weir1979a <resolveuid/e3329e0d28ba360667c5fd57947c8441#Weir1979a>`_

Weir et al. designed an instrumented motorcycle with a torque sensor. The range was +/- 70 Nm with 1% accuracy and\>10 Hz dynamic range. The crosstalk due to the other moments on the steer were removed with by utilizing two thrust bearings. It included stops to prevent sensor overload protection and weighed 14 Newtons. They comment that the handlebars are significantly rigid for their purposes. It was a modular design set up for multiple motorcycles. They comment on the range being too large for small amplitude inputs used in steady turning and straight running and that more sensitivity would be needed to measure these accurately. Weir used this to measure steer torques for two motorcycles at various speeds (\>10 m/s) for steady turning and lane change maneuvers. The steady turning produced torques in the range of -10 to 30 Nm and the lane change produced -20 to 55 Nm.


.. image:: resolveuid/70ffec06b2a0a0b062825cea5f48b766/image_preview
   :alt: weirSteerTorque.png
Lorenzo1997

David de Lorenzo instrumeted a bike to measure pedal forces, handlebar forces, hub forces to measure the in-plane structural loads. He took the bike to the trails and had 7 riders do a downhill section. The hand reactions were measured with a handlerbar sensitive to x (pointing forward and parallel to the ground) and z (pointing upwards, perpendicular to the ground) axis forces on both the left and right sides of the handlebar. Net torque about any vector in the fork plane of symmetry can be calculated from these. Figure 3d shows a plot of steering torque with maximums around 7 Nm. The stem extension torque (representing the torque from pushin down and up on the handlebars) reaches 15 Nm. The calibration information leads me to believe that the crosstalk from the all of the forces and moments on the handlebars gives a very low accuracy for the reported torques, probably in the +/- 1 to 3 Nm range.

`Biral2003 <resolveuid/e3329e0d28ba360667c5fd57947c8441#Biral2003>`_

Biral et al. designed a custom steer torque measurement system using a cantilever beam. They don't specifically discuss the cross talk, but do mention that they use a half-bridge strain gauge. This design seems that it could be susceptible to cross talk from the forces applied to the handlebars by the rider. But they also report experimental values for torque that match model predictions very well. The measure torques from -20 to 20 Nm for a slalom maneuver at 13 m/s.


.. image:: resolveuid/f9b5e6dae31958f0c23a8138ba463478/image_preview
   :alt: Biral's Steer Torque Design
\

`Astrom2005 <resolveuid/e3329e0d28ba360667c5fd57947c8441#Astrom2005>`_

Åström et al. shows a steer torque measurement system constructed for the UCSB instrumented bicycle but with little extra information. They use a linear force transducer of some sort mounted on the handlebars.


.. image:: resolveuid/84725eb403fffe4a7a8bb44731822875/image_preview
   :alt: UCSB Steer Torque Measurement


 `Cheng2003 <resolveuid/e3329e0d28ba360667c5fd57947c8441#Cheng2003>`_ 



This is a report about a design project at UCSB to develop and implement a steer torque measurement device (same one shown the Åström paper). He gives a pretty bad anedoctal introduction to bicycle dynamics, but the experiments and measurements seem to be one of a kind. They did some basic experiments by attaching a torque wrench to a bicycle and made left at right turns at speeds from 0 to 13 m/s (0 to 30mph). The torques were under 5Nm except for the 13 m/s trial which read about 20 Nm. They designed a pretty nice compac torque measurement setup by mounting the handlebars on bearings and using a linear force transducer to connect the handlbars to the steer tube which reduced the effects of other moments and forces acting on the steer tube. The use of bearings and rodends may be questionable as there is bearing friction and slop. Furthermore, downward forces on the handlebars could possibly still be transmitted to the load cell. The design does allow one to choose the lever arm for the load cell, thus giving some choice to amplify the force signal. They set it up to measure from 0 to 84 Nm with a Model SM Series S-type load cell from Interface with a 670 Newton range. They used a transducer amplifier also for signal conditioning. There are several sections on calibration, with some description of the use of pulleys and cables to apply a torque to the handlebars. They measured the torque during two different manuever types: a sharp turn at various angles and steady turns on various diameter circles both at 10mph (4.5 meters/second). The rider maintained constant speed through visual feedback of a speedometer. He talks of very noisy measurements and filters the noise by some type of moving average. He does not identify an countersteering. He claims the rider turns the handle bars right to initiate a right turn. There seems to be no counter-torque in the data for turns. For the sharp turns the highest reported torque is about 10 Nm, for the steady turning he reports the highest average torque as 1 Nm.



Download the final report and associated data files here: `Cheng2003.pdf <resolveuid/ac368855518787b7cc5f430a91127168#Cheng2003>`_ and `data.zip <resolveuid/9214550a56ec25f3e94067965b6ee054#Cheng2003>`_ Related topics from STV Discussion List
---------------------------------------
\

*  `Welcome and a steer torque question <http://groups.google.com/group/stvdy/browse_thread/thread/863bd2761a8ee3de>`_ 
*  `Steering torque measurement <http://groups.google.com/group/stvdy/browse_thread/thread/e82893d10cbb1d46>`_ 
*  `More questions on bicycle steer torque measurements <http://groups.google.com/group/stvdy/browse_thread/thread/4ae6ebb1d05ba299/>`_ 

Initial Design Ideas
********************
We are planning on measuring the steer torque the rider applies to control a bicycle. This will be used for human control model identification and for use in the necessary feedback loops required control the riderless bicycle. Measuring the steer torque is not trivial. This is because various models predict torques ranging in the 0-2 Nm (0-1.5 ft lbs) range with signal variations and reversals requiring +/- 0.01 Nm (0.01 ft lbs) in measurement accuracy. The range and accuracy are easily measured with modern torque sensors, but the fact that large moments can be applied to the fork and handlebars by the ground and/or rider introduces the problem of crosstalk. The forces and moments applied to the fork will corrupt the relatively small torque measurements as they can be hundreds of times larger in magnitude. With this in mind, we are trying to come up with a way to isolate the torque measurement to eliminate or minimize the crosstalk and get good, noiseless, accurate readings. The following are some basic designs we are working with:

1. Åström Design
----------------
This is a sketch of what was designed for the UCSB instrumented bicycle and presented in a `2005 paper by Karl Åström et al <../references#Astrom2005>`_ . It uses an off-the-shelf axial load cell mounted between a floating handlebar and a bar extending from the steer tube. This seems to be a good design, but it would be nice to eliminate the handlebar bearings and the rod ends.\\

`
.. image:: resolveuid/c0d97223989ee68a3374677e0e91c112/image_preview
   :alt: Astrom Design
 <../instrumented-and-actuated-bicycle/photos/P1040070.JPG>`_

My professor, `Drew Landman <http://eng.odu.edu/aerospace/aefaculty/dlandman.shtml>`_ , from Virginia who I worked with designed force balances for wind tunnel testing at the `LFST <http://www.nasa.gov/vision/earth/improvingflight/fst_overview.html>`_ suggested a `redesign that eliminates the bearings and replaces them with flexures <resolveuid/dd2f3c8a73e2229352bbc0320e6d4df5>`_ .

2. Weir Design
--------------
David Weir designed a motorcycle steer torque measurement system in his `1979 technical repor <../references#Weir1979a>`_ t that also floats the handlebars on bearings but uses an off-the-shelf torque sensor instead. The sketch shows the basic concept. The handlebars are floating on bearings and the torque sensor connects the handlebars to the steer tube. He claimed that the design lacked low range resolution. Motorcycles can experience torques that are as high as 50 Nm according to some models.

`
.. image:: resolveuid/aeecb1a6ff643de9ba50f3bd041bf2de/image_preview
   :alt: Weir Design
 <../instrumented-and-actuated-bicycle/photos/P1040072.JPG>`_

3. Internal Stem Design
-----------------------
This is a design that we came up with when preparing our abstract on the topic. It is fundamentally the same as the Åström design but includes flexure elements instead of rod ends and is a bit smaller in scale.

`
.. image:: resolveuid/66607943aed83c431d32574f6c71a3bd/image_preview
   :alt: Internal Stem Design
 <../instrumented-and-actuated-bicycle/photos/P1040069.JPG>`_ 
.. image:: resolveuid/3c72eeac7942df92ace40db550c5102b/image_preview
   :alt: steerTorque.png

4. Double Steer Design
----------------------
\This design separates the handlebar and stem's rotation axis from the steer tube and fork's rotation axis much the way many long wheel base recumbents or bakfiets are designed. The load cell is then place on the connecting rod. This design is is prone to slop in the steer mechanism.

`
.. image:: resolveuid/a116bf55e754b4722dc10dad3d25d266/image_preview
   :alt: Double Steer Design
 <../instrumented-and-actuated-bicycle/photos/P1040073.JPG>`_

5. Bearing-less design
----------------------
\Luke came up with this design and was able to eliminate the need for bearings. Two arms are clamped to the steer tube and a load cell is placed between the arms. The difference in this is that not all of the torque is transferred through the load cell, but maybe enough is that we can measure it.

`
.. image:: resolveuid/2fb828ed476c7be1652cb1733c0c1acf/image_preview
   :alt: Bearing-less Design
 <../instrumented-and-actuated-bicycle/photos/P1040074.JPG>`_

Forces on the steer tube
************************
\Ideally, we'd like to slap a strain gauge on the steer tube to measure the shear strain and get a good torque reading but this isn't so easily done. The bicycle steer tube has various other forces acting on it. For the most basic case a the ground contact force at the front wheel puts the fork into bending and compression. Likewise the person can apply forces to the handlbars which also put the steer tube into bending and compression. It turns out that the moments in the steer tube can be as high as 200 times the steer torques we are trying to measure.

 `
.. image:: resolveuid/c1b056efbeda1b2a4d12746e58d23021/image_preview
   :alt: Basic Bicycle Forces
 <resolveuid/8cd3b8787503b6d430324632879251e3>`_ \

There are ways to apply strain gauges to a bar in torsion that would theorectically cancel all of the axial and bending strain components. Both bending moments and axial forces only create strain in the axial direction and shear and torsion create strain in the direction normal to axial. The following comes from Beckwith and Margoni's Mechanical Measurements and shows two possible strain gage bridge configurations that can reduce or eliminate strains not due to torsion.\


.. image:: resolveuid/bf57e0090435ce8abd001875e8048c59/image_preview
   :alt: Strain Bridge Configuration for Torsion
L seems to be a good choice for the steer torque measurement, but in reality it is impossible to align strain gages perfectly. This can introduce cross-sensitivity or cross talk. If the cross talk strains due to the bending moments are only 1% of the of the total strain due to the moments, that can still corrupt the steer torque measurement. With this in mind we decided to look into what the forces in the steer tube actually look like.

\We modeled the fork as a basic beam supported by the headset bearings (points C and D) and the forces/moments due to the ground reaction force and force applied to the handlebars were calculated.


.. image:: resolveuid/90e67bba258d9fc9a10c52b7f9e57252/image_preview
   :alt: Fork Modeled as a Beam
\

The following graphs show what the shear and bending moment diagrams for various loadings look like both from the side and the front of the bike.

\
.. image:: resolveuid/151b3c8243fd5d2c731a8eae91188c5a/image_preview
   :alt: mvdiagram01.png
\
.. image:: resolveuid/3793383a568fdd2ce08de994c53ed178/image_preview
   :alt: mvdiagram02.png
\
.. image:: resolveuid/a140ee7e5f4d70c0b44eadb5e6e0b4be/image_preview
   :alt: mvdiagram03.png
\
.. image:: resolveuid/c599592a90c32dba06aef0c91ce42dcb/image_preview
   :alt: mvdiagram04.png
\
.. image:: resolveuid/0ca7e86d028868a832aeef90eba9bddf/image_preview
   :alt: mvdiagram05.png

.. image:: resolveuid/2af4768d559082a648ccc51c3bb08ebf/image_preview
   :alt: mvdiagram06.png
\These graphs show that the bending moments and shear stresses can be of much larger magnitude than the steer torques, so cross talk is a major concern. These graphs also show that it if no loads are placed on the handlebars the entire portion of the steer tube/stem above the headset has no bending moments and no shear stress. This is the ideal place for a torque sensor, if we can eliminate the transfer of forces applied to the handlebars to the steer tube.

\This leads us to a design idea that isolates the steer torque sensor from the handlebar and fork forces. The basic design idea is sketched below. It includes a separate "headset" for the handlebars that take up any handlebar forces. The handlebar is connected to the steer torque sensor via a zero backlash universal joint so no moments can be transferred to the sensor. The steer motor will need to be mounted above the u-joint so torques from the rider or the motor can be measured. We are looking at a `Futek <http://www.futek.com/>`_ Reaction Torque sensor that has a max torque of either `6 Nm <http://www.futek.com/product.aspx?stock=FSH02594>`_ or `12 Nm <http://www.futek.com/product.aspx?stock=FSH02595>`_ but are unsure what the best range and accuracy for these measurements are since there seems to be no public data from bicycle steer torque measurements.


.. image:: resolveuid/c599ed60206a4dc53ca4bfb385e29e58/image_preview
   :alt: Torque Measurement Design
Torque Wrench Experiments
*************************
Following Cheng's lead, we decided to do some experiments with a accurate torque wrench to see get an idea of maximum torques. We made a little attachment to the steer tube that allowed easy connection of various torque wrenches. A helmet camera was mounted such that it could view the torque wrench, handlebars and speedometer relative to the bicycle frame. The torque wrench had a range from 0 to 8.5 Nm and a +/- 2% accuracy of full scale (+/- 0.17 Nm). The speed was maintained by an electric hub motor (i.e. no pedaling).


.. image:: resolveuid/a5dd3f34a3fdab005d47044cc79ec415/image_mini
   :alt: Torque wrench mount

.. image:: resolveuid/cf4e4b895604aa8a0708cd0da2f9dfa8/image_mini
   :alt: Torque wrench face
\
.. image:: resolveuid/ceef82f5a04518123a04fa71d77092af/image_mini
   :alt: Torque camera


The `data file <resolveuid/881a2e6a7f894ca6c3c9318cc5ebc921>`_ includes the run number that corresponds to the video number, the rider's estimate of the speed after the run in miles per hour, the maximum reading from the torque needle after the run in inch-lbs, the rider's name, the maneuver, the minimum speed seen on the video footage in miles per hour, the maximum speed seen on the video footage in miles per hour, the maximum torque seen on the video footage in inch-lbs, the minimum torque seen on the video footage in newton-meters, and the rotation sense for each run (+ for clockwise [right turn] and - for counter clockwise [left turn]) . There were seven different maneuvers: straight into tracking a half circle (radius = 6 meters and 10 meters), tracking a straight line, straight to a 2 meter lane change, slalom with 3 meter spacing, steady circle tracking (radius = 5 and 10 meters). All of the videos and data can be downloaded `here <http://www.archive.org/details/BicycleSteerTorqueExperiment01>`_ . The results ( `R code <resolveuid/0d0ff8f04173b50c5ff52b572f7232e6>`_ ), are shown in the following graphs:


.. image:: resolveuid/a41a4da65605e8d6c98e1cf41c3b19f6/image_preview
   :alt: torqueHist.png
\\
.. image:: resolveuid/0ad457a926630a28fffe4933f564108d/image_preview
   :alt: torqueSpeed.png
\
.. image:: resolveuid/eeb33b106268eb3610800cb1fcb128bd/image_preview
   :alt: Circle5.png
\
.. image:: resolveuid/1cb55905c0c7d6e0a3ca5418ab6332b1/image_preview
   :alt: Circle10.png

.. image:: resolveuid/ffa24c1a665ac8069176eb74b8980489/image_preview
   :alt: HalfCircle6.png
\\
.. image:: resolveuid/7dc9751d669c72fbfd0325e3786d71c5/image_preview
   :alt: HalfCircle10.png
\
.. image:: resolveuid/687dfb8a8784bd097f270c9dde6d5b30/image_preview
   :alt: LaneChange.png
\
.. image:: resolveuid/c15cd7b01dd093ba1c202abdaead757e/image_preview
   :alt: LineTrack.png
\
.. image:: resolveuid/02c0ffe9fe730b129c557f4852824b3c/image_preview
   :alt: Slalom.png
The primary goal was to determine the maximum torques we will see for the types of maneuvers we are interested in. The histograms shows that we never recorded any torques higher than 5 Nm. The following shows the max and min torque values for different maneuvers:

\ManeuverMax Torque

Min Torque

Steady Circle (r = 10m)

3.4

-2.4

Steady Circle (r = 5m)

2.4

-2.2

Half Circle (r = 10m)

3.8

-3.2

Half Circle (r = 6m)

3.4

-5.0

Lane Change (2m)

2.9

-2.6

Line Tracking

2.6

-3.4

Slalom

4.5

-4.8

There seems to be little to no speed dependency on the max and min torque values.

Final Steer Assembly Design
***************************
\


.. image:: resolveuid/2b03ff99ae75489ee433058e64814f7f/image_large
   :alt: Final Steer Torque Measurement Design
Steer Dynamics
**************
This design is setup to eliminate anything but the torque from being measured, but their is a little more need to get to the actual rider applied steer torque. The torque we measure is the torque in the steer column, \(T_S\). Their is a relationship from \(T_S\) to \(T_\delta\) that requires one to know the friction in the lower and upper bearings (this is potentially both viscous and coulomb) and the inertia of the handlebar/fork assembly and the inertia of the portion above and below the torque sensor.

The first thing we did was to try to characterize the friction in the bearings. We did this by mounting the bicycle frame such that the steer axis was vertical, the wheel was off the ground, and the bicycle frame was made very rigid. Secondly, we attached two springs to the handlebars such that the force from the springs acted on a lever arm relative to the steer axis. This allowed us to perturb the handlebars and let the vibrations damp out. We recorded data from the steer potentiometer, steer rate gyro and the torque sensor during these perturbations. For now, we simply used the steer angle signals to estimate both the viscous and coulomb friction from the two bearing sets.\

Once the steer friction and the inertial characteristics are known the steer torque applied by the rider can be formulated based on a free body diagram of the upper part of the handlebar/fork assembly. The time derivative of the angular momentum of the handlebar about its center of mass is equal to the sum of the torques acting on it. During a run, the torques acting on the body made up of the handlebars and the torque sensor are the friction in the upper bearing, \(T_F\), the measured steer column torque, \(T_S\), and the rider applied steer torque, \(T_\delta\).

$$\sum{\bar{T}} = \left[\begin{array}{c}0\\0\\T_\delta - T_S - T_F\end{array}\right]$$

The derivative of the angular momentum of the handlebar is:

$$\dot{\bar{H}} = I\bar{\alpha} + \bar{\omega} \times \bar{H}$$

Being that the torques only appear in the 3 component, we can formulate the equation of motion as such:

$$T_\delta = T_S + T_F + I_{22}\omega_1\omega_2 + I_{31}\alpha_1 + I_{33}\alpha_3 - \omega_2(I_{11}\omega_1+I_{31}\omega_3)$$

\(T_\delta\)Steer torque applied by the rider.\\(T_S\)\Measured torque in the steer column, between the two bearing sets.\\(T_F\)\The friction in the upper bearing. \(T_F = c\dot{\delta} + asgn(\dot{\delta})\)\\(\bar{\omega}\)\The body fixed rate of of the handlebar. The 3 component is aligned with the steer axis (positive is down), the 1 component is perpendicular to the steer axis and point forward, and the 2 component follows from the right hand rule (perpendicular to the steer axis, pointing to the right).\(\bar{\alpha}\)\The body fixed angular accelerations of the handlebar.\\(I\)\The inertia tensor of the handlebar about its center of mass and aligned with the same coordinate system as the angular velocity.\


