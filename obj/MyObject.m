classdef MyObject
    properties
        Property1
        Property2
    end
    
    methods
        function obj = MyObject(prop1, prop2)
            obj.Property1 = prop1;
            obj.Property2 = prop2;
        end
    end
end


%myObj = MyObject(2, 3);
%output = MyFunction(myObj, 4, 5);
%disp(output);
