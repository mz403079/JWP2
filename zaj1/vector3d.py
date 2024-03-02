import math

class Vector3D:
    def __init__(self, x,y,z):
        self.__x = x  # Prywatny atrybut
        self.__y = y  # Prywatny atrybut
        self.__z = z  # Prywatny atrybut

    def __str__(self):
         print(f"Vector3D({self.__x}, {self.__y}, {self.__z})")

    def norm(self):
        return math.sqrt(math.pow(self.__x,2)+
        math.pow(self.__y,2)+
        math.pow(self.__z,2))
        
    def __add__(self,other):
        return Vector3D(self.__x + other.__x,
                        self.__y + other.__y,
                        self.__z + other.__z)
        
    def __sub__(self,other):
        return Vector3D(self.__x - other.__x,
                    self.__y - other.__y,
                    self.__z - other.__z)
        
    def __mul__(self,scalar):
        return Vector3D(self.__x * scalar,
                    self.__y * scalar,
                    self.__z * scalar)
        
    def dot(self,vec2):
        return (self.__x * vec2.__x +
                    self.__y * vec2.__y+
                    self.__z * vec2.__z)
        
    def cross(self,vec2):
        return Vector3D(self.__y * vec2.__z - self.__z * vec2.__y,
                    self.__z * vec2.__x - self.__x * vec2.__z,
                    self.__x * vec2.__y - self.__y * vec2.__x)
        
    @staticmethod   
    def are_orthogonal(vec1,vec2):
        if(vec1.dot(vec2)) == 0:
            return True
        else:
            return False
        
vec1 = Vector3D(4,5,6)
vec1.__str__()
print(vec1.norm())
vec2 = Vector3D(1,2,1)
(vec1+vec2).__str__()
(vec1-vec2).__str__()
(vec1*3).__str__()
print(vec1.dot(vec2))
vec1.cross(vec2).__str__()
print(Vector3D.are_orthogonal(vec1,Vector3D(3,2,0)))
print(Vector3D.are_orthogonal(vec1,Vector3D(0,0,0)))