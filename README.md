# Preplacement Education Program (PEP)

Study material for various topics covered in the PEP sessions.

## class topics

1. python recap
2. fizzbuzz challenge
3. types of operators
4. type checking
5. what types can dict of python hold? They can hold any type as keys and values, including:
   - Keys: strings, numbers, tuples (if they are immutable)
   - Values: any data type including lists, other dictionaries, custom objects, etc.
6. default dictionary
7. sets in python (how they work internally, operations, use cases)
8. functions (single largest number in a list)
9. function multiple return values (tuple unpacking, edge cases)
10. decorators (function as first class citizens, nested functions, closures)
11. generators (yield keyword, memory efficiency, use cases)
12. oop concepts (classes, objects, inheritance, polymorphism, encapsulation)
    - static methods and class methods
    - properties and getters/setters
    - ```
      Create a class Student that demonstrates encapsulation using private variables and the @property decorator. Requirements: The class should have the following private instance variables: __name __marks Implement: A getter method using @property to return the student's marks. A setter method using @marks.setter to update the marks, but: Marks should be between 0 and 100 only. If invalid marks are given, print: "Invalid marks" Create an object of the class and: Print the student's marks using the getter. Update the marks using the setter. Try setting invalid marks and observe the result.
      ```
13. dutch national flag problem
14. json module (serialization and deserialization) dump, load, dumps, loads
15. file handling (read, write, append modes, context managers)
16. django basics (project setup, apps, models, views, templates)
17. django static files handling
18. django template rendering
19. django inherited templates
20. problem:

```

Create a Django application that displays a student's report card using Django Template Language. This exercise will help you practice variables, for loops, and conditional statements in templates. Start by creating a view function in views.py with sample data including school name, student information (name, class, roll number, attendance), and a list of subjects with marks. Your main task is to create a report_card.html template that displays this information in a structured format. First, display the basic information: school name as the main heading, followed by student name, class, roll number, and attendance percentage. Next, implement attendance status logic using if-elif-else statements - if attendance is 90% or above show "Excellent Attendance" in green, between 75-89% show "Good Attendance" in blue, and below 75% show "Poor Attendance - Warning!" in red. Create a table displaying all subjects with serial numbers (using forloop.counter), subject names, marks obtained, and calculated grades. The grade calculation should use if-elif-else logic: 90+ for A+, 80-89 for A, 70-79 for B, 60-69 for C, 40-59 for D, and below 40 for F. Calculate and display total marks and percentage (hint: it's better to do this calculation in the view). Based on the percentage, show the overall division: 75%+ for First Division, 60-74% for Second Division, 40-59% for Third Division, and below 40% for Failed. Add a teacher's remarks section with appropriate messages based on percentage ranges. For bonus points, create a "Strengths" section listing subjects with 85+ marks and an "Areas for Improvement" section for subjects below 70 marks. Remember common mistakes to avoid: forgetting to close template tags, using double curly braces for logic instead of curly-percent syntax, and misspelling variable names. The grading breakdown is: basic info display (10 points), attendance status (10 points), subject table (15 points), grade calculation (20 points), totals display (10 points), overall result (10 points), teacher's remarks (10 points), and bonus sections (10 points combined), with 5 points for code quality. Test your code frequently and make sure all template tags are properly closed.
```

21. django forms (form handling, validation, form classes)
22. django authentication (user registration, login, logout)
23. django session management (storing data across requests, session variables)
24. django object-relational mapping (ORM) (models, querying, relationships)
25. get or filter in django ORM (difference between get and filter, use cases, handling exceptions) (return type) [get_or_create, update_or_create, get_object_or_404]
26. middlewares in django (request and response processing, custom middlewares)
