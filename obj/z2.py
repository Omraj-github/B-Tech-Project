
import matlab.engine
import numpy as np

eng = matlab.engine.start_matlab()

myObj = eng.MyObject(2, 3)

output = eng.MyFunction(myObj, 4, 5)

# eng.disp(output)
print(output)
