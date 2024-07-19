# Dynamic-Shaft-Balancing 
<p align="justify"> Python-based software for shaft balancing, specifically designed for systems with two bearings. Computes forces and moments using vector summation and provides correction masses for balance. 

<p align="justify"> This application is designed to assist with the calculation and visualization of forces and torques in a shaft balancing system. It uses Python and the customtkinter library for the user interface, allowing users to input various parameters and visualize the resulting forces and torques.

Project Structure

_main.py:_ The main script where the application is executed and the user interface is set up.

_object_class.py:_ Defines the Object class, which represents a mass on the shaft causing imbalance.

_data_management.py:_ Contains the functions that perform calculations and generate plots.

The object_class.py and data_management.py files are located in the modules directory. 



# Dependencies

_Python 3.x_

_customtkinter_

_matplotlib_

# Installation
* Clone the repository:

git clone <https://github.com/josecherrera9/Dynamic-Shaft-Balancing>

cd shaft-balancing

* Install the required dependencies:

pip install customtkinter matplotlib

# Usage

* Run the application:

python main.py

* Enter the following parameters in the provided entry fields:

_Mass_

_Radius_

_Angle_

_Length_

_Angular Velocity_

_Bearing B Position_

_Bearing A Position_

_Shaft Length_


* Choose the measurement system (Metric or Imperial) and the unit for angular velocity (rad/s or rpm) using the provided switches.

* Click "Add Object" to add the specified object to the system.

* Click "Calculate" to compute the forces and torques and display the results.

* Click "Delete" to remove the last added object from the system.

____________________________________________________________________________

# Files Description

* main.py
 <p align="justify"> This file sets up the user interface and handles user interactions. It contains the setup_ui function, which creates entry fields, buttons, and switches for inputting parameters and controlling the application. The setup_ui function also includes the main event loop to run the application.

* object_class.py
 <p align="justify"> Defines the Object class, which represents a mass on the shaft. The class includes methods to calculate forces and torques based on the object's properties and the input parameters.

* data_management.py
 <p align="justify"> Contains the functions that manage data input, perform calculations, and generate plots. These functions include get_data, update_table, delete, calculate, add_label, and plotting.
