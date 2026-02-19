# Python Training Plan for LabVIEW Programmers

## Context

This training plan is designed for a team that primarily uses LabVIEW for instrumentation and test automation. The team needs to learn Python to expand their capabilities, particularly for:
- Hardware control and instrument communication (PyVISA, serial, TCP)
- Data acquisition and processing
- Test automation and result analysis
- Modern software development practices
- Database integration for test data management
- HTTP/REST API integration

The team already understands programming fundamentals (variables, loops, conditionals, functions) from LabVIEW but needs to transition from **graphical/dataflow-based programming to text-based Python**. This is a significant cognitive shift that requires adequate time and practice. This plan balances comprehensive coverage with realistic pacing.

**Key Constraints:**
- Maximum 2 hours per day for teaching
- Assignments and evaluations are outside the 2-hour teaching window
- Extended duration to accommodate the graphical→text paradigm shift

**Goals:**
- Enable team to use Python effectively in their daily work
- Cover all fundamentals and essential topics
- Include hardware interfacing, networking, and database capabilities
- Provide practical, hands-on experience with instrumentation examples
- Build confidence in text-based programming

---

## Training Overview

**Duration:** 18 days (36 hours total teaching time)
**Daily Structure:** Max 2 hours instruction + assignments for practice
**Pace:** Measured but steady - accounts for graphical→text transition
**Focus:** Practical application to instrumentation, data analysis, hardware control, data management, and GUI development

---

## Day-by-Day Breakdown

### Day 1: Python Fundamentals - Part 1 (2 hours)
**Theme:** "From Wires to Text - Starting Your Python Journey"

