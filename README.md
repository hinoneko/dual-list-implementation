# Dual List Implementation

## Project Description

This project demonstrates two implementations of a typed character list in Python:
1. **Doubly Linked List** - Custom pointer-based implementation
2. **Array List** - Implementation using Python's built-in lists

Both implementations provide identical functionality for storing and manipulating single-character elements while showcasing different architectural approaches.

## Variant Information
**Group list number is 21**

Remainder = 21 mod 4 = 1
- **Initial implementation**: Doubly Linked List
- **Refactored implementation**: Array List

## Features

The list class implements the following operations:
- `length()` - Get current list size
- `append(element)` - Add element to end
- `insert(element, index)` - Insert at position
- `delete(index)` - Remove by position
- `deleteAll(element)` - Remove all occurrences
- `get(index)` - Access by position
- `clone()` - Create a deep copy
- `reverse()` - Reverse list in-place
- `findFirst(element)` - Find first occurrence
- `findLast(element)` - Find last occurrence
- `clear()` - Remove all elements
- `extend(list)` - Merge another list

## Installation & Usage

### Prerequisites
- Python 3.10+
- Git

### Clone the repository

First, you need to download the project to your local machine. You can do this using Git:

```bash
git clone https://github.com/hinoneko/dual-list-implementation.git
cd dual-list-implementation
```
### Run the project

Once you're inside the project folder, run the main script:

```bash 
python main.py
```
### Running Tests

To run the unit tests:

```sh
pytest
```

## Failed CI commit:

View test failure examples: [first](https://github.com/hinoneko/dual-list-implementation/commit/c8887f8e35df188802e55ceaa6a7b07a75246f72) and [second](https://github.com/hinoneko/dual-list-implementation/commit/093d76a66b4069c4b5eea56e5a575836e20dc4f8).

## Conclusions

Unit testing proved to be a crucial part of development, significantly improving code quality and efficiency. The tests helped identify edge cases early, ensuring the correctness of both the doubly linked list and array-based implementations. By catching errors during method development, they minimized debugging time and provided immediate feedback.

Additionally, unit tests served as reliable documentation, clarifying expected behavior for each function. They also enabled safe refactoring, allowing seamless transitions between different implementations without introducing regressions. The integration of CI further automated verification, ensuring stability after every change.

While writing tests required initial effort, the long-term benefits far outweighed the investment. Testing was not just a requirement—it became a fundamental tool that enhanced reliability, accelerated development, and maintained code integrity throughout the project.