**GitHub Repository**: https://github.com/alexs2112/CPSC501-Serializer

**Move displaying object info from ObjectType into static ObjectHelper class**:
[0997820e8624db66ccf8375e0a74188ba26a87be](https://github.com/alexs2112/CPSC501-Serializer/commit/0997820e8624db66ccf8375e0a74188ba26a87be)
 - Large refactoring to clean up the way objects are displayed to the screen
 - Previously, each ObjectType subclass had a bunch of extra methods that were strictly for displaying the object to the screen
 - Now there is an ObjectHelper class. This class has the same methods as before, but they take an `ObjectType` parameter and are now static methods. These static methods take the object in question and determine how it should be displayed to the screen, before calling the necessary methods to do so.
 **Break ModifyArray into several subclasses**: [5c2fdc7c5a399afdd46178cc2c99da61b1e9c09f](https://github.com/alexs2112/CPSC501-Serializer/commit/5c2fdc7c5a399afdd46178cc2c99da61b1e9c09f)
  - Previously the ModifyArray class was very ugly, it took 4 different types of arrays as inputs and 2 different types of screens to handle them. Almost every method in this class had to first check to figure out what array it is working on before doing anything.
  - This turns ModifyArray into an abstract class and has 4 different subclasses that each handle a type of array. ModifyIntArray, ModifyDoubleArray, ModifyBoolArray, and ModifyObjectArray.
  - Now this class is so much cleaner and all work is delegated to the appropriate type of array.
