| **Characteristic**      | **Pass by Value**                           | **Pass by Reference**                        | **Pass by Pointer**                          |
|-------------------------|---------------------------------------------|----------------------------------------------|----------------------------------------------|
| **Definition**          | Copies the actual value of an argument into the formal parameter of the function | Copies the reference (address) of an argument into the formal parameter | Passes the address of the argument to the function |
| **Modification**        | Changes made to the parameter inside the function do not affect the original argument | Changes made to the parameter affect the original argument | Changes made to the parameter affect the original argument |
| **Memory Allocation**   | Allocates new memory for the parameter      | Uses the same memory location as the original argument | Uses the same memory location as the original argument |
| **Performance**         | Slower for large data types due to copying  | Faster for large data types as no copying is involved | Faster for large data types as no copying is involved |
| **Syntax**              | `void func(int x)`                          | `void func(int& x)`                          | `void func(int* x)`                          |
| **Use Case**            | Suitable for small data types or when the function should not modify the argument | Suitable when the function needs to modify the argument or for large data types | Suitable when the function needs to modify the argument or for large data types |
| **Example**             | `void func(int x) { x = 10; }`              | `void func(int& x) { x = 10; }`              | `void func(int* x) { *x = 10; }`             |
| **Function Call**       | `int a = 5; func(a); // a remains 5`        | `int a = 5; func(a); // a becomes 10`        | `int a = 5; func(&a); // a becomes 10`       |
