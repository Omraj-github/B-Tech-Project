import matlab.engine 
eng = matlab.engine.start_matlab()

# Run a MATLAB script that creates an instance of the triarea class
eng.eval("obj = triarea;", nargout=0)
# obj = eng.triarea()

# Set the base and height using the class method
eng.eval("obj.Triangle(1, 5);", nargout=0)

# Calculate the area using the class method
eng.eval("a = obj.tarea();", nargout=0)

# Retrieve the value of 'a' from the MATLAB workspace
eng.eval("result = a;", nargout=0)
area = eng.workspace['result']
print(area)
# Quit MATLAB engine
eng.quit()


# t = eng.triarea()
# t.Triangle( matlab.double([1]),  matlab.double([5]))
# area = t.tarea(nargout = 1)
# print(area) 

# ret = eng.triarea(matlab.double([1]),matlab.double([5]))
# print(ret)
