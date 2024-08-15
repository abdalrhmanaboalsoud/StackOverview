# Loops

## in JS

### `map(`

- **Purpose**: Transforms each element in an array by applying a provided function and returns a new array with the transformed elements.
- **Syntax**: `array.map(callback(element, index, array)`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const doubled = numbers.map(num => num * 2);
  console.log(doubled); // Output: [2, 4, 6, 8]
  ```

### `reduce(`

- **Purpose**: Reduces an array to a single value by executing a provided function for each element (from left to right), with an accumulator to store the intermediate results.
- **Syntax**: `array.reduce(callback(accumulator, currentValue, index, array), initialValue`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const sum = numbers.reduce((acc, num) => acc + num, 0);
  console.log(sum); // Output: 10
  ```

### `filter(`

- **Purpose**: Creates a new array with all elements that pass the test implemented by the provided function.
- **Syntax**: `array.filter(callback(element, index, array)`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const evenNumbers = numbers.filter(num => num % 2 === 0);
  console.log(evenNumbers); // Output: [2, 4]
  ```

### `forEach(`

- **Purpose**: Executes a provided function once for each array element.
- **Syntax**: `array.forEach(callback(element, index, array)`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  numbers.forEach(num => console.log(num));
  // Output: 1, 2, 3, 4 (each on a new line)
  ```

### `find(`

- **Purpose**: Returns the first element in the array that satisfies the provided testing function. If no values satisfy the testing function, `undefined` is returned.
- **Syntax**: `array.find(callback(element, index, array)`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const found = numbers.find(num => num > 2);
  console.log(found); // Output: 3
  ```

### `some(`

- **Purpose**: Tests whether at least one element in the array passes the test implemented by the provided function. Returns a boolean value.
- **Syntax**: `array.some(callback(element, index, array)`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const hasEven = numbers.some(num => num % 2 === 0);
  console.log(hasEven); // Output: true
  ```

### `every(`

- **Purpose**: Tests whether all elements in the array pass the test implemented by the provided function. Returns a boolean value.
- **Syntax**: `array.every(callback(element, index, array)`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const allEven = numbers.every(num => num % 2 === 0);
  console.log(allEven); // Output: false
  ```

### `sort(`

- **Purpose**: Sorts the elements of an array in place and returns the sorted array. The default sort order is according to string Unicode code points.
- **Syntax**: `array.sort([compareFunction]`
- **Example**:

  ```javascrip
  const numbers = [4, 2, 3, 1];
  numbers.sort();
  console.log(numbers); // Output: [1, 2, 3, 4]
  ```

### `slice(`

- **Purpose**: Returns a shallow copy of a portion of an array into a new array object selected from `start` to `end` (end not included).
- **Syntax**: `array.slice([start[, end]]`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const sliced = numbers.slice(1, 3);
  console.log(sliced); // Output: [2, 3]
  ```

### `concat(`
- **Purpose**: Merges two or more arrays. This method does not change the existing arrays but returns a new array.
- **Syntax**: `array.concat(array2, array3, ..., arrayN`
- **Example**:

  ```javascrip
  const numbers1 = [1, 2];
  const numbers2 = [3, 4];
  const combined = numbers1.concat(numbers2);
  console.log(combined); // Output: [1, 2, 3, 4]
  ```

### `includes(`

- **Purpose**: Determines whether an array includes a certain value among its entries, returning `true` or `false` as appropriate.
- **Syntax**: `array.includes(valueToFind, [fromIndex]`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const hasThree = numbers.includes(3);
  console.log(hasThree); // Output: true
  ```

### `indexOf(`

- **Purpose**: Returns the first index at which a given element can be found in the array, or `-1` if it is not present.
- **Syntax**: `array.indexOf(searchElement, [fromIndex]`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const index = numbers.indexOf(3);
  console.log(index); // Output: 2
  ```

### `join()

- **Purpose**: Joins all elements of an array into a string and returns this string.
- **Syntax**: `array.join([separator]`
- **Example**:

  ```javascript
  const numbers = [1, 2, 3, 4];
  const joined = numbers.join('-');
  console.log(joined); // Output: '1-2-3-4'
  ```

### `flat()`

- **Purpose**: Creates a new array with all sub-array elements concatenated into it recursively up to the specified depth.
- **Syntax**: `array.flat([depth]`
- **Example**:

  ```javascript
  const numbers = [1, [2, [3, [4]]]];
  const flat = numbers.flat(2);
  console.log(flat); // Output: [1, 2, 3, [4]]
  ```

### `flatMap()`

- **Purpose**: First maps each element using a mapping function, then flattens the result into a new array. It is identical to a `map()` followed by a `flat()` of depth 1.
- **Syntax**: `array.flatMap(callback(element, index, array)`
- **Example**:

  ```javascrip
  const numbers = [1, 2, 3, 4];
  const flatMapped = numbers.flatMap(num => [num, num * 2]);
  console.log(flatMapped); // Output: [1, 2, 2, 4, 3, 6, 4, 8]
  ```
