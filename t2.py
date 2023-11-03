import matlab.engine
import numpy as np
import matplotlib.pyplot as plt
eng = matlab.engine.start_matlab()
 
# t.initial_position[2,0] = 2
# t.set_initial_position(2)
tilt_degrees = 45
ini_dire_rad = np.deg2rad(tilt_degrees)  # initial direction angle. NE

t = eng.qd_track('linear', matlab.double([200]), ini_dire_rad);  
eng.eval("t.name = 'Terminal';", nargout=0) 
eng.eval('t.initial_position(3,1) = 2;', nargout=0) 



# Define a 10 m curve radius, and convert the angle from degrees to radians
curve_radius = 10
curve_angle_rad = np.deg2rad(135)
# Generate the curve coordinates
curve_points = 10 * np.exp(1j * np.arange(135, 45, -1) * np.pi / 180)
curve_points = curve_points[1:] - curve_points[0]

# Append the curve to the existing track
# new_positions = eng.horzcat(t.positions,
#                             [t.positions[0][-1] + np.real(curve_points),
#                              t.positions[1][-1] + np.imag(curve_points),
#                              np.zeros(len(curve_points))])
# eng.eval('t.positions = new_positions;', nargout=0)
# Access the positions using the positions_abs method
positions_abs = eng.positions_abs(t)
eng.workspace['new_positions'] = eng.horzcat(positions_abs,
                            [positions_abs[0][-1] + np.real(curve_points),
                             positions_abs[1][-1] + np.imag(curve_points),
                             np.zeros(len(curve_points))])
eng.eval('t.positions = new_positions;', nargout=0)


eng.calc_orientation(t, nargout=0)
print("success")
eng.quit()

