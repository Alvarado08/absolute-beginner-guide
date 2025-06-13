| Type | Ordered | Mutable | Unique | Use Cases |
|------|---------|---------|---------|-----------|
| List | Yes | Yes | No | • Storing ordered sequences of items<br>• When you need to modify the collection<br>• When you need to access elements by index<br>• When you need to maintain duplicates |
| Tuple | Yes | No | No | • Storing fixed sequences of items<br>• When you need immutable data<br>• When returning multiple values from a function<br>• When using as dictionary keys |
| Dictionary | Yes (Python 3.7+) | Yes | Keys: Yes<br>Values: No | • Storing key-value pairs<br>• Fast lookups by key<br>• When you need to associate data with unique identifiers<br>• When you need to count occurrences of items |
| Set | No | Yes | Yes | • Storing unique values<br>• Mathematical set operations (union, intersection, etc.)<br>• Removing duplicates from a sequence<br>• Fast membership testing |
