
# Parser with PyPDF2

PDF parser for students blank.



## Installation

Clone the project

```bash
  git clone https://github.com/muhammadusufs/pdfparser
```

Go to the project directory

```bash
  cd my-project
```
Run terminal command
```bash
  pip install -r requirements.txt

```
    
## Usage/Examples
Parsing data from pdf
```python
data = DataParser(file_path)
data.parse_all_data()

```
Getting result
```python
print(data.parsed_data) # Prints all data 
print(data.parse_data)  # Print only details
print(data.parse_universities) # Prints univerties and faculties
```

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

