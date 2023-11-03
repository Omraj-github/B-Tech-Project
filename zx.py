# import mat4py
import matlab.engine
import numpy as np
import matplotlib.pyplot as plt
 
eng = matlab.engine.start_matlab()
tilt_degrees = 12
tilt_radians = np.deg2rad(tilt_degrees)

# Create a high-gain antenna
a1 = eng.qd_arrayant('multi', matlab.double([8]), matlab.double([0.5]), matlab.double([tilt_radians]))
a2 = eng.qd_arrayant('multi', matlab.double([8]), matlab.double([0.5]), matlab.double([tilt_radians]))
 
# eng.load('qd_layout.m')

l = eng.qd_layout()
# Now, you can set the 'no_tx' property of the layout within the MATLAB engine workspace
eng.workspace['l'] = l
eng.eval('l.no_tx = 2;', nargout=0)
# eng.set(l, 'no_tx', 2)
# l.no_tx = 2
# eng.set_no_tx(l, 2)
# l.set.no_tx( 2)
# eng.eval('set(l, "no_tx", 2);', nargout=0)
# eng.eval('l.no_tx = 2;', nargout=0) 

map, x_coords, y_coords = eng.power_map(
    l,
    '3GPP_38.901_UMa_LOS',
    'quick',    # sample_distance: Distance between sample points in [m] (default = 10 m)
    matlab.double([5]),    # x_min, x_max: x-coordinates in [m] of the top left and bottom right corners
    matlab.double([-500]), matlab.double([500]),    # y_min, y_max: y-coordinates in [m] of the bottom right and top left corners
    matlab.double([-500]), matlab.double([500]),    # -500, 500,    # rx_height: Height of the receiver points in [m] (default = 1.5 m)
    matlab.double([1.5]),    # tx_power: A vector of tx-powers (logarithmic scale in [dBm] or [dBW])
    matlab.double([0]),
   # 1                         # i_freq: The frequency index in case of multi-frequency simulations. Default: 1
    matlab.double([1]), nargout=3
)


P = 10*np.log10(np.sum(np.dstack(map), axis=2))
# eng.visualize(l, [-200, 0, 25], [200, 0, 25], 0)

eng.visualize(l, [], [], 0)
eng.quit()
