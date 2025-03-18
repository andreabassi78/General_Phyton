import numpy as np
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

lambda_ = 0.473 * um  # wavelength of laser (m)
x0 = 0.000001 * mm 
theta0 = -0.000001 * deg 
w0 = 3.4 * mm  # Initial beam waist

f0 = 100*mm  # cyl lens
f1 = 100*mm  # lens 1
f2 = 150*mm # lens 2
f3 = 200*mm # tube lens
M = 20 # magnification of the microscope objectives 

f4 = 200*mm/M # objective lens (assuming lens from Leica/Nikon/Thorlabs)

f_tune = -250*mm # tunable lens

# Define function to compute the matrix from the chip to the pupil of the microscope objective
def compute_matrix():
     
    M0 = space(f0)  # 
    M1 = lens(f0)  # cyl lens
    M2 = space(f0)  # 
    
    M3 = space(f1)  # 
    M4 = lens(f1)  # 
    M5 = space(f1)  #

    M_tune = lens(f_tune) # tunable lens in the focus of f1 and f2
    M5 = M_tune @ M5

    M6 = space(f2)  # 
    M7 = lens(f2)  # 
    M8 = space(f2)  # 
    
    M9 = space(f3)  # 
    M10 = lens(f3)  # tube lens
    M11 = space(f3)  #

    M12 = space(f4)  # distance from the pupil
    M13 = lens(f4)  # objective lens
    M14 = space(f4)  # distance from the sample
    

    M_total =  M14 @ M13 @ M12 @ M11 @ M10 @ M9 @ M8 @ M7 @ M6 @ M5 @ M4 @ M3 @ M2 @ M1 @ M0
    # A, B, C, D = M_total.flatten()
    # Compute total ABCD matrix
    
    return M_total

def compute_waist(z):
    z_rayleigh = np.pi * w0**2 / lambda_  # Rayleigh range
    q0 = 1j * z_rayleigh  # Initial complex beam parameter
    M_in_focus = compute_matrix()
    Mz = space(z)  # distance from the sample
    Mtot =  Mz @ M_in_focus 
    A, B, C, D = Mtot.flatten()
    # Beam parameter transformation
    q_z = (A * q0 + B) / (C * q0 + D)
    w_z = np.sqrt(-lambda_ / (np.pi * np.imag(1/q_z)))  # Compute beam waist
    return w_z


# Optimize z to minimize w
result = minimize_scalar(compute_waist, bounds=(-2*f4, 2*f4), method='bounded')

# Best z found
z_opt = result.x
w_opt = compute_waist(z_opt)


# Display results
def display_results():
    print(f"Optimal focus position z: {z_opt/mm:.4f} mm")
    print(f"Beam waist at focus position: = {w_opt/um:.4f} um")

display_results()