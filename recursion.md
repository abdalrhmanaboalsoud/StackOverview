| **Aspect**              | **Description**                                                                 |
|-------------------------|---------------------------------------------------------------------------------|
| **How Recursion Works** | Recursion involves a function calling itself to solve a smaller instance of the same problem. This continues until a base condition is met, which stops the recursion. |
| **When It Returns**     | The function returns when the base condition is satisfied. This prevents infinite recursion and starts the process of unwinding the call stack. |
| **When It Prints**      | The function prints when a print statement is executed within it. This can happen before, during, or after the recursive call, depending on where the print statement is placed. |
| **Recursive Call**      | The function calls itself with a modified argument that moves it closer to the base condition. This is the essence of recursion. |
| **Common Element**      | All recursive functions must have a base condition. This is a condition that stops the recursion and prevents infinite loops. |
| **Tracing Recursion**   | To trace recursion, follow each function call and return. This is often visualized using a call stack, where each call adds a new frame to the stack, and each return removes a frame. |
| **Base Condition**      | A specific condition that, when met, stops the recursion. Without a base condition, the function would call itself indefinitely, leading to a stack overflow. |
| **Call Stack**          | A stack data structure that stores information about active subroutines or function calls. Each recursive call adds a new frame to the stack. |
| **Memory Usage**        | Each recursive call uses stack memory. If the recursion is too deep, it can lead to a stack overflow. It's important to ensure that the recursion depth is manageable. |
| **Performance**         | Recursive functions can be less efficient than iterative solutions due to the overhead of multiple function calls. Tail recursion can optimize this by reusing the same stack frame. |
| **Tail Recursion**      | A special case of recursion where the recursive call is the last operation in the function. Some compilers can optimize tail-recursive functions to improve performance. |
| **Example**             | A simple example of a recursive function in C++ that calculates the factorial of a number: `int factorial(int n) { if (n <= 1) return 1; return n * factorial(n - 1); }` |
| **Tracing Example**     | To trace the example, follow each call and return: `factorial(5)` calls `factorial(4)`, `factorial(4)` calls `factorial(3)`, `factorial(3)` calls `factorial(2)`, `factorial(2)` calls `factorial(1)`, `factorial(1)` returns 1 (base condition met), `factorial(2)` returns 2 * 1 = 2, `factorial(3)` returns 3 * 2 = 6, `factorial(4)` returns 4 * 6 = 24, `factorial(5)` returns 5 * 24 = 120. |
| **Debugging Tips**      | Use print statements or a debugger to trace the flow of recursive calls. This helps in understanding how the function progresses and where it might be going wrong. |
| **Common Pitfalls**     | Missing base condition, infinite recursion, and excessive memory usage are common issues in recursive functions. Always ensure there is a clear base condition and be mindful of the recursion depth. |
| **Head Recursion**      | The recursive call is made before any other operations. Example: `int headRecursion(int n) { if (n == 0) return; headRecursion(n - 1); cout << n << " "; }` |
| **Tail Recursion**      | The recursive call is the last operation in the function. Example: `int tailRecursion(int n, int a = 1) { if (n == 0) return a; return tailRecursion(n - 1, n * a); }` |
| **Tree Recursion**      | The function makes multiple recursive calls. Example: `int treeRecursion(int n) { if (n == 0 || n == 1) return n; return treeRecursion(n - 1) + treeRecursion(n - 2); }` |
| **Nested Recursion**    | The function's recursive call is passed as an argument to another recursive call. Example: `int nestedRecursion(int n) { if (n > 100) return n - 10; return nestedRecursion(nestedRecursion(n + 11)); }` |

```
#include <iostream>
using namespace std;

int factorial(int n) {
    // Base condition
    if (n <= 1) {
        return 1;
    }
    // Recursive call
    return n * factorial(n - 1);
}

int main() {
    int number = 5;
    cout << "Factorial of " << number << " is " << factorial(number) << endl;
    return 0;
}
```
