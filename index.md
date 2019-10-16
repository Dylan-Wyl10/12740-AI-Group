
# Smart Aquarium
## 12740-F19-Project

### Group Member: 

<div class="test">
    <img src="Pht/YLW.JPG" alt="visualization" width="100" height="75" />
    <img src="Pht/JWW.jpg" alt="visualization" width="100" height="75" />
    <img src="Pht/YC.JPG" alt="visualization" width="100" height="75" />
    <img src="Pht/XCW.JPG" alt="visualization" width="100" height="73" />
</div>
    
#### [Yilin Wang](mailto:yilinw2@andrew.cmu.edu), [Jiangwen Wei](mailto:jiangwew@andrew.cmu.edu), [Yue Cao](mailto:yuec3@andrew.cmu.edu), [Xiangchao Wang](mailto:xiangchw@andrew.cmu.edu)

### [Progress report for the first two weeks](https://dylan-wyl10.github.io/12740/index.html)
### [Progress report for week(Oct.6th - Oct.14th)]()
### [Video]()

---------------------
## 1. Introduction

* People in the city are living far away from natural at present. The city, fulfilled with concrete and steels, isolates the communication between man and nature. In order to ameliorate this situation, we are going to create a domestic micro biosystem that provide a chance for people to get in touch with the nature at home. The smart micro-biosystem called “Smart Aquarium” that can detect and feedback upon the environmental changes with four types of sensors. It contains water and soil environment which is supposed to react individually to the environment changes through a programmed control center(Figure 1-1). 

<p><img src="image012%E7%9A%84%E5%89%AF%E6%9C%AC.jpg" alt="visualization" /></p>

-                              Figure 1-1 Diagrammatic sketch for the Smart Aquarium

* The Smart Aquarium can be divided as two parts: Sensor part and Feedback part. A Raspberry Pi is used as a “brain” to process the data from sensors and multiple the relay to control the feedback circuit with Python code. The system was established by a water level sensor, a photosensitive light sensor, an infrared sensor and a temperature & Humidity sensor. The dump will be controlled by a relay based on the data collect from water level sensor. An LED strip was used as a phenomena light resources when the infrared sensor detected the motion of people coming near the tank. 

### 1.1 Motivation

* Sensors utilize a wide spectrum of transducer and signal transformation approaches with corresponding variations in technical complexity(). It conveys a physical input with an electrical or optical signals in an interst of detecting which stimulate the control system finishing a further reaction. Sensors, playing a role as the bond of computer- environment interaction, are the fundamental parts for the computer to measure the environment. AI Group, consisting of four master students in CEE, aims to explore the impact of sensor technology on the future domestic life. By designing a micro-biosystem which smartly responses to the surroundings and gives a feedback accordingly, the group tries to convey the idea of achieving the co-existence of man and nature with advance technologies. Furthermore, they will gain a great experience in applying sensors into real life. Raspberry Pi, a commonly used microcomputer, is used as a central control system for the demo which is able to monitor the humidity and temperature changes in the micro-ecosystem, detect the human motion around itself and react by lighting LED strip up, or change the water in the system automatically. 

### 1.2 Specific Goals

* Our objective is to multiple sensors implementing the concepts learned in Data Acquisition course with an Raspberry Pi, and design a complete system with a loop of censoring and feedback. The supporting goals are:

    1). Using RPI to collect data from the dht11-Tem & Humidity Sensor. 

    2). Mutipling the relay with Raspberry Pi in Python code, then modify relay into the circuit to finish the entire "Feedbace Loop. 

    3). Conneting the water level sensor and photosensitive light sensor with an ADC analog. Then programming the sensor to detect the water level in the tank and give orders to the dump. An incandescent lamp will open up whent he light sensor detects the ambient light is weakdark to provide supplementary light for photosynthesis. 

    4). Achieving a multi - sensor work system. 

---------------------
## 2. Methodology 

### 2.1 Phenomena of Interest

* The aquarium, which can be placed somewhere in the host's house，will automatically adjust the environment such as the water level in the tank. It can also detect the temperature and humidity which will be showing on the moniter terminal. The tank is divided into two seperate parts, one is a mini eco-system of land area and the other is the ocean area(Figure 1-1). The land area, detected by a light sensor, will be provided light from lamp if the room is dark. We assume the plants in this mirco-system are able to photosynthesize when the host is out of house for a long time. As for the water part, a water-level sensor and a dump are installed to control the water level and keep it fresh. The dump, controled by a relay with the electrical signal from the RPI, is responsible for pumping out unfresh water from the tank. The water-level sensor is used to keep the water level in a stable range. These four sensors operate independently of each other at the same time (Figure 2-1).

<p><img src="xxxxxx" alt="visualization" /></p>

-                              Figure 2-1 Graph for System Working Princple

### 2.1 Sensor(s) Review

#### 2.1.1 Water Level Sensor

##### Working Principle

##### Signal Character

#### 2.1.2 Infrared Motion Sensor

##### Working Principle

##### Signal Character

#### 2.1.3 Photosensitive Light Sensor 

##### Working Principle

##### Signal Character

#### 2.1.4 Temperature and Humidity Sensor(DHT11)

##### Working Principle

* The DHT11 is a basic, ultra low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed).[[1]](http://kookye.com/2018/11/16/arduino-lesson-dht11-sensor/)


<div style="text-align: center">
<img src="Report/dht11-1.jpg"/>
</div>


<center>
   Figure 2-? DHT11
</center>

##### Signal Character

### 2.2 Circuit Connect

### 2.3 Demo Construction

---------------------

## 3. Demo Test

---------------------
## 4. Discussion


```markdown

import numpy as np
def indf():
    eee
    eee
    
```


