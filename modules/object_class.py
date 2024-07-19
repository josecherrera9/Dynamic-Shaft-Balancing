# Objects

import math

class Object:
    def __init__(self, mass, radius, position, angle, angular_velocity, results):
        self.mass = mass
        self.radius = radius
        self.position = position
        self.angle = math.radians(angle)
        self.angular_velocity = angular_velocity
        self.results = results
        self.force = None
        self.torque = None

    def calculate_forces(self):
        force = round(self.mass * self.radius * self.angular_velocity, 2)
        force_x = round(force * math.cos(self.angle), 2)
        force_y = round(force * math.sin(self.angle), 2)
        self.results['Force'].append(force)
        self.results['Force x'].append(force_x)
        self.results['Force y'].append(force_y)

    def calculate_torques(self):
        torque = round(self.mass * self.radius * self.angular_velocity * self.position, 2)
        torque_x = round(torque * math.cos(self.angle), 2)
        torque_y = round(torque * math.sin(self.angle), 2)
        self.results['Torque'].append(torque)
        self.results['Torque x'].append(torque_x)
        self.results['Torque y'].append(torque_y)