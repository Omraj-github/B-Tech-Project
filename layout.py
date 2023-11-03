import matlab.engine 
eng = matlab.engine.start_matlab()
m = matlab.engine.connect_matlab()

# Define the layout object
# layout = eng.qd_layout()
# eng.set.no_tx(layout, matlab.double([2]))
# eng.set.no_tx(layout, 2.0 ,nargout=0)

# eng.eval("l = qd_layout;", nargout=0)
# eng.eval("l.no_tx(l, 2);", nargout=0)

# eng.eval("layo = l;", nargout=0)
# layout = eng.workspace['layo']

m.life(nargout=0)
# eng.visualize(layout, [], [], 0)
# Quit the MATLAB engine
eng.quit()
