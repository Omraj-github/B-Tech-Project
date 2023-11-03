import matlab.engine
import numpy as np
import matplotlib.pyplot as plt

# Start the MATLAB engine
eng = matlab.engine.start_matlab()

# Convert degrees to radians for the tilt angle
tilt_degrees = 12
tilt_radians = np.deg2rad(tilt_degrees)

# Create a high-gain antenna
a = eng.qd_arrayant('multi', matlab.double(
    [8]), matlab.double([0.5]), matlab.double([tilt_radians]))

# Create a layout
l = eng.qd_layout()
# l.no_tx = 2  # Two BSs
# l.tx_position[:,1] = matlab.double([-200, 0, 25])  # Position of BS 1
# l.tx_position[:,2] = matlab.double([200, 0, 25])   # Position of BS 2

# Set the no_tx property using MATLAB-style syntax
eng.eval('l.no_tx = 2;', nargout=0)
# Set the tx_position property using MATLAB-style syntax
eng.eval('l.tx_position(:,1) = [-200, 0, 25];', nargout=0)
eng.eval('l.tx_position(:,2) = [200, 0, 25];', nargout=0)


# l.tx_array[1][1] = a  # Assign antenna to BS1
# l.tx_array[1][2] = a  # Assign antenna to BS2
# l.tx_array[1][2].rotate_pattern(180, 'z')  # Rotate BS2 antenna by 180 degrees

# Set the number of transmitters by creating track objects
# num_tx = 2  # Set the number of transmitters
# for i in range(num_tx):
#     trk = eng.qd_track()
#     trk.name = f'Tx{i + 1}'
#     # Set other properties of the track as needed
#     l.tx_track[1][i + 1] = trk  # Add the track to the layout
# # Now you have two transmitters in the layout
# l.no_tx = num_tx
# num_tx = 2  # Set the number of transmitters
# eng.eval(f'l.no_tx = {num_tx}', nargout=0)
# # Create track objects for transmitters and set their names using MATLAB
# for i in range(num_tx):
#     eng.eval(f'trk = qd_track;', nargout=0)
#     eng.eval(f'trk.name = ''Tx{i + 1}'';', nargout=0)
#     eng.eval(f'l.tx_track(1, {i + 1}) = trk;', nargout=0)


# # Create a plot of the layout
# eng.close('all', nargout=0)
# eng.set(0,'defaultTextFontSize', 18)
# Set MATLAB properties using eval
eng.eval("set(0,'defaultTextFontSize', 18);", nargout=0)
eng.eval("set(0,'defaultAxesFontSize', 18);", nargout=0)
eng.eval("set(0,'defaultAxesFontName','Times');", nargout=0)
eng.eval("set(0,'defaultTextFontName','Times');", nargout=0)
eng.eval("set(0,'defaultFigurePaperPositionMode','auto');", nargout=0)
eng.eval("set(0,'DefaultFigurePaperType','<custom>');", nargout=0)
eng.eval("set(0,'DefaultFigurePaperSize', [14.5, 7.8]);", nargout=0)


# eng.addpath(r'C:\Users\Omraj\Desktop\BTP\Quadriga\quadriga_src\@qd_layout')
# eng.addpath('C:\\Users\\Omraj\\Desktop\\BTP\\Quadriga\\quadriga_src\\@qd_layout')
# map, x_coords, y_coords = eng.power_map('3GPP_38.901_UMa_LOS', 'quick', 5, -500, 500, -500, 500, 1.5)
# map, x_coords, y_coords = eng.eval("l.power_map('3GPP_38.901_UMa_LOS', 'quick', 5, -500, 500, -500, 500, 1.5);", nargout=3)
# map, x_coords, y_coords = eng.eval("l.power_map('3GPP_38.901_UMa_LOS', 'quick', 5, -500, 500, -500, 500, 1.5);", nargout=3)
x1 = matlab.double([-500])
x2 = matlab.double([500])
# x1 = [-500]
# x2 = [500]
map, x_coords, y_coords = eng.power_map(
    l,
    # h_layout: The scenario for which the map shall be created.
    '3GPP_38.901_UMa_LOS',
    'quick',                  # usage: A string specifying the detail level.
    # sample_distance: Distance between sample points in [m] (default = 10 m)
    matlab.double([5]),
    # x_min, x_max: x-coordinates in [m] of the top left and bottom right corners
    x1, x2,
    # x_min, x_max: x-coordinates in [m] of the top left and bottom right corners
    x1, x2,
    # -500, 500,                # y_min, y_max: y-coordinates in [m] of the bottom right and top left corners
    # rx_height: Height of the receiver points in [m] (default = 1.5 m)
    matlab.double([1.5]),
    # tx_power: A vector of tx-powers (logarithmic scale in [dBm] or [dBW])
    matlab.double([0]),
    # 1                         # i_freq: The frequency index in case of multi-frequency simulations. Default: 1
    matlab.double([1]), nargout=3
)

