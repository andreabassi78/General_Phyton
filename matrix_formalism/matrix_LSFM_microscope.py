import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Define ABCD matrices
def lens(f):
    """Ray transfer matrix for a thin lens of focal length f."""
    return np.array([[1, 0], [-1/f, 1]])

def space(d):
    """Ray transfer matrix for free space of distance d."""
    return np.array([[1, d], [0, 1]])

# Initial beam parameters
mm = 1e-3
um = 1e-6
deg = np.pi/180

lambda_ = 0.561 * um  # wavelength of laser (m)
x0 = 0.5 * mm 
theta0 = -0.01 * deg 
w0 = 2.8 * um  # Initial beam waist

f0 = 40*mm  # first objective focal length and distance from chip
f1 = 150*mm  # lens 1
f2 = 150*mm # lens 2
f3 = 200*mm # tube lens
f4 = 3.3 * mm # objective lens

# Define function to compute the matrix from the chip to the pupil of the microscope objective
def compute_matrix():
     
    M0 = space(f0)  # distance from the chip
    M1 = lens(f0)  # 
    M2 = space(f0*0.7)  # 
    
    M3 = space(f1)  # 
    M4 = lens(f1)  # 
    M5 = space(f1)  #

    #M_extra = lens(-3000*mm) # correction lens in the pupil plane
    #M5= M_extra @ M5 
    
    M6 = space(f2)  # 
    M7 = lens(f2)  # 
    M8 = space(f2)  # 
    
    M9 = space(f3)  # 
    M10 = lens(f3)  # tube lens
    M11 = space(f3)  #

    # Compute total ABCD matrix
    M_total =  M11 @ M10 @ M9 @ M8 @ M7 @ M6 @ M5 @ M4 @ M3 @ M2 @ M1 @ M0
    
    return M_total


def compute_x1(z):
    M0 = compute_matrix()
    M12 = space(f4)  # distance from the pupil
    M13 = lens(f4)  # objective lens
    M14 = space(z)  # distance from the sample
    M_total =  M14 @ M13 @ M12 @ M0
    A, B, C, D = M_total.flatten()

    return abs(A * x0 + B * theta0)  # Minimize the absolute beam displacement

def compute_x_theta_at_the_pupil():
    # computes theta at the pupil
    M = compute_matrix()
    # Extract ABCD elements
    A, B, C, D = M.flatten()
    return A*x0+B*theta0 , C*x0+D*theta0  

# Optimize z to minimize x1
result = minimize_scalar(compute_x1, bounds=(0, 2*f4), method='bounded')

# Best z found
z_opt = result.x
x1_opt = compute_x1(z_opt)
x_pupil,theta_pupil = compute_x_theta_at_the_pupil()

# Compute waist at focus position
def compute_waist_at_z(w0, lambda_,z):
    z_rayleigh = np.pi * w0**2 / lambda_  # Rayleigh range
    q0 = 1j * z_rayleigh  # Initial complex beam parameter
    M0 = compute_matrix()
    M12 = space(f4)  # distance from the pupil
    M13 = lens(f4)  # objective lens
    M14 = space(z)  # distance from the sample
    M_total =  M14 @ M13 @ M12 @ M0
    A, B, C, D = M_total.flatten()
    # Beam parameter transformation
    q_z = (A * q0 + B) / (C * q0 + D)
    w_z = np.sqrt(-lambda_ / (np.pi * np.imag(1/q_z)))  # Compute beam waist
    return w_z

w_focus = compute_waist_at_z(w0, lambda_, z_opt)


# Compute waist at the pupil
def compute_waist_at_pupil(w0, lambda_):
    z_rayleigh = np.pi * w0**2 / lambda_  # Rayleigh range
    q0 = 1j * z_rayleigh  # Initial complex beam parameter
    M = compute_matrix()
    A, B, C, D = M.flatten()
    q_pupil = (A * q0 + B) / (C * q0 + D)
    w_pupil = np.sqrt(-lambda_ / (np.pi * np.imag(1/q_pupil)))  # Compute beam waist at the pupil
    return w_pupil

w_pupil = compute_waist_at_pupil(w0, lambda_)


# Display results
def display_results():
    print(f"Optimal focus position z: {z_opt/mm:.4f} mm")
    print(f"Distance x at the pupil: {x_pupil/mm:.4f} mm")
    print(f"Angle at the pupil: {theta_pupil/deg:.4f} deg")
    print(f"Distance x from optical axis at focus position : {x1_opt/um:.4f} um")
    print(f"Beam waist at focus position: = {w_focus/um:.4f} um")
    print(f"Beam waist at pupil: {w_pupil/um:.4f} um")

display_results()