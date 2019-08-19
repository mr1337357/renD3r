RenD3r:
___
3D renderer in python\
How it works:
__
1. generator creates a set of vectors representing a 3d object
2. each vector is transformed across matrices to set orientation of the object
3. also translated to set its point in 3d space
4. then x and y are divided by z to figure out what point on the screen it's behind
