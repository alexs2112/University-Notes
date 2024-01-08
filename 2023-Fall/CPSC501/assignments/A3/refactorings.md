**GitHub Repository**: https://github.com/alexs2112/CPSC501-Serializer
 - Code changes are stored in the git commit page that is hyperlinked to. These commits are entirely refactorings, there is no additional work in each commit that is not refactoring related. The code changes are typically way too large to paste into this document otherwise.

**Move displaying object info from ObjectType into static ObjectHelper class**:
[0997820e8624db66ccf8375e0a74188ba26a87be](https://github.com/alexs2112/CPSC501-Serializer/commit/0997820e8624db66ccf8375e0a74188ba26a87be)
 - Large Classes + Feature Envy -> Extract Classes + Move Methods
 - Large refactoring to clean up the way objects are displayed to the screen
 - Previously, each ObjectType subclass had a bunch of extra methods that were strictly for displaying the object to the screen
 - Now there is an ObjectHelper class. This class has the same methods as before, but they take an `ObjectType` parameter and are now static methods. These static methods take the object in question and determine how it should be displayed to the screen, before calling the necessary methods to do so.
 
 **Break ModifyArray into several subclasses**: [5c2fdc7c5a399afdd46178cc2c99da61b1e9c09f](https://github.com/alexs2112/CPSC501-Serializer/commit/5c2fdc7c5a399afdd46178cc2c99da61b1e9c09f)
  - Switch Statements -> Replace Conditional with Polymorphism
  - Previously the ModifyArray class was very ugly, it took 4 different types of arrays as inputs and 2 different types of screens to handle them. Almost every method in this class had to first check to figure out what array it is working on before doing anything.
  - This turns ModifyArray into an abstract class and has 4 different subclasses that each handle a type of array. ModifyIntArray, ModifyDoubleArray, ModifyBoolArray, and ModifyObjectArray.
  - Now this class is so much cleaner and all work is delegated to the appropriate type of array.

**Extract method to validate object for map**: [f6f2d662fc455cf5e5874c8b1e6d7e0cf08f9c28](https://github.com/alexs2112/CPSC501-Serializer/commit/f6f2d662fc455cf5e5874c8b1e6d7e0cf08f9c28)
 - Duplicated Code -> Extract Method
 - Duplicated code three times when validating if an object assigned to a field is valid to be populated into the serialization hashmap of objects.
 - Simply extracted the method `isValidObject(Object o)` and removed those duplicated code segments

**Extract ObjectMap class**: [ad801973f2b6e3d9f7f7ef3725f35c65cd41c786](https://github.com/alexs2112/CPSC501-Serializer/commit/ad801973f2b6e3d9f7f7ef3725f35c65cd41c786)
 - Large Class -> Extract Class
 - Move all code in `Serializer` that involves setting up the HashMap of objects into a new `ObjectMap` class
 - This new class is instantiated and called in `Serializer` and unit tests

**Extract FieldHelper class from objectMap**: [39a3be35c68da24ef0b379179fcb22613739a39c](https://github.com/alexs2112/CPSC501-Serializer/commit/39a3be35c68da24ef0b379179fcb22613739a39c)
 - Feature Envy -> Move Method
 - The `ObjectMap` class used to contain many methods for handling lists of fields that an object contains.
 - The functionality of these methods was desired in other places and didn't make a whole lot of sense to turn into static methods in `ObjectMap`
 - Create a new `serializer.helpers.FieldHelper` class that contains these methods as static functions to be called in other places of the code

**Extract serializeValue to remove duplicated code**: [47d7682f569cc42f7d8e37bba756333e5a2252c1](https://github.com/alexs2112/CPSC501-Serializer/commit/47d7682f569cc42f7d8e37bba756333e5a2252c1)
 - Duplicated Code -> Extract Method
 - Lots of duplicated code between `serializeField` and `serializeArray` for serializing the values of fields or the values stored in an array
 - Extract out a new `serializeValue` method that uses that duplicated code. This will also need to be used in an eventual `serializeList` method for handling an ArrayList
