RenD3r:
3D renderer in python
How it works:
generator creates a set of vectors representing a 3d object
each vector is transformed across matrices to set orientation of the object
also translated to set its point in 3d space
then x and y are divided by z to figure out what point on the screen it's behind
