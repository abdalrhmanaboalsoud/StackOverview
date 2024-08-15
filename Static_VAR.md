| **Characteristic**      | **Normal (Automatic) Variables**             | **Static Variables**                          |
|-------------------------|----------------------------------------------|-----------------------------------------------|
| **Lifetime**            | - Created when function/block is entered     | - Created when program starts                 |
|                         | - Destroyed when function/block exits        | - Destroyed when program ends                 |
|                         |                                              | - Retain value between function calls         |
| **Scope**               | - Limited to function/block                  | - Local scope within function or block        |
|                         |                                              | - File scope if declared at file level        |
|                         |                                              | - Shared among all instances of class if declared in class |
| **Memory Allocation**   | - Stack                                      | - Static memory segment                       |
| **Default Value**       | - Undefined (garbage value)                  | - Zero (0) if not explicitly initialized      |
| **Usage**               | - Local state within function/block          | - Persistent state across function calls      |
|                         |                                              | - Shared data among class instances           |
|                         |                                              | - Encapsulation within file scope             |
