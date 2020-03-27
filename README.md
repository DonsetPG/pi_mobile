# pi_mobile

Disclaimer: The codes are messy and we do not plan on cleaning them nor taking care of the repo.

# Overview :

The PI Mobile is an AI powered car built with a RaspberryPi and Lego. The goal was to use :

* Lego to build the car
* Lego Motor to power it
* a RaspberryPi to run the algorithm 
* a BrickPi3 to link the Lego motors and the RaspberryPi

A better overview of the project is available here : https://donsetpg.github.io/blog/2020/03/13/Pimobile/

# Remote connection to the RaspberryPi :

We used [VNC viewer](https://www.realvnc.com/fr/connect/download/viewer/) to connect to the RaspberryPi from our own computer. You only need them to share the same wifi to be able to do so. After that, use the ip address of the raspberry to connect from you computer L

```
hostname -I
```

# Connecting the Lego motor to the RaspberryPi :

We used a BrickPi3 from [Dexter Industries](https://www.dexterindustries.com/) to achieve this. 

The repo can be install with :

```
curl -kL dexterindustries.com/update_brickpi3 | bash
```

You can then easily perform a lot of operations :

```python3
import brickpi3
# Create a object to manage the motors :
BP = brickpi3.BrickPi3()
```

You can then access the motors with the port they are connected to :

```python3
BP.set_motor_power(BP.PORT_A,100)
```

# Driving the car :

## Remotely : 

You can use the BrowserBot folder to remotely control the car. Simply run :

```
python RPi_Server_Code.py
```

on the Rpi, and launch Browser_Client_Code.html on your computer. Enter the ip address of the Rpi to remotely control it. 

We changed the original version of this code to make sure we could save the cameras inputs, and our inputs as well. 

## DRL and IL:

The main classes we used are available in the DRL folder. The IL folder contains a notebook precossing the frames, linking them with inputs and setting up a model. It also contains a script to run the Rpi. 