**Session Breakdown:**
- **Setup & Environment (25 min)**
  - Python installation verification, VS Code setup
  - Jupyter notebooks (compare to LabVIEW's interactive front panel)
  - Virtual environments - why they matter
  - **Materials:** `01-setup/01-python.ipynb`, `01-setup/03-jupyter-notebook.ipynb`, `01-setup/04-virtual-environments.ipynb`

- **Syntax Introduction (30 min)**
  - Print statements, comments
  - Indentation (Python's way of showing structure - no wires!)
  - Variables and assignment (no wiring needed)
  - Dynamic typing vs LabVIEW's strong typing
  - **Materials:** `02-syntax/01-syntax.ipynb`, `02-syntax/02-comments.ipynb`
  - **Key Mindset Shift:** In LabVIEW, data flows through wires. In Python, data flows through time (sequential execution)

- **Data Types (40 min)**
  - Basic types: int, float, bool, str (compare to LabVIEW DBL, I32, Boolean, String)
  - Type checking with type()
  - Type casting and conversion
  - **Materials:** `03-variables/01-data-types.ipynb`, `03-variables/02-type-casting.ipynb`

- **Operators (25 min)**
  - Arithmetic, comparison, logical operators
  - Operator precedence
  - **Materials:** `05-operators/01-operators.ipynb`
  - **Note:** Quick review since concepts are familiar from LabVIEW

**Key Focus:** Get comfortable with text-based programming, understand sequential execution
**Assignments:**
- Exercise 1: Variable manipulation (temperature conversions)
- Exercise 2: Simple calculator with different data types
- Exercise 3: Type casting practice
- Reading: Review syntax and operators

---

### Day 2: Control Flow & Functions Basics (2 hours)
**Theme:** "Sequential Logic - Control Structures in Text"

**Session Breakdown:**
- **String Operations (25 min)**
  - String indexing and slicing
  - F-strings for formatted output (critical for logging)
  - Common string methods
  - **Materials:** `04-strings/02-indexing-and-slicing.ipynb`, `04-strings/04-f-strings.ipynb`
  - **Use Case:** Format measurement outputs, log messages

- **Conditionals (35 min)**
  - If/elif/else (compare to LabVIEW Case Structure)
  - Nested conditionals
  - Ternary operator
  - **Materials:** `06-control-flow-and-loops/01-conditionals.ipynb`
  - **Live Demo:** Convert LabVIEW case structure to Python if/elif/else

- **Loops (40 min)**
  - For loops with range() (compare to LabVIEW For Loop)
  - While loops (compare to LabVIEW While Loop)
  - Break/continue (compare to LabVIEW Stop/Continue)
  - Nested loops
  - **Materials:** `06-control-flow-and-loops/02-loops.ipynb`
  - **Focus:** Syntax translation, not concept explanation

- **Functions Introduction (20 min)**
  - Why functions? (same as LabVIEW SubVIs)
  - Defining functions with def
  - Parameters and return values
  - Calling functions
  - **Materials:** `07-functions/01-intro.ipynb`

**Key Focus:** Master control structures and basic function usage
**Assignments:**
- Exercise 1: Temperature threshold alarm with multiple conditions
- Exercise 2: Process measurement array using loops
- Exercise 3: Write function to calculate statistics (mean, min, max)
- Exercise 4: Combine conditionals, loops, and functions

---

### Day 3: Data Structures - Part 1 (2 hours)
**Theme:** "Beyond Arrays - Python's Flexible Collections"

**Session Breakdown:**
- **Lists - Python's Dynamic Arrays (60 min)**
  - Creating lists, indexing, slicing
  - List methods: append, insert, remove, pop, sort, reverse
  - Nested lists (2D arrays)
  - Iterating through lists
  - **List comprehensions** - powerful one-liners (no LabVIEW equivalent!)
  - **Materials:** `08-lists/01-basics.ipynb`, `08-lists/02-comprehensions.ipynb`
  - **Use Cases:** Store measurement readings, device IDs, test results
  - **Demo:** Parse sensor readings, filter values above threshold using comprehension

- **Tuples (30 min)**
  - Immutable sequences
  - When to use: return multiple values, fixed configurations
  - Tuple unpacking
  - **Materials:** `09-tuples/01-basics.ipynb`
  - **Use Case:** Return (status, value, timestamp) from measurement function

- **Sets (Brief Overview) (15 min)**
  - Unique elements, membership testing
  - Basic set operations
  - **Materials:** `10-sets/01-basics.ipynb`
  - **Use Case:** Track unique device IDs, check for duplicates

- **Practice Integration (15 min)**
  - Work with multiple data structures
  - Convert between types

**Key Focus:** Master lists (most commonly used) and understand other sequence types
**Assignments:**
- Exercise 1: Store and process voltage measurements in lists
- Exercise 2: Use list comprehensions to filter test results
- Exercise 3: Function that returns multiple values using tuples
- Exercise 4: Use sets to find unique device IDs from test data

---

### Day 4: Data Structures - Part 2 (2 hours)
**Theme:** "Dictionaries - Your Configuration Powerhouse"

**Session Breakdown:**
- **Dictionaries Fundamentals (50 min)**
  - Creating dictionaries (think: LabVIEW cluster with named fields)
  - Accessing values by key
  - Adding/updating entries
  - Dictionary methods: keys(), values(), items(), get()
  - Iterating through dictionaries
  - **Materials:** `11-dictionaries/01-basics.ipynb`, `11-dictionaries/03-use-cases.ipynb`
  - **Use Cases:** Device configurations, test parameters, instrument settings
  - **Demo:** Store/retrieve instrument config (VISA address, baud rate, timeout, command set)

- **Dictionary Comprehensions (20 min)**
  - Create dictionaries with comprehensions
  - Transform data structures
  - **Materials:** `11-dictionaries/02-comprehensions.ipynb`

- **Nested Data Structures (30 min)**
  - List of dictionaries (test results table)
  - Dictionary of lists (grouped data)
  - Real-world example structure:
  ```python
  test_results = [
      {"id": "DAQ-001", "voltage": 3.3, "current": 0.15, "temp": 25.3, "status": "PASS"},
      {"id": "DAQ-002", "voltage": 3.28, "current": 0.16, "temp": 26.1, "status": "PASS"},
  ]
  ```

- **Working with JSON (20 min)**
  - Reading and writing JSON files (common for configs)
  - json module basics
  - Use case: Save/load instrument configurations

**Key Focus:** Master dictionaries for configuration management
**Assignments:**
- Exercise 1: Create instrument configuration dictionary
- Exercise 2: Build test result data structure (list of dicts) for 10+ devices
- Exercise 3: Write function to filter failed tests using dict comprehension
- Exercise 4: Save and load configuration from JSON file
- Exercise 5: Build device inventory system

---

### Day 5: Functions Deep Dive & Type Hints (2 hours)
**Theme:** "Building Reusable, Well-Documented Code"

**Session Breakdown:**
- **Advanced Function Concepts (45 min)**
  - Function scope (local, global, nonlocal)
  - Default parameters and keyword arguments
  - *args and **kwargs (variable arguments)
  - Return multiple values
  - **Materials:** `07-functions/02-scope.ipynb`
  - **Use Cases:** Flexible instrument drivers, configurable test functions
  - **Demo:** Measurement function with flexible parameters

- **Type Hints & Annotations (35 min)**
  - Why type hints? (LabVIEW users appreciate strong typing!)
  - Basic type hints: int, float, str, bool
  - List, Dict, Tuple type hints
  - Optional types
  - Return type annotations
  - IDE benefits (autocomplete, error detection)
  - **Materials:** `21-typing/` (if exists in repo)
  - **Example:**
  ```python
  def set_voltage(channel: int, voltage: float, timeout: float = 5.0) -> bool:
      """Set voltage on specified channel."""
      # Implementation
      return True

  def measure_current() -> tuple[float, str]:
      """Measure current, return (value, unit)."""
      return (0.15, "A")
  ```

- **Docstrings - Documenting Your Code (25 min)**
  - Why documentation matters
  - Docstring conventions (Google style, NumPy style)
  - Writing clear function documentation
  - **Materials:** `07-functions/03-docstrings.ipynb`
  - **Example:**
  ```python
  def calculate_power(voltage: float, current: float) -> float:
      """
      Calculate electrical power.

      Args:
          voltage: Voltage in volts
          current: Current in amperes

      Returns:
          Power in watts
      """
      return voltage * current
  ```

- **Lambda Functions (15 min - brief)**
  - Quick anonymous functions
  - When to use (sorting, filtering)
  - **Materials:** `07-functions/04-lambda-map-filter-reduce.ipynb` (lambda section only)

**Key Focus:** Write professional, type-hinted, documented functions
**Assignments:**
- Exercise 1: Add type hints to previous exercise functions
- Exercise 2: Write measurement processing functions with full documentation
- Exercise 3: Create configurable instrument driver function with defaults
- Exercise 4: Use lambda for sorting test results

---

### Day 6: Modules & Packages (2 hours)
**Theme:** "Organizing Code for Large Projects"

**Session Breakdown:**
- **Module Basics (40 min)**
  - What are modules? (organizing code into files)
  - Importing modules: import, from...import, as alias
  - Creating custom modules
  - `__name__ == "__main__"` pattern
  - Module search path
  - **Materials:** `12-modules/01-module-basics.ipynb`, `12-modules/02-imports.ipynb`
  - **Use Cases:** Separate instrument drivers, utilities, calculations

- **Packages (35 min)**
  - What are packages? (directories with `__init__.py`)
  - Creating package structure
  - Relative vs absolute imports
  - **Materials:** `12-modules/03-packages.ipynb`
  - **Demo:** Create test automation package structure:
  ```
  test_automation/
    __init__.py
    instruments.py      # Instrument drivers
    data_logger.py      # File I/O utilities
    analysis.py         # Data processing
    config.py           # Configuration constants
  ```

- **Standard Library Tour (30 min)**
  - Important modules for instrumentation:
    - `time`, `datetime` - timing and timestamps
    - `math` - mathematical functions
    - `random` - test data generation
    - `pathlib` - modern path handling
    - `json` - configuration files
    - `collections` - specialized data structures
  - Quick examples of each

- **Best Practices (15 min)**
  - Module naming conventions
  - Avoiding circular imports
  - When to split code into modules

**Key Focus:** Organize code into maintainable module structure
**Assignments:**
- Exercise 1: Create module for common measurement calculations
- Exercise 2: Build package structure for instrument drivers
- Exercise 3: Use standard library modules (time, math, json)
- Exercise 4: Refactor previous exercises into organized modules

---

### Day 7: File I/O & Error Handling (2 hours)
**Theme:** "Robust Data Logging and Error Management"

**Session Breakdown:**
- **File Handling Basics (40 min)**
  - Opening files: open(), modes (r, w, a, r+)
  - Reading: read(), readline(), readlines()
  - Writing: write(), writelines()
  - Context managers (with statement) - automatic cleanup
  - Working with paths (pathlib is recommended!)
  - **Materials:** `16-files/01-basics.ipynb`, `16-files/02-os-and-shutil.ipynb`
  - **Use Cases:** Log test results, read calibration data
  - **Demo:** Write measurement data with timestamps, read back and verify

- **CSV File Operations (20 min)**
  - Reading CSV files (csv module)
  - Writing CSV files
  - DictReader and DictWriter
  - **Use Case:** Log test results to CSV (most common format!)

- **Error Handling (50 min)**
  - Why error handling matters in test automation
  - try/except blocks
  - Common exceptions: FileNotFoundError, ValueError, TypeError, IOError
  - Catching specific vs general exceptions
  - finally clause - cleanup resources
  - else clause
  - Raising exceptions
  - Creating custom exceptions (brief)
  - **Materials:** `14-error-handling/01-error-handling-basics.ipynb`, `14-error-handling/02-defensive-programming.ipynb`
  - **Use Cases:** Handle instrument failures, invalid readings, file access issues
  - **Demo:** Retry logic for unreliable connections

- **Best Practices (10 min)**
  - When to catch exceptions vs let them propagate
  - Logging errors (preview of next section)
  - Defensive programming mindset

**Key Focus:** Robust file operations and error handling
**Assignments:**
- Exercise 1: Write test data logger (CSV with timestamps)
- Exercise 2: Read configuration from file with error handling
- Exercise 3: Build robust file reader that handles missing files
- Exercise 4: Add retry logic to measurement function

---

### Day 8: Logging & Decorators (2 hours)
**Theme:** "Professional Debugging and Code Enhancement"

**Session Breakdown:**
- **Logging for Instrumentation (50 min)**
  - Why logging beats print statements
  - logging module basics
  - Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Configuring loggers
  - Formatting log messages
  - Multiple handlers (console + file)
  - Log rotation for long-running tests
  - **Materials:** `19-development-tools/01-logging.ipynb`
  - **Use Cases:** Track test execution, debug automation, audit trails
  - **Demo:** Complete test script with comprehensive logging
  - **Example:**
  ```python
  import logging

  logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      handlers=[
          logging.FileHandler('test_automation.log'),
          logging.StreamHandler()
      ]
  )

  logger = logging.getLogger(__name__)
  logger.info("Starting test sequence")
  logger.debug(f"Voltage set to {voltage}V")
  logger.error("Instrument connection failed")
  ```

- **Decorator Basics (50 min)**
  - What are decorators?
  - Function decorators explained
  - Common built-in decorators: @property, @staticmethod, @classmethod
  - Creating simple custom decorators
  - **Materials:** `15-advanced-concepts/01-decorators.ipynb` (basic sections)
  - **Use Cases:**
    - Timing measurements
    - Retry logic
    - Input validation
    - Logging function calls
  - **Example:**
  ```python
  import time
  from functools import wraps

  def timing_decorator(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          start = time.time()
          result = func(*args, **kwargs)
          elapsed = time.time() - start
          logger.info(f"{func.__name__} took {elapsed:.3f}s")
          return result
      return wrapper

  @timing_decorator
  def measure_voltage():
      # measurement code
      pass
  ```

- **Practical Integration (20 min)**
  - Combine logging with decorators
  - Build reusable decorators for instrumentation
  - Error handling + logging + decorators together

**Key Focus:** Professional logging and basic decorators for cleaner code
**Assignments:**
- Exercise 1: Add comprehensive logging to previous file I/O exercises
- Exercise 2: Create retry decorator for instrument communication
- Exercise 3: Build timing decorator to measure test execution time
- Exercise 4: Combine error handling, logging, and decorators

---

### Day 9: Object-Oriented Programming - Fundamentals (2 hours)
**Theme:** "Organizing Complex Systems with Classes"

**Session Breakdown:**
- **OOP Introduction (25 min)**
  - Why OOP? (managing complexity, code reuse, encapsulation)
  - Classes vs instances (blueprint vs object)
  - Comparison to LabVIEW: VIs with data → Classes with methods and attributes
  - When to use OOP vs functions
  - **Materials:** `13-oops/01-intro.ipynb`
  - **Use Cases:** Instrument drivers, test equipment abstraction

- **Classes and Objects (40 min)**
  - Defining classes with class keyword
  - `__init__` method (constructor)
  - Instance attributes (self.attribute)
  - Instance methods (functions that belong to objects)
  - Creating and using objects
  - **Materials:** `13-oops/02-pillars.ipynb` (encapsulation), `13-oops/03-attributes.ipynb`
  - **Demo:** Create Instrument base class

- **Methods and Attributes (30 min)**
  - Instance methods vs class methods vs static methods
  - Public vs private attributes (naming conventions with _)
  - Properties with @property decorator
  - Getters and setters
  - **Materials:** `13-oops/04-method-types.ipynb`, `13-oops/07-getters-and-setters.ipynb`
  - **Use Cases:** Instrument configuration, state management

- **Dunder Methods (Magic Methods) (25 min)**
  - What are dunder methods?
  - `__str__` and `__repr__` - string representation
  - `__eq__` - equality comparison
  - `__len__` - length support
  - **Materials:** `15-advanced-concepts/02-dunder-methods.ipynb` (basic sections)
  - **Use Case:** Better debugging and printing of instrument objects
  - **Example:**
  ```python
  class PowerSupply:
      def __init__(self, name: str, max_voltage: float):
          self.name = name
          self.max_voltage = max_voltage
          self._current_voltage = 0.0

      @property
      def voltage(self) -> float:
          return self._current_voltage

      @voltage.setter
      def voltage(self, value: float):
          if value > self.max_voltage:
              raise ValueError(f"Voltage {value}V exceeds max {self.max_voltage}V")
          self._current_voltage = value

      def __str__(self) -> str:
          return f"{self.name} - {self.voltage}V"

      def __repr__(self) -> str:
          return f"PowerSupply('{self.name}', {self.max_voltage})"
  ```

**Key Focus:** Create classes for instrument drivers with proper structure
**Assignments:**
- Exercise 1: Create Multimeter class with voltage/current/resistance methods
- Exercise 2: Build DataLogger class with file management
- Exercise 3: Add properties, dunder methods for better usability
- Exercise 4: Create TemperatureController class with setpoint management

---

### Day 10: Object-Oriented Programming - Advanced (2 hours)
**Theme:** "Building Instrument Hierarchies"

**Session Breakdown:**
- **Inheritance (50 min)**
  - Parent and child classes
  - Method overriding
  - super() function
  - Multiple inheritance (brief mention, generally avoid)
  - **Materials:** `13-oops/02-pillars.ipynb` (inheritance section)
  - **Use Cases:** Create specialized instruments from base class
  - **Demo:**
  ```python
  class Instrument:
      def __init__(self, name: str):
          self.name = name
          self.connected = False

      def connect(self):
          raise NotImplementedError

      def disconnect(self):
          raise NotImplementedError

  class PowerSupply(Instrument):
      def __init__(self, name: str, max_voltage: float):
          super().__init__(name)
          self.max_voltage = max_voltage

      def connect(self):
          # Specific implementation
          self.connected = True

  class Multimeter(Instrument):
      def connect(self):
          # Different implementation
          self.connected = True
  ```

- **Polymorphism (25 min)**
  - Same interface, different implementations
  - Duck typing in Python
  - **Materials:** `13-oops/02-pillars.ipynb` (polymorphism section)
  - **Use Case:** Common interface for all instruments (connect, disconnect, measure)

- **Composition (35 min)**
  - Has-a relationship vs is-a relationship
  - When to use composition over inheritance (prefer composition!)
  - Building complex objects from simpler ones
  - **Materials:** `13-oops/06-composition.ipynb`
  - **Use Cases:** TestStation has-a PowerSupply, has-a Multimeter, has-a DataLogger
  - **Demo:**
  ```python
  class TestStation:
      def __init__(self):
          self.power_supply = PowerSupply("PSU-1", 30.0)
          self.multimeter = Multimeter("DMM-1")
          self.logger = DataLogger("results.csv")

      def run_test(self, device_id: str):
          self.logger.log_start(device_id)
          self.power_supply.voltage = 5.0
          current = self.multimeter.measure_current()
          self.logger.log_measurement(device_id, current)
  ```

- **Design Principles (10 min)**
  - SOLID principles (brief overview)
  - When to use inheritance vs composition
  - Keeping classes focused (Single Responsibility)

**Key Focus:** Build robust instrument driver hierarchies
**Assignments:**
- Exercise 1: Create instrument hierarchy (Instrument → SCPI_Instrument → specific devices)
- Exercise 2: Build TestRig using composition
- Exercise 3: Implement polymorphic measure() across different instruments
- Exercise 4: Design complete test automation system with OOP

---

### Day 11: NumPy for Signal & Data Processing (2 hours)
**Theme:** "High-Performance Numerical Computing"

**Session Breakdown:**
- **Why NumPy for Instrumentation (15 min)**
  - Performance comparison: lists vs NumPy arrays
  - Element-wise operations (vectorization)
  - Comparison to LabVIEW arrays (similar performance!)
  - When to use NumPy vs regular lists
  - **Materials:** `22-numpy/01-basics-and-indexing.ipynb` (intro)

- **NumPy Arrays Fundamentals (45 min)**
  - Creating arrays: from lists, zeros, ones, linspace, arange
  - Array attributes: shape, dtype, ndim, size
  - Indexing and slicing (1D and 2D arrays)
  - Array reshaping and transposing
  - **Materials:** `22-numpy/01-basics-and-indexing.ipynb`, `22-numpy/02-creation-and-manipulation.ipynb`
  - **Use Cases:** Store waveforms, voltage/current arrays, multi-channel data
  - **Demo:** Simulate oscilloscope waveform, slice time windows

- **NumPy Operations (45 min)**
  - Element-wise arithmetic (+, -, *, /)
  - Mathematical functions (sin, cos, exp, log, sqrt)
  - Statistical functions: mean, std, min, max, sum, median, percentile
  - Boolean indexing and masking
  - Broadcasting rules
  - **Materials:** `22-numpy/03-operations-and-statistics.ipynb`
  - **Use Cases:** Statistics on test runs, filter outliers, threshold detection
  - **Demo:**
  ```python
  import numpy as np

  # Voltage measurements
  voltages = np.array([3.3, 3.28, 3.35, 3.29, 5.2, 3.31])  # One outlier!

  # Calculate statistics
  mean_v = np.mean(voltages)
  std_v = np.std(voltages)

  # Filter outliers (beyond 2 std deviations)
  mask = np.abs(voltages - mean_v) < 2 * std_v
  clean_voltages = voltages[mask]

  # Calculate RMS
  rms = np.sqrt(np.mean(voltages**2))
  ```

- **Signal Processing Example (15 min)**
  - Load DAQ data
  - Calculate RMS, peak-to-peak
  - Detect threshold crossings
  - Find peaks

**Key Focus:** Efficient numerical operations for measurement data
**Assignments:**
- Exercise 1: Process voltage array - comprehensive statistics
- Exercise 2: Analyze multi-channel DAQ data (2D arrays)
- Exercise 3: Threshold alarm with hysteresis
- Exercise 4: Peak detection algorithm for waveforms
- Exercise 5: Calculate power from V and I arrays

---

### Day 12: Pandas & Data Visualization (2 hours)
**Theme:** "Test Data Analysis and Reporting"

**Session Breakdown:**
- **Pandas DataFrames (40 min)**
  - What are DataFrames? (spreadsheet in Python)
  - Loading CSV files
  - Exploring: head(), tail(), info(), describe(), shape
  - Selecting columns, rows, cells (loc, iloc)
  - Filtering with boolean indexing and query()
  - **Materials:** `23-pandas/01-data-analysis-basics.ipynb` (sections 1-6)
  - **Use Cases:** Analyze test results across devices/conditions/time

- **Data Manipulation (30 min)**
  - Creating calculated columns
  - Sorting data
  - Grouping and aggregation (groupby)
  - Handling missing data
  - **Materials:** `23-pandas/01-data-analysis-basics.ipynb` (sections 7-8)
  - **Demo:** Analyze hardware test data (hw_measurements.csv)

- **Data Visualization (40 min)**
  - Line plots (compare to LabVIEW graphs!)
  - Scatter plots (voltage vs current)
  - Bar plots (pass/fail counts)
  - Histograms (distributions)
  - Box plots (statistical summaries)
  - Subplots (multiple charts)
  - Customizing: labels, titles, legends, colors
  - **Materials:** `23-pandas/01-data-analysis-basics.ipynb` (visualization sections)
  - **Demo:** Multi-panel test report

- **Integration Example (10 min)**
  - Load → Clean → Analyze → Visualize → Export workflow

**Key Focus:** Complete data analysis and visualization pipeline
**Assignments:**
- Exercise 1: Analyze test dataset - create summary report
- Exercise 2: Build automated test data analyzer
- Exercise 3: Weekly report generator with multiple plots
- Exercise 4: Analyze hw_measurements.csv - find patterns and failures
- Exercise 5: Dashboard-style report (4-6 plots)

---

### Day 13: Hardware Interfacing - PyVISA & Serial (2 hours)
**Theme:** "Controlling Real Instruments"

**Session Breakdown:**
- **Instrument Communication Overview (15 min)**
  - VISA (Virtual Instrument Software Architecture)
  - GPIB, USB, Ethernet, Serial interfaces
  - SCPI (Standard Commands for Programmable Instruments)
  - Comparison to LabVIEW VISA VIs
  - Installing PyVISA and backends

- **PyVISA Basics (50 min)**
  - Resource Manager - finding instruments
  - Opening connections
  - Writing commands (write, query)
  - Reading responses
  - Timeout and error handling
  - Closing connections
  - **Example:**
  ```python
  import pyvisa

  rm = pyvisa.ResourceManager()
  instruments = rm.list_resources()

  # Connect to power supply
  ps = rm.open_resource('GPIB::1::INSTR')
  ps.timeout = 5000

  # SCPI commands
  ps.write('VOLT 3.3')
  ps.write('CURR 0.5')
  ps.write('OUTP ON')

  # Query measurements
  voltage = float(ps.query('MEAS:VOLT?'))
  current = float(ps.query('MEAS:CURR?'))

  ps.close()
  ```

- **Serial Communication (35 min)**
  - pySerial library
  - Opening serial ports (COM ports / /dev/tty*)
  - Configuration: baud rate, data bits, parity
  - Reading and writing data
  - Binary vs text data
  - **Use Cases:** Arduino, custom test equipment, UART sensors
  - **Example:**
  ```python
  import serial

  ser = serial.Serial(
      port='COM3',
      baudrate=9600,
      bytesize=8,
      parity='N',
      stopbits=1,
      timeout=1
  )

  ser.write(b'READ_TEMP\n')
  response = ser.readline()
  temperature = float(response.decode().strip())

  ser.close()
  ```

- **Building Instrument Driver Class (20 min)**
  - Combine OOP + PyVISA
  - Error handling and logging
  - **Integration example:**
  ```python
  class PowerSupply:
      def __init__(self, resource_name: str):
          rm = pyvisa.ResourceManager()
          self.instrument = rm.open_resource(resource_name)
          self.instrument.timeout = 5000
          logger.info(f"Connected to {self.identify()}")

      def identify(self) -> str:
          return self.instrument.query('*IDN?').strip()

      def set_voltage(self, voltage: float) -> None:
          self.instrument.write(f'VOLT {voltage}')
          logger.debug(f"Set voltage to {voltage}V")

      def measure_current(self) -> float:
          response = self.instrument.query('MEAS:CURR?')
          return float(response)

      def close(self):
          self.instrument.close()
  ```

**Key Focus:** Control real instruments with Python
**Assignments:**
- Exercise 1: Query instrument *IDN?
- Exercise 2: Create oscilloscope driver class
- Exercise 3: Automated power supply ramping script
- Exercise 4: Retry logic for serial communication
- Exercise 5: Complete test with multiple instruments

**Note:** This content needs to be created (not in current repo)

---

### Day 14: Network Communication - TCP & HTTP (2 hours)
**Theme:** "Modern Instrument Communication"

**Session Breakdown:**
- **TCP Socket Communication (55 min)**
  - Why TCP? (many modern instruments use TCP/IP)
  - socket module basics
  - Client vs server
  - Creating TCP client for instruments
  - Sending and receiving data
  - Error handling and timeouts
  - **Use Case:** LAN-based instruments (oscilloscopes, power supplies)
  - **Example:**
  ```python
  import socket

  class TCPInstrument:
      def __init__(self, host: str, port: int):
          self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          self.sock.settimeout(5.0)
          self.sock.connect((host, port))
          logger.info(f"Connected to {host}:{port}")

      def send_command(self, command: str) -> None:
          self.sock.sendall(command.encode() + b'\n')

      def query(self, command: str) -> str:
          self.send_command(command)
          response = self.sock.recv(4096)
          return response.decode().strip()

      def close(self):
          self.sock.close()
  ```

- **HTTP and REST APIs (55 min)**
  - requests library - the standard for HTTP
  - GET, POST, PUT, DELETE methods
  - Working with JSON responses
  - Authentication (API keys, tokens)
  - Error handling
  - **Use Cases:**
    - Web-based instruments
    - Cloud services
    - Lab information systems
    - Modern test equipment APIs
  - **Materials:** `18-external-libraries/01-requests.ipynb`
  - **Example:**
  ```python
  import requests

  # Query cloud-based test database
  response = requests.get(
      'https://api.testlab.com/results',
      params={'device_id': 'DAQ-001'},
      headers={'Authorization': 'Bearer YOUR_TOKEN'},
      timeout=10
  )

  if response.status_code == 200:
      data = response.json()
      results = data['test_results']
  else:
      logger.error(f"API error: {response.status_code}")

  # POST test result
  test_data = {
      'device_id': 'DAQ-001',
      'voltage': 3.3,
      'current': 0.15,
      'status': 'PASS'
  }

  response = requests.post(
      'https://api.testlab.com/results',
      json=test_data,
      headers={'Authorization': 'Bearer YOUR_TOKEN'}
  )
  ```

- **Practical Integration (10 min)**
  - Choose the right protocol for your instrument
  - Comparison: PyVISA vs TCP vs HTTP
  - Building unified instrument interface

**Key Focus:** Modern network-based instrument control
**Assignments:**
- Exercise 1: Create TCP client for LAN instrument
- Exercise 2: Query REST API for test data
- Exercise 3: Build HTTP-based instrument driver
- Exercise 4: POST test results to cloud database
- Exercise 5: Compare PyVISA, TCP, and HTTP approaches

**Note:** This is new content (not in current repo)

---

### Day 15: Database Integration with SQLite (2 hours)
**Theme:** "Persistent Test Data Storage"

**Session Breakdown:**
- **Why Databases for Test Data? (10 min)**
  - CSV limitations for large datasets
  - Structured queries
  - Relationships between data
  - Data integrity
  - When to use database vs CSV

- **SQLite Basics (50 min)**
  - Why SQLite? (serverless, file-based, perfect for local storage)
  - sqlite3 module (built into Python!)
  - Creating database and tables
  - INSERT, SELECT, UPDATE, DELETE operations
  - Query filtering with WHERE
  - Connection management
  - **Example:**
  ```python
  import sqlite3
  from datetime import datetime

  # Connect to database (creates if doesn't exist)
  conn = sqlite3.connect('test_results.db')
  cursor = conn.cursor()

  # Create table
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS test_results (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          device_id TEXT NOT NULL,
          timestamp TEXT NOT NULL,
          voltage REAL,
          current REAL,
          temperature REAL,
          status TEXT,
          notes TEXT
      )
  ''')

  # Insert test result
  cursor.execute('''
      INSERT INTO test_results
      (device_id, timestamp, voltage, current, temperature, status)
      VALUES (?, ?, ?, ?, ?, ?)
  ''', ('DAQ-001', datetime.now().isoformat(), 3.3, 0.15, 25.5, 'PASS'))

  conn.commit()

  # Query results
  cursor.execute('''
      SELECT * FROM test_results
      WHERE device_id = ? AND status = 'FAIL'
      ORDER BY timestamp DESC
  ''', ('DAQ-001',))

  failed_tests = cursor.fetchall()

  conn.close()
  ```

- **Working with Test Data (35 min)**
  - Designing table schema for test results
  - Inserting bulk data
  - Querying with filters and aggregation
  - Joins (brief - for related tables)
  - Indexes for performance
  - **Use Cases:**
    - Store historical test results
    - Query trends over time
    - Track device performance
    - Generate reports from database

- **Integration with Pandas (20 min)**
  - Read SQL query into DataFrame
  - Write DataFrame to SQL table
  - Best of both worlds!
  - **Example:**
  ```python
  import pandas as pd
  import sqlite3

  conn = sqlite3.connect('test_results.db')

  # Read SQL query into DataFrame
  df = pd.read_sql_query('''
      SELECT device_id, AVG(voltage) as avg_voltage,
             COUNT(*) as test_count
      FROM test_results
      GROUP BY device_id
  ''', conn)

  # Write DataFrame to SQL
  df.to_sql('summary_stats', conn, if_exists='replace', index=False)

  conn.close()
  ```

- **Best Practices (5 min)**
  - Always use parameterized queries (prevent SQL injection)
  - Close connections properly
  - Transaction management (commit/rollback)
  - Backup strategies

**Key Focus:** Store and query test data in databases
**Assignments:**
- Exercise 1: Create database schema for your test data
- Exercise 2: Write functions to insert and query test results
- Exercise 3: Build TestDatabase class with OOP
- Exercise 4: Generate reports from database using Pandas
- Exercise 5: Compare CSV vs database for 1000+ test results

**Note:** This is new content (not in current repo)

---

### Day 16: Testing & AI-Assisted Programming (2 hours)
**Theme:** "Modern Testing and Leveraging AI for Text-Based Coding"

**Session Breakdown:**

**Part 1: Pytest Basics (60 min)**

- **Why Automated Testing? (10 min)**
  - Importance of testing in test automation
  - Catching bugs early
  - Regression testing
  - Confidence in code changes
  - **Comparison:** Similar to LabVIEW's unit testing framework

- **Writing Test Functions (25 min)**
  - Test function naming conventions (test_*)
  - Assertions (assert statements)
  - pytest.approx() for floating-point comparisons
  - Testing instrument calculations
  - Testing data processing functions
  - **Materials:** `20-pytest/01-intro-basics.ipynb`
  - **Example:**
  ```python
  # test_calculations.py
  import pytest
  from calculations import calculate_power, calculate_rms
  from instruments import PowerSupply

  def test_calculate_power():
      assert calculate_power(3.3, 0.15) == pytest.approx(0.495)
      assert calculate_power(5.0, 1.0) == pytest.approx(5.0)

  def test_calculate_power_zero():
      assert calculate_power(0, 1.0) == 0
      assert calculate_power(3.3, 0) == 0

  def test_calculate_rms():
      values = [1.0, 2.0, 3.0]
      result = calculate_rms(values)
      assert result == pytest.approx(2.160, rel=0.01)

  def test_power_supply_voltage_validation():
      ps = PowerSupply("Test-PSU", max_voltage=30.0)
      with pytest.raises(ValueError):
          ps.voltage = 35.0  # Should raise error
  ```

- **Running Tests (10 min)**
  - Running pytest from command line
  - Test discovery
  - Verbose output (-v flag)
  - Running specific tests

- **Test Organization & Fixtures (15 min)**
  - Organizing tests in separate files
  - Using fixtures for setup/teardown
  - Basic fixture example for instrument initialization
  - **Example:**
  ```python
  import pytest

  @pytest.fixture
  def sample_data():
      """Provide sample test data"""
      return [3.3, 3.28, 3.35, 3.29, 3.31]

  def test_mean_calculation(sample_data):
      mean = calculate_mean(sample_data)
      assert mean == pytest.approx(3.306, rel=0.01)
  ```

**Part 2: AI-Assisted Programming for Text-Based Coding (60 min)**

- **Introduction: AI as Your Text-Based Programming Partner (10 min)**
  - Why AI tools are especially helpful for LabVIEW → Python transition
  - AI understands both graphical and text-based paradigms
  - Overview of available tools: Claude Code, GitHub Copilot, Cursor, ChatGPT
  - **Key Point:** AI can help translate your LabVIEW thinking into Python code
  - **No APIs needed** - use built-in coding assistants in your IDE

- **Using AI Coding Assistants (20 min)**
  - **Claude Code:**
    - Inline code completion as you type
    - Chat interface for questions and explanations
    - Multi-file editing and refactoring
    - Ask for explanations of Python syntax
    - Generate boilerplate code
    - Compare Python solutions to LabVIEW approaches

  - **GitHub Copilot:**
    - Real-time code suggestions in VS Code
    - Writing functions from comments/docstrings
    - Completing repetitive patterns
    - Learning common Python idioms

  - **Cursor IDE:**
    - AI-native code editor
    - Inline chat and editing
    - Codebase-aware suggestions

  - **Live Demo:** Using Claude Code/Copilot to:
    - Explain unfamiliar Python syntax
    - Convert LabVIEW VI logic to Python
    - Generate a basic instrument driver class
    - Add docstrings to functions
    - Debug an error message
    - Ask "How would I do this in Python vs LabVIEW?"

- **Prompt Engineering Best Practices (20 min)**
  - **Writing Effective Prompts:**
    - Be specific about what you want
    - Provide context (you're learning Python from LabVIEW)
    - Include relevant code snippets
    - Specify constraints and requirements
    - Ask for explanations, not just code

  - **Examples of Good vs Bad Prompts:**

    ❌ **Bad:** "Write a function"
    ✅ **Good:** "Write a Python function that takes a list of voltage measurements and returns the mean, std, and RMS. Add type hints and docstring."

    ❌ **Bad:** "Fix this"
    ✅ **Good:** "This code gives 'TypeError: unsupported operand type(s)'. I'm trying to divide a list by a number. How do I do element-wise division in Python? In LabVIEW I would use array operations."

    ❌ **Bad:** "How do I use classes?"
    ✅ **Good:** "I want to create a PowerSupply class with methods to set_voltage() and measure_current(). In LabVIEW, I'd use action engines. What's the Python equivalent using classes?"

    ❌ **Bad:** "Make this better"
    ✅ **Good:** "Review this instrument driver code and suggest improvements for error handling, logging, and following Python best practices. I come from LabVIEW background."

  - **Key Principles:**
    - Mention your LabVIEW background
    - Ask for comparisons/translations
    - Request explanations of "why"
    - Include error messages completely
    - Be specific about the desired outcome

- **Providing Context for Better AI Responses (10 min)**
  - **Share your background:**
    - "I'm transitioning from LabVIEW to Python..."
    - "I'm working on instrument automation..."
    - "I know the concept but not the Python syntax..."
    - "I'm used to LabVIEW's dataflow model..."

  - **Include relevant information:**
    - Show what you've tried
    - Share error messages completely (full traceback)
    - Mention relevant libraries you're using (NumPy, Pandas, PyVISA)
    - Describe your use case (test automation, data analysis)

  - **Ask for explanations:**
    - "Explain this like I'm coming from LabVIEW"
    - "What's the Python equivalent of LabVIEW's [feature]?"
    - "Why does Python do it this way instead of..."
    - "Can you compare this to how LabVIEW handles it?"

- **Practical AI Workflow for Learning Python (15 min)**
  - **When to use AI:**
    - ✅ Translating LabVIEW concepts to Python
    - ✅ Understanding error messages and tracebacks
    - ✅ Learning Python syntax and idioms
    - ✅ Getting unstuck on specific problems
    - ✅ Code reviews and improvements
    - ✅ Writing documentation and docstrings
    - ✅ Finding the right library or function
    - ✅ Understanding someone else's code

  - **When NOT to rely on AI:**
    - ❌ Understanding core concepts (learn them properly first)
    - ❌ Debugging complex logic without trying yourself
    - ❌ Avoiding reading documentation
    - ❌ Skipping the learning process entirely
    - ❌ Blindly copying without understanding

  - **Best practices:**
    - **Verify AI-generated code** - Always test it yourself
    - **Understand before using** - Ask "why" questions
    - **Use AI as a tutor, not a crutch** - Learn, don't just copy
    - **Iterate:** Generate → Review → Refine → Understand
    - **Build debugging skills** - Try to solve problems yourself first
    - **Read error messages** - Let AI explain them, don't just ask for fixes

  - **Complete Workflow Example:**
    1. Write basic code yourself first
    2. Get stuck on syntax or error
    3. Ask AI with proper context
    4. Review the suggestion and ask follow-up questions
    5. Understand WHY it works
    6. Test the solution
    7. Ask for comparison to LabVIEW approach
    8. Learn the pattern for future use

- **AI for Common LabVIEW → Python Tasks (5 min)**
  - Converting LabVIEW VI logic to Python functions
  - Understanding Python's sequential execution vs dataflow
  - Translating LabVIEW data types to Python equivalents
  - Finding Python libraries for LabVIEW VI functionality
  - Getting help with NumPy (array operations like LabVIEW)
  - Understanding Python's import system vs LabVIEW dependencies
  - Explaining Python decorators, context managers, comprehensions
  - Code organization (modules vs LabVIEW projects)

**Key Takeaways:**
- ✅ AI tools dramatically accelerate Python learning for LabVIEW programmers
- ✅ Good prompts include context, specifics, and your LabVIEW background
- ✅ Use AI to explain concepts and translate thinking, not just generate code
- ✅ Always understand before using AI-generated code
- ✅ AI is your 24/7 tutor for the LabVIEW → Python transition
- ✅ Prompt engineering is a valuable skill for modern programming

**Assignments:**
- Exercise 1: Write pytest tests for your instrument driver classes
- Exercise 2: Use AI (Claude Code/Copilot) to explain 3 Python concepts you find confusing, comparing them to LabVIEW
- Exercise 3: Ask AI to review and improve one of your previous exercises, then understand the improvements
- Exercise 4: Use AI to generate docstrings for your code, verify they're accurate, and learn the documentation style
- Exercise 5: Create a personal "prompt template" for asking LabVIEW → Python translation questions
- Exercise 6: Practice converting a LabVIEW VI workflow to Python with AI assistance, documenting what you learned

**Final Project Assignment (After Day 16):**

Students build a complete test automation system integrating all concepts learned:

**Option 1: Automated Test Station**
- Connect to instruments (PyVISA/TCP/serial)
- Run test sequences using OOP classes
- Collect and process data (NumPy/Pandas)
- Store results in database
- Generate visualizations
- Use AI for failure analysis
- Write pytest tests
- Full documentation

**Option 2: Data Analysis Platform**
- Load historical test data from multiple sources
- Clean and validate with Pandas
- Perform statistical analysis
- Create interactive dashboards
- Use AI for trend analysis and anomaly detection
- Generate automated reports
- Store insights in database

**Option 3: Instrument Driver Library**
- Create reusable instrument driver package
- 3+ instrument classes with proper OOP
- Comprehensive error handling and logging
- Type hints and documentation
- Full pytest test suite
- AI-generated documentation
- Example usage notebooks

**Note:** Final projects will naturally integrate all concepts from Days 1-18

---

### Day 17: PySide6 Fundamentals (2 hours)
**Theme:** "Building Python Desktop Applications with PySide6"

**Session Breakdown:**

- **Qt and PySide6 Introduction (20 min)**
  - What is Qt? What is PySide6?
  - Desktop GUI development in Python
  - Comparison: LabVIEW front panels vs PySide6 GUIs
  - Event-driven programming model
  - Why PySide6? (mature, cross-platform, professional applications)
  - Installation: `pip install PySide6`
  - Qt Designer vs code-based approach
  - **Key Point:** LabVIEW users are already familiar with UI concepts - PySide6 applies them in Python
  - **Example comparison:**
    - LabVIEW: Visual programming - drag controls onto front panel → wire to block diagram
    - PySide6: Code-based - create widget objects → connect signals to slots (methods)

- **Basic Widgets and Layouts (45 min)**
  - Creating main window and application
  - Common widgets:
    - `QPushButton` - buttons for user actions
    - `QLabel` - text/image display
    - `QLineEdit` - single-line text input
    - `QTextEdit` - multi-line text input
    - `QSpinBox`, `QDoubleSpinBox` - numeric input
    - `QComboBox` - dropdown selection
    - `QCheckBox`, `QRadioButton` - boolean/choice inputs
    - `QSlider` - value slider
  - Layout managers (automatic widget positioning):
    - `QVBoxLayout` - vertical stacking
    - `QHBoxLayout` - horizontal arrangement
    - `QGridLayout` - grid positioning (row, column)
    - Nested layouts for complex UIs
  - Setting widget properties (text, size, enabled state, tooltips, etc.)
  - **Materials:** NEW - `24-pyside6/01-introduction.ipynb`, `24-pyside6/02-widgets-and-layouts.ipynb`
  - **Live Demo:** Build simple application with various widgets
  - **Example:**
  ```python
  from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                   QPushButton, QLabel, QLineEdit, QVBoxLayout)
  import sys

  class SimpleApplication(QMainWindow):
      def __init__(self):
          super().__init__()
          self.setWindowTitle("My First PySide6 App")
          self.setGeometry(100, 100, 400, 200)

          # Central widget
          central_widget = QWidget()
          self.setCentralWidget(central_widget)

          # Create widgets
          self.label = QLabel("Enter your name:")
          self.input = QLineEdit()
          self.button = QPushButton("Submit")
          self.result_label = QLabel("")

          # Create layout
          layout = QVBoxLayout()
          layout.addWidget(self.label)
          layout.addWidget(self.input)
          layout.addWidget(self.button)
          layout.addWidget(self.result_label)

          central_widget.setLayout(layout)

  if __name__ == "__main__":
      app = QApplication(sys.argv)
      window = SimpleApplication()
      window.show()
      sys.exit(app.exec())
  ```

- **Signals and Slots (Event Handling) (40 min)**
  - Qt's signal/slot mechanism (powerful event system)
  - Built-in signals: `clicked`, `textChanged`, `valueChanged`, `currentIndexChanged`
  - Connecting signals to slots (methods)
  - Creating custom slots
  - Updating UI elements from code
  - **Comparison:** Similar to LabVIEW's event structure
  - **Materials:** NEW - `24-pyside6/03-signals-and-slots.ipynb`
  - **Demo:** Make button respond to clicks and update UI
  - **Example:**
  ```python
  class SimpleApplication(QMainWindow):
      def __init__(self):
          super().__init__()
          # ... widget setup from previous example ...

          # Connect signal to slot
          self.button.clicked.connect(self.on_button_clicked)
          self.input.textChanged.connect(self.on_text_changed)

      def on_button_clicked(self):
          """Handle button click"""
          name = self.input.text()
          if name:
              self.result_label.setText(f"Hello, {name}!")
              self.result_label.setStyleSheet("color: green")
          else:
              self.result_label.setText("Please enter a name")
              self.result_label.setStyleSheet("color: red")

      def on_text_changed(self, text):
          """Handle text input changes"""
          # Enable button only if text is not empty
          self.button.setEnabled(bool(text.strip()))
  ```

- **Complete Simple Application Example (15 min)**
  - Put it all together: functional application
  - Run the application
  - Understanding the event loop (`app.exec()`)
  - Proper application structure
  - **Use Cases:** Data entry forms, calculators, configuration tools

**Key Focus:** Understand PySide6 basics and how to build simple desktop applications

**Assignments:**
- Exercise 1: Create "Hello World" application with button that updates label
- Exercise 2: Build temperature converter (Celsius ↔ Fahrenheit) with input, button, output
- Exercise 3: Create calculator GUI with number buttons and basic operations
- Exercise 4: Design simple form with multiple input types (text, numbers, checkboxes)
- Exercise 5: Build BMI calculator with height/weight inputs and result display

---

### Day 18: Data Display & Dynamic Content (2 hours)
**Theme:** "Displaying Data and Building Interactive Interfaces"

**Session Breakdown:**

- **Tables for Data Display (30 min)**
  - `QTableWidget` for displaying tabular data
  - Creating and populating tables
  - Setting headers and column widths
  - Loading data from lists and Pandas DataFrames
  - Basic formatting (alignment, colors)
  - **Use Cases:** Display test results, measurement data, configuration tables
  - **Materials:** NEW - `24-pyside6/04-data-display.ipynb`
  - **Example:**
  ```python
  from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
  import pandas as pd

  class DataViewer(QMainWindow):
      def __init__(self):
          super().__init__()
          self.setWindowTitle("Data Viewer")

          # Create table
          self.table = QTableWidget()
          self.setCentralWidget(self.table)

          # Load and display data
          self.load_data()

      def load_data(self):
          """Load data from DataFrame into table"""
          # Sample data
          data = {
              'Device': ['DAQ-001', 'DAQ-002', 'DAQ-003'],
              'Voltage': [3.3, 3.28, 3.35],
              'Current': [0.15, 0.16, 0.14],
              'Status': ['PASS', 'PASS', 'PASS']
          }
          df = pd.DataFrame(data)

          # Set table dimensions
          self.table.setRowCount(len(df))
          self.table.setColumnCount(len(df.columns))
          self.table.setHorizontalHeaderLabels(df.columns.tolist())

          # Populate table
          for i, row in df.iterrows():
              for j, value in enumerate(row):
                  item = QTableWidgetItem(str(value))
                  self.table.setItem(i, j, item)
  ```

- **Dynamic Page Switching (30 min)**
  - `QStackedWidget` for multiple pages/views
  - Switching between different content areas
  - Navigation with buttons
  - Organizing complex UIs into separate pages
  - **Use Cases:** Settings page, data view, about page, multi-step workflows
  - **Materials:** NEW - `24-pyside6/05-dynamic-pages.ipynb`
  - **Example:**
  ```python
  from PySide6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QPushButton

  class MultiPageApp(QMainWindow):
      def __init__(self):
          super().__init__()
          self.setWindowTitle("Multi-Page Application")

          # Central widget with layout
          central_widget = QWidget()
          self.setCentralWidget(central_widget)
          layout = QVBoxLayout()

          # Navigation buttons
          nav_layout = QHBoxLayout()
          btn_page1 = QPushButton("Page 1")
          btn_page2 = QPushButton("Page 2")
          btn_page1.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
          btn_page2.clicked.connect(lambda: self.stacked.setCurrentIndex(1))
          nav_layout.addWidget(btn_page1)
          nav_layout.addWidget(btn_page2)

          # Stacked widget for page switching
          self.stacked = QStackedWidget()

          # Page 1
          page1 = QWidget()
          page1_layout = QVBoxLayout()
          page1_layout.addWidget(QLabel("This is Page 1"))
          page1_layout.addWidget(QPushButton("Action 1"))
          page1.setLayout(page1_layout)

          # Page 2
          page2 = QWidget()
          page2_layout = QVBoxLayout()
          page2_layout.addWidget(QLabel("This is Page 2"))
          page2_layout.addWidget(QPushButton("Action 2"))
          page2.setLayout(page2_layout)

          # Add pages to stacked widget
          self.stacked.addWidget(page1)
          self.stacked.addWidget(page2)

          # Add to main layout
          layout.addLayout(nav_layout)
          layout.addWidget(self.stacked)
          central_widget.setLayout(layout)
  ```

- **Image Display (20 min)**
  - `QLabel` with `QPixmap` for displaying images
  - Loading images from files
  - Scaling and resizing images
  - **Use Cases:** Display logos, diagrams, equipment photos, plots saved as images
  - **Example:**
  ```python
  from PySide6.QtGui import QPixmap
  from PySide6.QtWidgets import QLabel

  class ImageViewer(QMainWindow):
      def __init__(self):
          super().__init__()

          # Create label to display image
          self.image_label = QLabel()
          self.setCentralWidget(self.image_label)

          # Load and display image
          pixmap = QPixmap("diagram.png")
          # Scale image to fit
          scaled_pixmap = pixmap.scaled(400, 300, Qt.KeepAspectRatio)
          self.image_label.setPixmap(scaled_pixmap)
  ```

- **Basic Matplotlib Plot Embedding (25 min)**
  - Embedding simple matplotlib plots in PySide6
  - `FigureCanvas` for displaying plots
  - Creating basic line plots
  - Updating plots with new data
  - **Use Case:** Display data visualization within GUI
  - **Keep it Simple:** Just basic embedding, not complex interactions
  - **Materials:** NEW - `24-pyside6/06-basic-plotting.ipynb`
  - **Example:**
  ```python
  from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
  from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
  from matplotlib.figure import Figure
  import numpy as np

  class SimplePlotWidget(QWidget):
      def __init__(self):
          super().__init__()

          layout = QVBoxLayout()

          # Create matplotlib figure and canvas
          self.figure = Figure(figsize=(6, 4))
          self.canvas = FigureCanvas(self.figure)
          self.ax = self.figure.add_subplot(111)

          # Button to generate plot
          plot_button = QPushButton("Generate Plot")
          plot_button.clicked.connect(self.plot_data)

          layout.addWidget(self.canvas)
          layout.addWidget(plot_button)
          self.setLayout(layout)

      def plot_data(self):
          """Generate and display a simple plot"""
          # Sample data
          x = np.linspace(0, 10, 100)
          y = np.sin(x)

          # Plot
          self.ax.clear()
          self.ax.plot(x, y, 'b-', linewidth=2)
          self.ax.set_xlabel('X')
          self.ax.set_ylabel('Y')
          self.ax.set_title('Simple Plot')
          self.ax.grid(True)

          # Refresh canvas
          self.canvas.draw()
  ```

- **Creating Reusable Widget Classes (15 min)**
  - Combining widgets into custom reusable classes
  - Building your own composite widgets
  - Benefits: Code reuse, cleaner architecture
  - **Keep it Simple:** Just the basic concept, not complex custom widgets
  - **Example:**
  ```python
  class LabeledInput(QWidget):
      """Reusable widget: Label + Input field"""
      def __init__(self, label_text: str):
          super().__init__()

          layout = QHBoxLayout()
          self.label = QLabel(label_text)
          self.input = QLineEdit()

          layout.addWidget(self.label)
          layout.addWidget(self.input)
          self.setLayout(layout)

      def get_value(self) -> str:
          """Get the input value"""
          return self.input.text()

      def set_value(self, value: str):
          """Set the input value"""
          self.input.setText(value)

  # Usage in main window
  class MainWindow(QMainWindow):
      def __init__(self):
          super().__init__()

          layout = QVBoxLayout()

          # Use custom widgets
          self.name_input = LabeledInput("Name:")
          self.email_input = LabeledInput("Email:")
          self.phone_input = LabeledInput("Phone:")

          layout.addWidget(self.name_input)
          layout.addWidget(self.email_input)
          layout.addWidget(self.phone_input)

          # ... rest of UI
  ```

**Key Focus:** Display data effectively and organize complex UIs

**Assignments:**
- Exercise 1: Create table viewer that loads CSV file and displays in QTableWidget
- Exercise 2: Build multi-page app with 3 pages (Home, Settings, About) using QStackedWidget
- Exercise 3: Create image gallery viewer that displays multiple images
- Exercise 4: Add a simple line plot to an existing data viewer application
- Exercise 5: Create reusable "LabeledSpinBox" widget class (label + spinbox)
- **Challenge Exercise:** Build data analysis app combining table, plots, and page switching

---

**Final Project Assignment (Updated for Days 1-18):**

Students build a complete application integrating all concepts learned:

**Option 1: Test Automation System with GUI**
- PySide6 GUI for test control and monitoring
- Connect to instruments (PyVISA/TCP/serial)
- Run test sequences using OOP classes
- Collect and process data (NumPy/Pandas)
- Real-time plot display
- Store results in database
- Generate visualizations
- Write pytest tests
- Full documentation

**Option 2: Data Analysis Platform with Dashboard**
- PySide6 dashboard GUI for data exploration
- Load data from multiple sources (CSV, database, API)
- Clean and validate with Pandas
- Perform statistical analysis and visualization
- Interactive matplotlib plots embedded in GUI
- Export reports and results
- Multi-tab interface for different analyses
- User-friendly controls and progress indicators

**Option 3: General Purpose Application (Student's Choice)**
- Create any desktop application using Python + PySide6
- Must integrate at least 5 of the following:
  - File I/O operations
  - Data processing (NumPy/Pandas)
  - Database integration (SQLite)
  - External communication (HTTP, TCP, or serial)
  - Matplotlib visualization
  - OOP design with multiple classes
  - Error handling and logging
  - Pytest tests
  - Threading for responsiveness
- Professional GUI with proper layout, event handling, and user feedback
- Complete documentation

**Note:** Final projects will naturally integrate all concepts from Days 1-18

---

## Critical Files from Repository

### Materials Available in Current Repo:

**Day 1-2 Materials:**
- `01-setup/` - All setup notebooks
- `02-syntax/` - Syntax and comments
- `03-variables/` - Data types and casting
- `04-strings/` - String operations
- `05-operators/` - Operators
- `06-control-flow-and-loops/` - Control flow and loops
- `07-functions/01-intro.ipynb` - Function basics

**Day 3-4 Materials:**
- `08-lists/` - Lists and comprehensions
- `09-tuples/` - Tuples
- `10-sets/` - Sets
- `11-dictionaries/` - Dictionaries and comprehensions

**Day 5-6 Materials:**
- `07-functions/02-scope.ipynb` - Function scope
- `07-functions/03-docstrings.ipynb` - Documentation
- `07-functions/04-lambda-map-filter-reduce.ipynb` - Lambda functions
- `12-modules/` - Modules and packages
- `21-typing/` - Type hints (if available)

**Day 7-8 Materials:**
- `16-files/` - File I/O
- `14-error-handling/` - Error handling
- `19-development-tools/01-logging.ipynb` - Logging
- `15-advanced-concepts/01-decorators.ipynb` - Decorators

**Day 9-10 Materials:**
- `13-oops/` - All OOP materials
- `15-advanced-concepts/02-dunder-methods.ipynb` - Dunder methods

**Day 11-12 Materials:**
- `22-numpy/` - All NumPy materials
- `23-pandas/` - Pandas and visualization
- `23-pandas/hw_measurements.csv` - Sample hardware data

**Day 13 Materials:**
- **NOT IN REPO** - Need to create PyVISA and serial materials

**Day 14 Materials:**
- `18-external-libraries/01-requests.ipynb` - HTTP requests
- **TCP content** - Need to create

**Day 15 Materials:**
- **NOT IN REPO** - Need to create SQLite materials

**Day 16 Materials:**
- `20-pytest/01-intro-basics.ipynb` - Pytest basics
- **AI-assisted programming materials** - Need to create (Claude Code/Copilot demos, prompt engineering guide, LabVIEW→Python translation examples)

**Day 17 Materials:**
- **NOT IN REPO** - Need to create PySide6 fundamentals materials:
  - `24-pyside6/01-introduction.ipynb` - Qt and PySide6 introduction
  - `24-pyside6/02-widgets-and-layouts.ipynb` - Basic widgets and layouts
  - `24-pyside6/03-signals-and-slots.ipynb` - Event handling
  - Example scripts: `simple_app.py`, `calculator.py`, `temperature_converter.py`

**Day 18 Materials:**
- **NOT IN REPO** - Need to create PySide6 data display materials:
  - `24-pyside6/04-data-display.ipynb` - Tables (QTableWidget)
  - `24-pyside6/05-dynamic-pages.ipynb` - Dynamic page switching (QStackedWidget)
  - `24-pyside6/06-basic-plotting.ipynb` - Matplotlib embedding
  - Example scripts: `table_viewer.py`, `multi_page_app.py`, `image_viewer.py`, `plot_widget.py`, `reusable_widgets.py`

### Instructor Reference:
- `instructor-materials/INSTRUCTOR-DAY1-PLAN.md` - Pacing guide
- `instructor-materials/INSTRUCTOR-DAY2-PLAN.md` - Managing skill levels
- `instructor-materials/DAY2-EXERCISE-MAPPING.md` - Exercise design
- `instructor-materials/agents.md` - Course philosophy

---

## Teaching Approach for LabVIEW Programmers

### Critical Mindset Shift

LabVIEW users face a **fundamental paradigm shift** from graphical/dataflow to text/sequential:

**LabVIEW Thinking:**
- Data flows through wires
- Parallel execution by default
- Visual representation of logic
- Data types shown visually

**Python Thinking:**
- Data flows through time (sequential)
- Sequential execution by default
- Text representation of logic
- Data types are abstract

### Do's ✅

- **Acknowledge the shift** - "This feels different because it IS different"
- **Constantly compare to LabVIEW** - "In LabVIEW you'd wire X to Y, in Python you'd write..."
- **Show dataflow → sequential translation** - Draw diagrams showing VI logic becoming Python code
- **Use instrumentation examples exclusively** - voltage, current, DAQ, instruments
- **Fast pace on concepts** - They know what a loop is
- **Slower pace on syntax** - They need time to internalize text-based thinking
- **Live coding demonstrations** - Type code as you explain
- **Frequent hands-on practice** - More coding, less lecturing
- **Real-world scenarios** - Actual instrument models, realistic test cases
- **Encourage questions** - Especially "How would I do this in Python vs LabVIEW?"
- **Celebrate Python advantages** - Show where Python excels (data analysis, libraries, ecosystem)
- **Build on their strengths** - They're experienced with instrumentation domain

### Don'ts ❌

- **Don't explain what loops/conditionals ARE** - They already know the concepts
- **Don't use toy examples** - No "hello world", use measurement examples
- **Don't skip error handling** - They know Murphy's law with hardware
- **Don't rush the syntax** - Text-based thinking needs practice
- **Don't rush hardware interfacing** - This is their critical need
- **Don't assume sequential thinking comes naturally** - LabVIEW dataflow is fundamentally different
- **Don't dismiss LabVIEW** - Acknowledge its strengths (real-time, graphical debugging)
- **Don't overwhelm with too much at once** - One concept at a time

### Teaching Style

- **Assume intelligence, teach syntax and paradigms**
- **Move quickly through familiar concepts, slow down for Python-specific features**
- **Very frequent comprehension checks** - They may understand concepts but struggle with syntax
- **Pair programming encouraged** - Peer learning is powerful
- **Show multiple approaches** - "There are many ways to do this in Python"
- **Emphasize practicality** - "You'll use this every day" vs "nice to know"
- **Build confidence** - "You ARE programmers, just learning a new language"
- **Be patient with text-based adjustment** - This is a major shift

---

## Adaptations During Delivery

### If Team is Ahead of Schedule:

- Add advanced decorators (functools.lru_cache, custom decorators)
- Include pytest fixtures and parametrization
- Show scipy for signal processing (FFT, filtering)
- Demonstrate plotly or dash for interactive dashboards
- Cover context managers (with statement internals)
- Introduce async/await for concurrent instrument control
- Explore dataclasses and Pydantic for data validation
- Show more advanced SQL (joins, subqueries)

### If Team is Behind Schedule:

- **Extend to 17-20 days** with more practice time
- Add "practice days" between major topics
- Reduce Pandas scope (basic loading and filtering only)
- Simplify OOP (skip advanced inheritance, focus on composition)
- Make database optional (stick with CSV if needed)
- Make AI integration optional
- Provide more guided exercises with starter code
- Offer additional office hours or one-on-one help
- Create detailed syntax reference sheets
- Record sessions for review

### If Python Experience is Mixed:

- **Survey on Day 1** - Identify who has Python experience
- Create **two tracks**:
  - Track A: Accelerated (some Python experience)
  - Track B: Standard (no Python experience)
- Provide **advanced bonus exercises** for experienced learners
- **Pair experienced with beginners** for collaborative learning
- Offer **catch-up materials** and office hours
- Use **tiered exercises** (basic, intermediate, advanced)

---

## Success Criteria

### By End of Week 1 (Days 1-5):
✅ Write Python scripts with control flow and functions
✅ Use lists, dictionaries, and nested data structures effectively
✅ Add type hints to functions
✅ Organize code into modules
✅ Comfortable with text-based programming

### By End of Week 2 (Days 6-10):
✅ Read/write files with proper error handling
✅ Use logging for debugging
✅ Create classes for instrument drivers
✅ Use inheritance and composition
✅ Add dunder methods for better usability
✅ Build maintainable, reusable code

### By End of Week 3 (Days 11-15):
✅ Process measurement data efficiently with NumPy
✅ Analyze test results with Pandas
✅ Create publication-quality visualizations
✅ Control instruments with PyVISA/serial/TCP
✅ Query REST APIs
✅ Store test data in databases
✅ Build complete data analysis pipelines

### By End of Week 4 (Days 16-18 + Final Project):
✅ Write pytest tests for validation
✅ Use AI coding assistants (Claude Code, Copilot) effectively for learning and productivity
✅ Apply prompt engineering to get better help from AI tools
✅ Build desktop GUIs with PySide6 - widgets, layouts, event handling
✅ Display data in tables, switch between pages dynamically
✅ Embed basic matplotlib plots in GUIs
✅ Create reusable widget classes
✅ Build complete systems integrating all concepts
✅ **Ready to use Python productively in daily work**
✅ **Confident in replacing LabVIEW scripts with Python**
✅ **Leverage AI tools to continue learning independently**
✅ **Build professional desktop applications with data visualization**

### Final Project Evaluation Criteria:
- Code organization and structure (modules, classes)
- Proper use of OOP principles
- Comprehensive error handling and logging
- Type hints and documentation
- Functionality and correctness
- Appropriate use of libraries (NumPy, Pandas, PyVISA)
- Test coverage (pytest)
- Demonstrates understanding of AI-assisted development workflow (optional but encouraged)
- Professional code quality

---

## Post-Training Support

### Immediate Next Steps (Weeks 1-2 after training):
1. **Apply to real project** - Select ONE LabVIEW task and rewrite in Python
2. **Set up development environment** - Configure for actual work
3. **Start instrument driver library** - Build drivers for lab equipment
4. **Pair programming** - Work together on first project

### Week 3-4 After Training:
1. **Code review sessions** - Review each other's code
2. **Office hours** - Weekly Q&A sessions
3. **Build shared library** - Contribute reusable components
4. **Document patterns** - Capture best practices

### Continued Learning Resources:

**Official Documentation:**
- Python: https://docs.python.org/3/
- NumPy: https://numpy.org/doc/
- Pandas: https://pandas.pydata.org/docs/
- PyVISA: https://pyvisa.readthedocs.io/
- Requests: https://docs.python-requests.org/

**Learning Platforms:**
- Real Python: https://realpython.com/ (excellent tutorials)
- Python for Test & Measurement (industry-specific)
- PyVISA examples and tutorials
- Automate the Boring Stuff with Python (free online book)

**Community:**
- Stack Overflow (python, pyvisa, pandas tags)
- Python Discord/Slack channels
- r/Python and r/learnpython subreddits

### Advanced Topics for Future Training:

**Data Science Track (4-6 days):**
- SciPy for signal processing (FFT, filtering, curve fitting)
- Advanced Pandas (time series, multi-index)
- Seaborn for statistical visualization
- Plotly for interactive dashboards

**Web Development Track (3-4 days):**
- Flask for web dashboards
- REST API development
- Real-time data streaming
- Dash for interactive test monitoring

**Database Track (2-3 days):**
- PostgreSQL for enterprise data
- SQLAlchemy ORM
- Database design and optimization
- Time-series databases (InfluxDB)

**Advanced Python Track (3-4 days):**
- Async/await for concurrent operations
- Context managers and generators
- Metaclasses (advanced OOP)
- Performance optimization
- Profiling and debugging

**AI/ML Track (5-7 days):**
- Machine learning basics (scikit-learn)
- Anomaly detection in test data
- Predictive maintenance
- Using LLMs for data analysis
- OpenAI API integration

**DevOps Track (2-3 days):**
- Git workflows for teams
- CI/CD for test automation (GitHub Actions, Jenkins)
- Docker for reproducible environments
- Testing strategies at scale

---

## Materials Organization

### Repository Structure for Delivery:

```
python-labview-training/
├── day-01/
│   ├── notebooks/          # Setup, syntax, variables, operators
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── labview_comparison_day1.md
│
├── day-02/
│   ├── notebooks/          # Strings, control flow, functions
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── labview_comparison_day2.md
│
├── day-03/
│   ├── notebooks/          # Lists, tuples, sets
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── sample_data.csv
│
├── day-04/
│   ├── notebooks/          # Dictionaries, JSON
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── config_examples/
│
├── day-05/
│   ├── notebooks/          # Functions, type hints, docstrings
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── function_templates.py
│
├── day-06/
│   ├── notebooks/          # Modules, packages
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── example_package/
│
├── day-07/
│   ├── notebooks/          # File I/O, error handling
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── test_data/
│
├── day-08/
│   ├── notebooks/          # Logging, decorators
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── decorator_examples.py
│
├── day-09/
│   ├── notebooks/          # OOP fundamentals
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── instrument_template.py
│
├── day-10/
│   ├── notebooks/          # OOP advanced
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── test_station_example.py
│
├── day-11/
│   ├── notebooks/          # NumPy
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── waveform_data.csv
│
├── day-12/
│   ├── notebooks/          # Pandas, visualization
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── hw_measurements.csv
│
├── day-13/
│   ├── notebooks/          # PyVISA, serial (CREATE NEW)
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   ├── pyvisa_examples/
│   └── instrument_setup.md
│
├── day-14/
│   ├── notebooks/          # TCP, HTTP (CREATE NEW)
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── api_examples/
│
├── day-15/
│   ├── notebooks/          # SQLite (CREATE NEW)
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   ├── schema_examples.sql
│   └── sample_database.db
│
├── day-16/
│   ├── notebooks/          # Pytest, AI-assisted programming
│   ├── pytest_examples/
│   ├── ai_assistant_guide.md    # Guide to using Claude Code/Copilot
│   ├── prompt_engineering_examples.md
│   ├── labview_to_python_prompts.md
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── final_project_specs.md
│
├── day-17/
│   ├── notebooks/          # PySide6 fundamentals (CREATE NEW)
│   ├── examples/
│   │   ├── simple_app.py
│   │   ├── temperature_converter.py
│   │   └── calculator.py
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── pyside6_basics_guide.md
│
├── day-18/
│   ├── notebooks/          # PySide6 data display (CREATE NEW)
│   ├── examples/
│   │   ├── table_viewer.py
│   │   ├── multi_page_app.py
│   │   ├── image_viewer.py
│   │   ├── plot_widget.py
│   │   └── reusable_widgets.py
│   ├── exercises.ipynb
│   ├── solutions.ipynb
│   └── data_display_patterns.md
│
├── instructor-materials/
│   ├── TEACHING_GUIDE.md
│   ├── LABVIEW_PYTHON_COMPARISON.md
│   ├── PACING_GUIDE_15_DAYS.md
│   ├── COMMON_ISSUES.md
│   ├── timing-per-day.md
│   └── evaluation-rubric.md
│
├── reference/
│   ├── python-syntax-cheatsheet.pdf
│   ├── labview-python-cheatsheet.pdf
│   ├── type-hints-reference.pdf
│   ├── scpi-commands-reference.pdf
│   └── instrument-list.md
│
└── final-projects/
    ├── project1-automated-test-station/
    ├── project2-data-analysis-platform/
    └── project3-instrument-library/
```

---

## Hardware and Software Requirements

### Student Machines:
- **OS:** Windows 10/11 (preferred for VISA), macOS, or Linux
- **Python:** 3.9 or higher (3.11+ recommended)
- **IDE:** VS Code with Python extension
- **RAM:** 8GB minimum, 16GB recommended
- **Storage:** 5GB free space

### Required Python Packages:
```bash
# Install in virtual environment
pip install numpy pandas matplotlib seaborn
pip install pytest pytest-cov
pip install pyvisa pyvisa-py
pip install pyserial
pip install requests
pip install jupyter ipykernel
pip install python-dotenv  # For managing credentials
pip install PySide6  # For GUI development (Days 17-18)
```

### Recommended IDE Extensions (Day 16):
- **GitHub Copilot** (VS Code extension) - AI code completion
- **Claude Code CLI** - AI coding assistant
- **Cursor** (optional) - AI-native code editor

### Instructor Requirements:
- **Projection/Screen sharing** for live coding
- **Sample instruments** or simulators for Day 13 demonstrations
- **VISA backend** installed (NI-VISA or pyvisa-py)
- **Serial devices** or USB-serial adapters
- **Network-accessible instruments** for TCP demo (or simulator)
- **Whiteboard** for drawing LabVIEW ↔ Python comparisons

### Optional but Recommended:
- **Git** for version control
- **GitHub/GitLab** account for code sharing
- **VISA instrument simulators** (for practice without hardware)
- **Slack/Teams/Discord** for class communication
- **Second monitor** for students (code on one, docs/exercises on other)

---

## Frequently Anticipated Questions

### Q: "Why not just use LabVIEW for everything?"
**A:** Python complements LabVIEW! Use LabVIEW for real-time control and hardware interfacing where it excels. Use Python for:
- Complex data analysis (Pandas, NumPy, SciPy)
- Machine learning and AI
- Cloud integration and APIs
- Web dashboards
- Massive open-source ecosystem
- Text-based version control (better Git integration)
- Cross-platform deployment

### Q: "Can Python replace LabVIEW for real-time control?"
**A:** **Not for deterministic real-time.** LabVIEW (especially with FPGA) is superior for hard real-time requirements (microsecond timing). Python excels at:
- Test automation and orchestration
- Data processing and analysis
- System-level integration
- Millisecond-level timing (sufficient for most test automation)

### Q: "Is Python fast enough for data acquisition?"
**A:** NumPy operations are very fast (C-level performance). For most test automation, Python is more than adequate. For extremely high-speed continuous acquisition (100kHz+), LabVIEW may be better, but Python can handle post-processing of that data excellently.

### Q: "Can I call Python from LabVIEW or vice versa?"
**A:** **Yes!** Several approaches:
- LabVIEW can execute Python scripts using Python nodes
- Python can interface with LabVIEW through VI Server
- Shared libraries (DLL) can bridge both
- Network communication (TCP/HTTP) between LabVIEW and Python
- This enables hybrid approaches: LabVIEW for RT control, Python for analysis

### Q: "What about debugging? LabVIEW's debugging is visual."
**A:** VS Code has excellent Python debugging:
- Breakpoints, step-through, variable inspection
- Watch expressions
- Call stack visualization
- Debug console for live evaluation
Plus comprehensive logging helps with deployed scripts. Takes adjustment but is very powerful.

### Q: "Do I need to learn Git?"
**A:** Highly recommended for professional development. Git works much better with text-based code (Python) than with binary files (LabVIEW VIs). We assume basic Git familiarity but won't focus on it in this training.

### Q: "Will we learn machine learning/AI?"
**A:** Day 16 covers AI-assisted programming using tools like Claude Code and GitHub Copilot to help you learn Python faster. These AI coding assistants are especially helpful for the LabVIEW → Python transition, providing real-time explanations and code suggestions. We also teach prompt engineering - how to ask AI tools effective questions. Full machine learning (scikit-learn, TensorFlow, PyTorch) is beyond this fundamentals course, but this training gives you the foundation (NumPy, Pandas) needed for those advanced topics.

### Q: "How do I handle licensing for commercial instruments?"
**A:**
- NI-VISA requires licenses (usually already have if using LabVIEW)
- For open-source alternative: pyvisa-py with appropriate backends
- Check instrument documentation for Python API availability
- Many vendors now provide Python APIs (Keysight, Tektronix, R&S)

### Q: "Can Python do parallel processing like LabVIEW's dataflow?"
**A:** Yes, but differently:
- Threading (for I/O-bound tasks like waiting for instruments)
- Multiprocessing (for CPU-bound tasks)
- Async/await (modern approach for concurrent I/O)
- Not covered in this fundamentals course but important for advanced work

### Q: "What if I get stuck after training?"
**A:** Multiple support channels:
- Office hours (weekly for first month)
- Internal Python users group
- Stack Overflow (huge community)
- Course Slack/Discord channel
- Pair programming with colleagues
- Comprehensive documentation and examples provided

---

## Conclusion

This **18-day training plan** provides a comprehensive, practical foundation for LabVIEW programmers transitioning to Python. The curriculum:

✅ **Respects the paradigm shift** - Adequate time for graphical→text transition
✅ **Respects existing expertise** - Fast on concepts, thorough on syntax
✅ **Focuses on practical application** - Instrumentation examples throughout
✅ **Covers essential topics** - Fundamentals through hardware interfacing
✅ **Includes modern best practices** - Type hints, logging, testing, OOP
✅ **Adds requested topics** - TCP, HTTP, database, AI integration, desktop GUI development with data visualization
✅ **Includes hands-on practice** - Every day has relevant exercises
✅ **Builds progressively** - Logical topic progression
✅ **Realistic pacing** - Suited for beginners, with manageable daily load

### What Makes This Plan Different:

1. **Acknowledges the cognitive shift** from dataflow to sequential thinking
2. **Proper topic ordering** - Functions before file I/O, foundations before advanced
3. **Type hints included** - Important for LabVIEW users accustomed to strong typing
4. **Modern networking** - TCP and HTTP for contemporary instruments
5. **Database integration** - Essential for test data management
6. **GUI development** - PySide6 fundamentals and data visualization
7. **Realistic pacing** - 18 days with manageable 2-hour daily sessions
8. **Comprehensive** - From "Hello World" to complete desktop applications with GUIs

### Expected Outcome:

By Day 18, team members can:
- **Confidently write Python** for various applications
- **Analyze data** with NumPy and Pandas
- **Control hardware** via PyVISA, serial, TCP, HTTP (when needed)
- **Store and query data** in databases
- **Build desktop GUIs** with PySide6 - tables, plots, dynamic pages
- **Build professional systems** with proper OOP, logging, error handling, testing
- **Complement their LabVIEW expertise** and expand their capabilities significantly
- **Apply Python to diverse problem domains** beyond just instrumentation
- **Continue learning independently** with solid foundation and AI assistance

### Next Steps:

1. **Review this plan** - Adjust as needed for your specific team/schedule
2. **Create missing materials** - Days 13, 14, 15, 17, 18 content
3. **Customize exercises** - Use your actual instruments and test scenarios
4. **Prepare examples** - LabVIEW↔Python comparison code
5. **Set up environment** - Ensure all software/hardware ready
6. **Survey team** - Assess Python experience and specific needs
7. **Schedule training** - Block out the days
8. **Communicate plan** - Share with team so they can prepare

**This training will empower your team to leverage Python's vast ecosystem while maintaining their LabVIEW expertise, making them significantly more versatile and effective!**
