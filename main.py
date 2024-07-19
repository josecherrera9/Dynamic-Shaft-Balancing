# Main

import customtkinter as ctk
from modules.data_management import get_data, delete, calculate

global counter, results, angular_velocity

counter = 1
results = {
    'Name': [],
    'Force': [],
    'Force x': [],
    'Force y': [],
    'Torque': [],
    'Torque x': [],
    'Torque y': []
}

def setup_ui():
    global switch_system, switch_rotation, frame

    app = ctk.CTk()
    app.geometry("900x900")
    app.title("CTk Example")

    entry_mass = ctk.CTkEntry(app, placeholder_text = 'Mass')
    entry_mass.place(relx = 0.17, rely = 0.1, anchor = 'w')

    entry_radius = ctk.CTkEntry(app, placeholder_text = 'Radius')
    entry_radius.place(relx = 0.17, rely = 0.2, anchor = 'w')

    entry_angle = ctk.CTkEntry(app, placeholder_text = 'Angle')
    entry_angle.place(relx = 0.17, rely = 0.3, anchor = 'w')

    entry_length = ctk.CTkEntry(app, placeholder_text = 'Length')
    entry_length.place(relx = 0.17, rely = 0.4, anchor = 'w')

    entry_angular_velocity = ctk.CTkEntry(app, placeholder_text = 'Angular Velocity')
    entry_angular_velocity.place(relx = 0.3, rely = 0.5, anchor = 'w')

    entry_b = ctk.CTkEntry(app, placeholder_text = 'Bearing B Position', width = 147)
    entry_b.place(relx = 0.17, rely = 0.5, anchor = 'w')

    entry_a = ctk.CTkEntry(app, placeholder_text = 'Bearing A Position', width = 147)
    entry_a.place(relx = 0.3, rely = 0.55, anchor = 'w')

    entry_shaft = ctk.CTkEntry(app, placeholder_text = 'Shaft Length')
    entry_shaft.place(relx = 0.17, rely = 0.55, anchor = 'w')

    frame = ctk.CTkFrame(app, width = 700, height = 200)
    frame.place(relx = 0.5, rely = 0.25, anchor = 'w')

    add_button = ctk.CTkButton(app, text = 'Add Object', command = lambda: get_data(
        mass = float(entry_mass.get()), 
        radius = float(entry_radius.get()),
        angle = float(entry_angle.get()),
        angular_velocity = entry_angular_velocity.get(), 
        system = switch_system.get(), 
        rotation = switch_rotation.get(),
        length = float(entry_length.get()),
        results = results,
        frame = frame
    ))
    add_button.place(relx = 0.05, rely = 0.6, anchor = 'w')

    calculate_button = ctk.CTkButton(app, text = 'Calculate', command = lambda: calculate(
        position_b = float(entry_b.get()), 
        results = results, 
        app = app
    ))
    calculate_button.place(relx = 0.3, rely = 0.6, anchor = 'w')

    delete_button = ctk.CTkButton(app, text = 'Delete', command = lambda: delete(
        frame = frame
    ))
    delete_button.place(relx = 0.17, rely = 0.7, anchor = 'w')

    switch_system = ctk.CTkSwitch(app, text = '', onvalue = 'Metric', offvalue = 'Imperial')
    switch_system.place(relx = 0.3, rely = 0.05, anchor = 'w')

    label_system_imperial = ctk.CTkLabel(app, text = 'Imperial', fg_color = 'transparent')
    label_system_imperial.place(relx = 0.24, rely = 0.05, anchor = 'w')

    label_system_metric = ctk.CTkLabel(app, text = 'Metric', fg_color = 'transparent')
    label_system_metric.place(relx = 0.35, rely = 0.05, anchor = 'w')

    switch_rotation = ctk.CTkSwitch(app, text = '', onvalue = 'rad/s', offvalue = 'rpm')
    switch_rotation.place(relx = 0.60, rely = 0.05, anchor = 'w')

    label_rotation_rpm = ctk.CTkLabel(app, text = 'rpm', fg_color = 'transparent')
    label_rotation_rpm.place(relx = 0.56, rely = 0.05, anchor = 'w')

    label_rotation_rad = ctk.CTkLabel(app, text = 'rad/s', fg_color = 'transparent')
    label_rotation_rad.place(relx = 0.65, rely = 0.05, anchor = 'w')

    app.mainloop()

if __name__ == '__main__':
    setup_ui()