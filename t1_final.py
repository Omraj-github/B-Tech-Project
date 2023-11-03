import matlab.engine
import numpy as np
import matplotlib.pyplot as plt

# Start the MATLAB engine
eng = matlab.engine.start_matlab()

# Convert degrees to radians for the tilt angle
tilt_degrees = 12
tilt_radians = np.deg2rad(tilt_degrees)

# Create a high-gain antenna
a1 = eng.qd_arrayant('multi', matlab.double([8]), matlab.double([0.5]), matlab.double([tilt_radians]))
a2 = eng.qd_arrayant('multi', matlab.double([8]), matlab.double([0.5]), matlab.double([tilt_radians]))

# Create a layout
l = eng.qd_layout()
eng.workspace['l'] = l
# eng.eval('l.no_tx = 2;', nargout=0)

# Set the no_tx property using MATLAB-style syntax
eng.eval('l.no_tx = 2;', nargout=0)
# l.no_tx = 2

eng.eval('l.tx_position(:,1) = [-200, 0, 25];', nargout=0)
eng.eval('l.tx_position(:,2) = [200, 0, 25];', nargout=0)


# Assign antennas to base stations by passing the 'a' variable
eng.workspace['a1'] = a1
eng.workspace['a2'] = a2
# Assign antennas to base stations
eng.eval('l.tx_array(1,1) = a1;', nargout=0)
eng.eval('l.tx_array(1,2) = a2;', nargout=0)

# Rotate the antenna for BS2
eng.eval("l.tx_array(1,2).rotate_pattern(180, 'z');", nargout=0)

eng.eval("set(0,'defaultTextFontSize', 18);", nargout=0)
eng.eval("set(0,'defaultAxesFontSize', 18);", nargout=0)
eng.eval("set(0,'defaultAxesFontName','Times');", nargout=0)
eng.eval("set(0,'defaultTextFontName','Times');", nargout=0)
eng.eval("set(0,'defaultFigurePaperPositionMode','auto');", nargout=0)
eng.eval("set(0,'DefaultFigurePaperType','<custom>');", nargout=0)
eng.eval("set(0,'DefaultFigurePaperSize', [14.5, 7.8]);", nargout=0)

x1 = matlab.double([-500])
x2 = matlab.double([500])

map, x_coords, y_coords = eng.power_map(
    l,
    # h_layout: The scenario for which the map shall be created.
    '3GPP_38.901_UMa_LOS',
    'quick',                  # usage: A string specifying the detail level.
    # sample_distance: Distance between sample points in [m] (default = 10 m)
    matlab.double([5]),
    # x_min, x_max: x-coordinates in [m] of the top left and bottom right corners
    x1, x2,
    # y_min, y_max: y-coordinates in [m] of the bottom right and top left corners
    x1, x2,
    # -500, 500,
    # rx_height: Height of the receiver points in [m] (default = 1.5 m)
    matlab.double([1.5]),
    # tx_power: A vector of tx-powers (logarithmic scale in [dBm] or [dBW])
    matlab.double([0]),
    # 1                         # i_freq: The frequency index in case of multi-frequency simulations. Default: 1
    matlab.double([1]), nargout=3
)
# print(map)


P = 10*np.log10(np.sum(np.dstack(map), axis=2))
# print(P)
# eng.visualize(l, [], [], 0)

plt.imshow(P, extent=[-500, 500, -500, 500])
plt.colorbar() 

marker_size = 100
plt.scatter(0, 0, c='b', marker='+', s= marker_size, label='Rx-Position')
plt.scatter(0, 0, c='b', marker='o', s= 30, label='Rx-Antenna')
Tx = 200
Ty = 0
Tz = 25
Tx1 = -200
Ty1 = 0
Tz1 = 25
plt.scatter(Tx, Ty, c='r', marker='x', s=marker_size)
plt.scatter(Tx, Ty, c='r', marker='^', s=40)

plt.scatter(Tx1, Ty1, c='r', marker='x', s=marker_size, label='Tx-Position')
plt.scatter(Tx1, Ty1, c='r', marker='^', s=50, label='Tx-Antenna')

# Specify the size of the marker (e.g., 100 points)

# Create the plot and mark the point with a custom marker size

plt.legend()

# plt.clim(np.max(P) - 20, np.max(P))
plt.title('Correct antenna orientation')
plt.grid(True, which='both', color='white', linewidth=1)
plt.gca().set_facecolor('black')  # Set the background color This function gets the current axes, which is the part of the plot where you will be drawing your data.
plt.xlabel('x-coord in [m]')
plt.ylabel('y-coord in [m]')
# plt.zlabel('z-coord in [m]')

plt.show()

# Stop the MATLAB engine
eng.quit()

#'+': A plus sign marker.
# 'o': A circle marker.
# 's': A square marker.
# '*': An asterisk marker.
# '.': A point marker (a small dot).
# 'x': A cross marker.
# 'D': A diamond marker.
# 'v': A triangle-down marker.
# '^': A triangle-up marker.
# '<': A triangle-left marker.
# '>': A triangle-right marker.
# 'p': A pentagon marker.
# 'h': A hexagon1 marker.
# 'H': A hexagon2 marker.