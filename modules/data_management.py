# Functions

import math
from tkinter import ttk
import customtkinter as ctk
from modules.object_class import Object
import matplotlib.pyplot as plt

global objects, counter, system_dict, angular_velocity, position_b

counter = 1
system_dict = {}
objects = {}

def get_data(mass, radius, angle, angular_velocity, system, rotation, length, frame, results):
    global counter, system_dict, objects
    
    metric_system = {'Mass': '(kg)', 'Length': '(m)', 'Force': 'N', 'Torque': 'N·m'}
    imperial_system = {'Mass': '(oz)', 'Length': '(in)', 'Force': 'lb', 'Torque': 'lb·in'}
    
    angular_velocity = float(angular_velocity)
    system = system
    rotation = rotation

    if system == 'Metric':
        system_dict = metric_system
        
    elif system == 'Imperial':
        system_dict = imperial_system

    if angular_velocity == 0:
        angular_velocity = 1

    elif angular_velocity != 0:
        if rotation == 'rpm':
            angular_velocity = (2 * math.pi / 60) * angular_velocity
        elif rotation == 'rad/s':
            pass
    else:
        pass

    new_object = Object(mass = mass, radius = radius, position = length,
                        angle=angle, angular_velocity = angular_velocity, results = results)
    object_name = f'Object {counter}'

    objects[object_name] = new_object
    results['Name'].append(object_name)

    new_object.calculate_forces()
    new_object.calculate_torques()

    update_table(frame = frame, objects = objects)

    counter += 1


def update_table(frame, objects):
    global table
    global system_dict

    columns = (f"Mass {system_dict['Mass']}", 
               f"Radius {system_dict['Length']}", 
               f"Position {system_dict['Length']}", 
               "Angle (°)")

    if 'table' in globals():
        for item in table.get_children():
            table.delete(item)
    else:
        table = ttk.Treeview(frame, columns = columns, show = 'headings')
        for col in columns:
            table.heading(col, text = col)
            table.column(col, minwidth = 0, width = 100)
        table.pack(expand = True, fill = 'both')

    for obj_name, obj in objects.items():
        table.insert("", "end", values = (obj.mass,
                                        obj.radius,
                                        obj.position,
                                        f'{math.degrees(obj.angle):.2f}'))


def delete(frame):
    global system_dict
    global objects
    global counter

    if counter <= 1:
        counter = 1
        pass

    else:
        counter -= 1
        object_name = f'Object {counter}'
        del objects[object_name]
        
    update_table(frame = frame, objects = objects)


def calculate(results, app, position_b):

    coordinates = {'Force': [], 'Torque': [], 'Angle': [], 'Force x': [0],
                   'Force y': [0], 'Torque x': [0], 'Torque y': [0]}
    f_x, f_y, t_x, t_y = 0, 0, 0, 0
    
    for element in range(len(results['Name'])):

        current_force_x = results['Force x'][element]
        current_force_y = results['Force y'][element]
        current_torque_x = results['Torque x'][element]
        current_torque_y = results['Torque y'][element]

        f_x += current_force_x
        f_y += current_force_y
        t_x += current_torque_x
        t_y += current_torque_y

        coordinates['Force x'].append(f_x)
        coordinates['Force y'].append(f_y)
        coordinates['Torque x'].append(t_x)
        coordinates['Torque y'].append(t_y)

    torque_b_x = -1 * coordinates['Torque x'][-1]
    torque_b_y = -1 * coordinates['Torque y'][-1]
    torque_b = math.sqrt(torque_b_x ** 2 + torque_b_y ** 2)
    angle_b = math.atan2(torque_b_y, torque_b_x)

    force_b = torque_b / position_b
    force_b_x = force_b * math.cos(angle_b)
    force_b_y = force_b * math.sin(angle_b)

    force_a_x = -1 * (coordinates['Force x'][-1] + force_b_x)
    force_a_y = -1 * (coordinates['Force y'][-1] + force_b_y)
    force_a = math.sqrt(force_a_x ** 2 + force_a_y ** 2)
    angle_a = math.atan2(force_a_y, force_a_x)

    coordinates['Force x'].append(coordinates['Force x'][-1] + force_b_x)
    coordinates['Force y'].append(coordinates['Force y'][-1] + force_b_y)
    coordinates['Force x'].append(coordinates['Force x'][-1] + force_a_x)
    coordinates['Force y'].append(coordinates['Force y'][-1] + force_a_y)
    coordinates['Force x'].append(force_b_x)
    coordinates['Force y'].append(force_b_y)
    coordinates['Force x'].append(force_a_x)
    coordinates['Force y'].append(force_a_y)
    coordinates['Torque x'].append(coordinates['Torque x'][-1] + torque_b_x)
    coordinates['Torque y'].append(coordinates['Torque y'][-1] + torque_b_y)

    coordinates['Force'].append(force_a)
    coordinates['Force'].append(force_b)
    coordinates['Torque'].append(torque_b)
    coordinates['Angle'].append(math.degrees(angle_a))
    coordinates['Angle'].append(math.degrees(angle_b))

    y_pos_r = 0.5
    y_pos_l = 0.5

    for element, values in coordinates.items():
        if element not in ['Torque x', 'Torque y']:
            if len(values) > 2:
                add_label(app, f'{element} B', values[-2], y_pos_r, 'w', 0.7)
                add_label(app, f'{element} A', values[-1], y_pos_l, 'w', 0.5)
                y_pos_r += 0.05
                y_pos_l += 0.05
            elif len(values) == 2:
                add_label(app, f'{element} B', values[-1], y_pos_r, 'w', 0.7)
                add_label(app, f'{element} A', values[-2], y_pos_l, 'w', 0.5)
                y_pos_r += 0.05
                y_pos_l += 0.05
            else:
                add_label(app, f'{element} B', values[-1], y_pos_r, 'w', 0.7)
                y_pos_r += 0.05

    plotting(coordinates = coordinates)

def add_label(app, text, value, y_pos, anchor, relx):
    label = ctk.CTkLabel(app, text = f'{text}: {value:.2f}',
                         bg_color = 'black', fg_color = 'gray', text_color = 'white',
                         font = ('Courier New', 13), corner_radius = 5)
    label.place(relx = relx, rely = y_pos, anchor = anchor)


def plotting(coordinates):
    del coordinates['Force x'][-1]
    del coordinates['Force x'][-1]
    del coordinates['Force y'][-1]
    del coordinates['Force y'][-1]

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(x = coordinates['Force x'], y = coordinates['Force y'], label = 'Force', color = 'blue')
    plt.plot(coordinates['Force x'], coordinates['Force y'], label = 'Force', color = 'red')

    plt.xlabel('i')
    plt.ylabel('j')
    plt.title('Torque')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.scatter(x = coordinates['Torque x'], y = coordinates['Torque y'], label = 'Torque', color = 'red')
    plt.plot(coordinates['Torque x'], coordinates['Torque y'], label = 'Torque', color = 'blue')
    plt.xlabel('i')
    plt.ylabel('j')
    plt.title('Force')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()