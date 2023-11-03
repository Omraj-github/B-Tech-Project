classdef triarea < handle
    properties (SetAccess = private)
        Base = 1;
        Height = 1;
    end
    
    methods
        function TR = Triangle(obj, b, h)
            obj.Base = b;
            obj.Height = h;
        end
        function a = tarea(this)
            a = 0.5*(this.Base* this.Height);
        end
    end
end