# DS Algo Simulator - LangGraph

A simple backend functionality for a Data Structures and Algorithms (DSA) simulator built using LangGraph. This repository currently includes:

- **Palindrome Checker**: Determines whether a given string is a palindrome.
- **Longest Duplicate Substring Finder**: Identifies the longest duplicate substring within a given string.

## Features

- **Palindrome Checker**: 
  - Input a string and the function checks if it is a palindrome.
- **Longest Duplicate Substring Finder**: 
  - Input a string and the function finds the longest substring that appears more than once.

## Future Development

- Adding more DSA functionalities.
- Developing a frontend interface to interact with the backend.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/kpbroz/ds-algo-simulator-langgraph.git
   ```
2. Navigate to the repository:
   ```bash
   cd ds-algo-simulator-langgraph
   ```
3. Open `main.py` and set your input string:
   ```python
   text = "can you find the longest duplicate substring of banana and also check whether hannah is palindrome"
   ```
4. Run the script:
   ```bash
   python main.py
   ```

## Example

```python
text = "banana"
# Output: Longest duplicate substring: 'ana'

text = "hannah"
# Output: 'hannah' is a palindrome
```

## Requirements

- Python 3.x
- LangGraph

## Installation

Install the required packages:
```bash
pip install -r requirements.txt
```

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