# Call the power_map function and store the result in a single variable
# map = eng.power_map(
#     l,
#     '3GPP_38.901_UMa_LOS',
#     'quick',
#     matlab.double([5]),
#          x1, x2,
#          x1, x2,
#     matlab.double([1.5]),
#     matlab.double([0]),
#     matlab.double([1])
# )

# # Unpack the result into separate variables
# map = result[0]
# x_coords = result[1]
# y_coords = result[2]


P = 10*np.log10(np.sum(np.dstack(map), axis=2))

# eng.l.visualize([],[],0, nargout=0)
# plt.figure()
# plt.imshow(P, extent=(x_coords[0], x_coords[1], y_coords[0], y_coords[1]))
# plt.colorbar()
# plt.xlim(-500, 500)
# plt.ylim(-500, 500)
# plt.title('Incorrect antenna orientation')
# plt.show()


# plt.legend(['Tx-Position', 'Tx-Antenna', 'Tx-Track', 'Rx-Position', 'Rx-Antenna', 'Rx-Track'])
# plt.text(-200, 0, 'Tx-Position', color='r', fontsize=12)
# plt.text(-200, -25, 'Tx-Antenna', color='b', fontsize=12)
# plt.text(-200, -50, 'Tx-Track', color='g', fontsize=12)
# plt.text(200, 0, 'Rx-Position', color='r', fontsize=12)
# plt.text(200, -25, 'Rx-Antenna', color='b', fontsize=12)
# plt.text(200, -50, 'Rx-Track', color='g', fontsize=12)


# # Get the dynamic positions for Tx-Position and Tx-Antenna from MATLAB workspace
# tx_position = eng.workspace['l'].tx_position
# tx_position_x = [float(tx_position[0][i]) for i in range(len(tx_position[0]))]

# # Add legends with labels "Tx-Position" and "Tx-Antenna" at dynamic positions
# for x, label in zip(tx_position_x, ["Tx-Position", "Tx-Antenna"]):
#     plt.text(x, 0, label, color='r' if label == "Tx-Position" else 'b', fontsize=12)
# plt.text(-200, 0, label = 'Tx-Position', color='r', fontsize=12)
# plt.plot(-200, 0, 25,  label = 'Tx-Position')
# plt.text(200, 0, label = 'Tx-Antenna', color='b', fontsize=12)
# fig, ax = plt.subplots()


















# eng.visualize(l, [matlab.int16(-200), matlab.int16(0), matlab.int16(25)], [matlab.int16(200), matlab.int16(0), matlab.int16(25)], 0)
# tx_indices = [1, 2]  # Replace with the actual transmitter indices you want to visualize
# rx_indices = [1]     # Replace with the actual receiver indices you want to visualize

# eng.visualize(l, (tx_indices), (rx_indices), 0)
# Reshape P to match the expected shape (n_y_coords, n_x_coords)
# P = np.squeeze(P)  # Remove singleton dimensions if present
# extent = [np.min(x_coords), np.max(x_coords),
#           np.min(y_coords), np.max(y_coords)]




# Convert matlab.double objects to NumPy arrays
x_coords = np.array(x_coords)
y_coords = np.array(y_coords)
print("P shape:", P.shape)
print("x_coords shape:", x_coords.shape)
print("y_coords shape:", y_coords.shape)

# Reshape P to match the expected shape (n_y_coords, n_x_coords)
P = np.squeeze(P)  # Remove singleton dimensions if present

# Calculate the extent based on x_coords and y_coords
# extent = [x_coords.min(), x_coords.max(), y_coords.min(), y_coords.max()]

# extent = [np.min(x_coords), np.max(x_coords), np.min(y_coords), np.max(y_coords)]

# plt.figure()
# # Visualize the layout using imshow
# plt.imshow(P, extent=extent, origin='upper', aspect='auto')
# plt.colorbar()
# plt.xlim(extent[0], extent[1])
# plt.ylim(extent[2], extent[3])
# plt.title('Power Map Visualization')
# plt.xlabel('X Coordinate (m)')
# plt.ylabel('Y Coordinate (m)')
# plt.show()

# Stop the MATLAB engine
eng.quit()
