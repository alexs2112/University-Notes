**GitHub Repository**: https://github.com/alexs2112/CPSC501-ObjectInspector

**Extract Methods in Inspector**: [9fba2ed41c9f6aac5e4ea0bafbf444e93edc393d](https://github.com/alexs2112/CPSC501-ObjectInspector/commit/9fba2ed41c9f6aac5e4ea0bafbf444e93edc393d)
 - New methods to `getDeclaringClass` and `getHeader` (superclass, interfaces) instead of doing everything in the `inspect` method.

**Extract addLine method to handle string formatting**: [c8342b990cf55efeaf26772d700c81f9fc286a4b](https://github.com/alexs2112/CPSC501-ObjectInspector/commit/c8342b990cf55efeaf26772d700c81f9fc286a4b)
 - Previously strings would be manually formatted by prepending a bunch of whitespace before certain lines to keep things organized
 - This adds a method to automatically add whitespace based on a parameter of `tab`

**Refactor printing into InspectorOutput and helpers**: [63a36ba8c7b3402baebc9bd4ee0609a3851f9c89](https://github.com/alexs2112/CPSC501-ObjectInspector/commit/63a36ba8c7b3402baebc9bd4ee0609a3851f9c89)
 - Big refactoring, previously would store all output lines of text into an ArrayList in Inspector, and then iterating over these strings and print them to the console
 - Unit testing needed to parse this output and handle string formatting with whitespace
 - Created new `InspectorOutput`, `InspectorConstructor`, `InspectorMethod` classes to handle storing the inspector output. This is much cleaner and makes the tests much nicer as well.

**Extract method for parsing non-array fields**: [881a4dc523a935f12310184130e59bd46bc4be6d](https://github.com/alexs2112/CPSC501-ObjectInspector/commit/881a4dc523a935f12310184130e59bd46bc4be6d)
 - Small refactoring
 - The commit directly before this introduced a method for parsing array fields while leaving the code for non-array fields as is. This results in duplicated code in two places in the inspector
 - Move the non-array field code to a new method that is similar to parsing array fields.

**Remove FieldClass in favour of BlankClass**: [d2aaed4d6b3af958b5368da890db21e1939fbd6f](https://github.com/alexs2112/CPSC501-ObjectInspector/commit/d2aaed4d6b3af958b5368da890db21e1939fbd6f)
 - While I was writing more unit tests I realized that FieldClass and BlankClass were the same thing
 - Remove FieldClass and change all references to it to BlankClass
