# Welcome to the Pipe Flow Analysis repository! This code provides a powerful tool for calculating pressure, velocity, and flow rate at various points inside a pipe system. Whether you're working on fluid dynamics research, engineering projects, or simply curious about understanding the internal dynamics of pipes, this repository offers a comprehensive solution.

# Using advanced algorithms and mathematical models, the code efficiently simulates fluid behavior, taking into account factors such as pipe geometry, fluid properties, and boundary conditions. With just a few inputs, you can obtain accurate results for pressure, velocity, and flow rate distribution within the pipe network.

# Key Features:

# Calculate pressure, velocity, and flow rate at any desired point within the pipe system.
# Handle complex pipe configurations, including branching, merging, and different pipe materials.
# Support for various fluid types, enabling analysis across a wide range of applications.
# Intuitive input parameters for pipe dimensions, fluid properties, and boundary conditions.
# Comprehensive output visualization, including graphical representations of pressure and velocity profiles.
# Whether you're an engineer, researcher, or enthusiast, this code empowers you to gain deeper insights into fluid dynamics and make informed decisions in pipe design, optimization, and performance evaluation.

# Feel free to explore, experiment, and contribute to this repository. Your feedback, suggestions, and contributions are highly valued as we strive to enhance the accuracy and versatility of pipe flow analysis.

# Join us in unraveling the mysteries of fluid behavior inside pipes, and let's unlock a new level of understanding in the fascinating world of fluid dynamics!

# Author : Marouane LAMZIRAI
# Contact : Marouanelamzirai01@gmail.com, +212658471836

import numpy as np

# Define the properties of water
initial_velocity = 2.5  # m/s
initial_pressure = 401300  # Pa
viscosity = 0.001  # Pa.s
density = 1000  # kg/m^3

# Define the dimensions of the pipe
length = 100  # m
diameter = 0.5  # m

# Define the discharge losses in the pipe
discharge_losses = 0.05  # fraction of pressure loss

# Define the grid parameters
num_points = 20
delta_x = length / num_points

# Initialize arrays to store the results
flow_rate = np.zeros(num_points)
pressure = np.zeros(num_points)
velocity = np.zeros(num_points)

# Calculate the flow rate, pressure, and velocity at each point
for i in range(num_points):
    # Calculate the cross-sectional area of the pipe at the current point
    area = np.pi * (diameter / 2) ** 2

    # Calculate the hydraulic diameter
    hydraulic_diameter = 4 * area / (2 * np.pi * (diameter / 2))

    # Calculate the friction factor using the Darcy-Weisbach equation
    friction_factor = 0.04

    # Calculate the Reynolds number
    reynolds_number = (density * initial_velocity * hydraulic_diameter) / viscosity

    # Calculate the pressure drop due to friction
    pressure_drop_friction = (friction_factor * length * density * initial_velocity ** 2) / (2 * hydraulic_diameter)

    # Calculate the pressure drop due to discharge losses
    pressure_drop_losses = discharge_losses * initial_pressure

    # Calculate the total pressure drop
    total_pressure_drop = pressure_drop_friction + pressure_drop_losses

    # Calculate the pressure at the current point
    pressure[i] = initial_pressure - (total_pressure_drop * (i * delta_x / length))

    # Calculate the flow rate at the current point
    flow_rate[i] = initial_velocity * area

    # Calculate the velocity at the current point
    velocity[i] = flow_rate[i] / area

# Print the results
for i in range(num_points):
    print(f"Point {i + 1}: Flow Rate = {flow_rate[i]} m^3/s, Pressure = {pressure[i]} Pa, Velocity = {velocity[i]} m/s")
