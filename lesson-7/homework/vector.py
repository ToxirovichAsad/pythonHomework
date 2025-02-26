class vector:
    def __init__(self, *component):
        self.component = tuple(component)

    # Represent as a human-readable vector
    def __repr__(self):
        return f"Vector{self.component}"

    # Vector addition
    def __add__(self, other):
        if len(self.component) != len(other.component):
            raise ValueError("Vector should have the same dimensions")
        return vector(*[a + b for a, b in zip(self.component, other.component)])

    # Vector subtraction
    def __sub__(self, other):
        if len(self.component) != len(other.component):
            raise ValueError("Vector should have the same dimensions")
        return vector(*[a - b for a, b in zip(self.component, other.component)])

    # Handle both scalar multiplication and dot product
    def __mul__(self, other):
        if isinstance(other, (int, float)):  # Scalar multiplication
            return vector(*[a * other for a in self.component])
        elif isinstance(other, vector):  # Dot product
            if len(self.component) != len(other.component):
                raise ValueError("Vector should have the same dimensions")
            return sum(a * b for a, b in zip(self.component, other.component))
        else:
            raise TypeError("Multiplication only supports scalars or dot products")
        #length of the vector 
    def magnitude(self):
        return sum([a**2 for a in self.component])**0.5

    # Enables scalar multiplication from the left (e.g., 5 * v)
    def __rmul__(self, other):
        return self * other
    #normalization
    def normalize (self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot be zero")
        else:
            return vector(*[a/mag for a in self.component])

# Example Usage
v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)

v3 = v1 + v2   
v4 = v3 - v2   
dot_product = v1 * v2  
v5 = v4 * 4    
v6 = 5 * v5    

print(v3)  
print(v4)  
print(dot_product)  
print(v5)  
print(v6)  
print(v1.magnitude())
print(v2.normalize())
