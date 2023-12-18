
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
**All data**

![App Screenshot](https://raw.githubusercontent.com/muhammadusufs/pdfparser/main/media/get_all_data.png)


**Just universities**

![App Screenshot](https://raw.githubusercontent.com/muhammadusufs/pdfparser/main/media/universities.png)

**Just details**
![App Screenshot](https://raw.githubusercontent.com/muhammadusufs/pdfparser/main/media/get_data.png)
