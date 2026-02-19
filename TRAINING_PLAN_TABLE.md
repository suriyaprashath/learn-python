# Python Training Plan for LabVIEW Programmers - Table Format

## Training Schedule Overview

| Category | Day | Hours | Topic | Detailed Items |
|----------|-----|-------|-------|----------------|
| Basic | 1 | 2 | Python Fundamentals - Part 1 | Setup & environment, syntax introduction, data types (int, float, bool, str), operators, indentation vs dataflow |
| Basic | 2 | 2 | Control Flow & Functions Basics | String operations, conditionals (if/elif/else), loops (for, while), break/continue, function basics (def, parameters, return) |
| Basic | 3 | 2 | Data Structures - Lists & Sequences | Lists (dynamic arrays), list methods, list comprehensions, tuples, sets, nested structures |
| Basic | 4 | 2 | Data Structures - Dictionaries | Dictionary fundamentals, dict comprehensions, nested data structures, JSON file operations |
| Intermediate | 5 | 2 | Functions Deep Dive & Type Hints | Function scope, default parameters, *args/**kwargs, type hints & annotations, docstrings, lambda functions |
| Intermediate | 6 | 2 | Modules & Packages | Module basics, imports, creating custom modules, packages & __init__.py, standard library tour (time, datetime, math, pathlib, json) |
| Intermediate | 7 | 2 | File I/O & Error Handling | File operations (read/write), CSV files, context managers (with), error handling (try/except/finally), raising exceptions |
| Intermediate | 8 | 2 | Logging & Decorators | Logging module (levels, handlers, formatters), decorator basics, @property, custom decorators, timing & retry decorators |
| Intermediate-Advanced | 9 | 2 | Object-Oriented Programming - Fundamentals | OOP introduction, classes & objects, __init__, instance/class/static methods, properties, dunder methods (__str__, __repr__, __eq__) |
| Intermediate-Advanced | 10 | 2 | Object-Oriented Programming - Advanced | Inheritance, method overriding, super(), polymorphism, composition vs inheritance, SOLID principles overview |
| Intermediate | 11 | 2 | NumPy for Signal & Data Processing | NumPy arrays, array creation & manipulation, indexing & slicing, element-wise operations, statistical functions, boolean masking |
| Intermediate | 12 | 2 | Pandas & Data Visualization | DataFrames (load, explore, filter), data manipulation (groupby, aggregation), matplotlib visualization (line, scatter, bar, histogram plots) |
| Advanced | 13 | 2 | Hardware Interfacing - PyVISA & Serial | VISA architecture, PyVISA basics (resource manager, write/query), SCPI commands, serial communication (pySerial, baud rate, read/write) |
| Advanced | 14 | 2 | Network Communication - TCP & HTTP | TCP socket communication, client/server basics, HTTP with requests library (GET, POST, REST APIs), authentication |
| Advanced | 15 | 2 | Database Integration with SQLite | Database fundamentals, SQLite operations (CREATE, INSERT, SELECT, UPDATE, DELETE), parameterized queries, pandas integration |
| Advanced | 16 | 2 | Testing & AI-Assisted Programming | Pytest basics (test functions, assertions, fixtures, running tests), AI coding assistants (Claude Code, GitHub Copilot, Cursor), prompt engineering best practices, using AI efficiently for text-based programming |
| UI Development | 17 | 2 | PySide6 Fundamentals | Qt and PySide6 introduction, GUI basics vs LabVIEW front panels, basic widgets (QPushButton, QLabel, QLineEdit, QSpinBox), layouts (QVBoxLayout, QHBoxLayout, QGridLayout), signals and slots (event handling), building simple applications |
| UI Development | 18 | 2 | Data Display & Dynamic Content | Tables (QTableWidget), dynamic page switching (QStackedWidget), image display (QPixmap), basic matplotlib plot embedding, creating reusable widget classes |

---

## Summary Statistics

- **Total Days:** 18
- **Total Teaching Hours:** 36 hours (2 hours per day)
- **Basic Topics:** 4 days (8 hours)
- **Intermediate Topics:** 6 days (12 hours)
- **Advanced Topics:** 4 days (8 hours)
- **Intermediate-Advanced Topics:** 2 days (4 hours)
- **UI Development Topics:** 2 days (4 hours)

---

## Complexity Breakdown

### Basic (Days 1-4)
Foundational Python syntax, data types, control structures, and core data structures for newcomers to text-based programming.

### Intermediate (Days 5-8, 11-12)
Functions, code organization, file operations, error handling, logging, data processing with NumPy/Pandas.

### Intermediate-Advanced (Days 9-10)
Object-oriented programming with classes, inheritance, and composition for building complex systems.

### Advanced (Days 13-16)
Hardware interfacing, network communication, database integration, testing, and complete system integration.

### UI Development (Days 17-18)
Desktop GUI development with PySide6 - widgets, layouts, event handling, data display, and dynamic content switching.

---

## CSV Format for Excel Import

```csv
Category,Day,Hours,Topic,Detailed Items
Basic,1,2,Python Fundamentals - Part 1,"Setup & environment, syntax introduction, data types (int, float, bool, str), operators, indentation vs dataflow"
Basic,2,2,Control Flow & Functions Basics,"String operations, conditionals (if/elif/else), loops (for, while), break/continue, function basics (def, parameters, return)"
Basic,3,2,Data Structures - Lists & Sequences,"Lists (dynamic arrays), list methods, list comprehensions, tuples, sets, nested structures"
Basic,4,2,Data Structures - Dictionaries,"Dictionary fundamentals, dict comprehensions, nested data structures, JSON file operations"
Intermediate,5,2,Functions Deep Dive & Type Hints,"Function scope, default parameters, *args/**kwargs, type hints & annotations, docstrings, lambda functions"
Intermediate,6,2,Modules & Packages,"Module basics, imports, creating custom modules, packages & __init__.py, standard library tour (time, datetime, math, pathlib, json)"
Intermediate,7,2,File I/O & Error Handling,"File operations (read/write), CSV files, context managers (with), error handling (try/except/finally), raising exceptions"
Intermediate,8,2,Logging & Decorators,"Logging module (levels, handlers, formatters), decorator basics, @property, custom decorators, timing & retry decorators"
Intermediate-Advanced,9,2,Object-Oriented Programming - Fundamentals,"OOP introduction, classes & objects, __init__, instance/class/static methods, properties, dunder methods (__str__, __repr__, __eq__)"
Intermediate-Advanced,10,2,Object-Oriented Programming - Advanced,"Inheritance, method overriding, super(), polymorphism, composition vs inheritance, SOLID principles overview"
Intermediate,11,2,NumPy for Signal & Data Processing,"NumPy arrays, array creation & manipulation, indexing & slicing, element-wise operations, statistical functions, boolean masking"
Intermediate,12,2,Pandas & Data Visualization,"DataFrames (load, explore, filter), data manipulation (groupby, aggregation), matplotlib visualization (line, scatter, bar, histogram plots)"
Advanced,13,2,Hardware Interfacing - PyVISA & Serial,"VISA architecture, PyVISA basics (resource manager, write/query), SCPI commands, serial communication (pySerial, baud rate, read/write)"
Advanced,14,2,Network Communication - TCP & HTTP,"TCP socket communication, client/server basics, HTTP with requests library (GET, POST, REST APIs), authentication"
Advanced,15,2,Database Integration with SQLite,"Database fundamentals, SQLite operations (CREATE, INSERT, SELECT, UPDATE, DELETE), parameterized queries, pandas integration"
Advanced,16,2,Testing & AI-Assisted Programming,"Pytest basics (test functions, assertions, fixtures, running tests), AI coding assistants (Claude Code, GitHub Copilot, Cursor), prompt engineering best practices, using AI efficiently for text-based programming"
UI Development,17,2,PySide6 Fundamentals,"Qt and PySide6 introduction, GUI basics vs LabVIEW front panels, basic widgets (QPushButton, QLabel, QLineEdit, QSpinBox), layouts (QVBoxLayout, QHBoxLayout, QGridLayout), signals and slots (event handling), building simple applications"
UI Development,18,2,Data Display & Dynamic Content,"Tables (QTableWidget), dynamic page switching (QStackedWidget), image display (QPixmap), basic matplotlib plot embedding, creating reusable widget classes"
```
