from PyPDF2 import PdfReader

class DataParser:
    def __init__(self, file_path):
        
        reader = PdfReader(file_path)
        text = reader.pages[0].extract_text()

        self.file_path = file_path
        self.data = text
        self.parsed_data = {}
        self.data_path = [
            "F.I.Sh.:",
            "Pasport:",
            "Tug‘ilgan sana:",
            "Test topshirish fanlari:",
            "Test sinovi topshirish hududi va hududga kelish vaqti:",
            "Test topshirish manzili:",
            "Test topshirish joyi nomi:",
            "Smena:",
            "Sektor raqami:",
            "Guruh raqami:",
            "Ta'lim shakli:",
            "Ta'lim tili:",
            "Test topshirish alifbosi:",
            "TANLANGAN TA'LIM YO‘NALISHLARI",
        ]
        
        self.university_path = [
            "TANLANGAN TA'LIM YO‘NALISHLARI",
            "IMTIYOZLAR"
        ]

        
    def parse_data(self) -> dict:
        text = self.data
        data_path = self.data_path
        parsed_data = {}
        
        for i in range(len(data_path)):
            if i+1 != len(data_path):
                obj = text[text.index(data_path[i]):text.index(data_path[i+1])].replace(data_path[i], "").replace("\n", "").strip()        
                parsed_data[data_path[i]] = obj
        
        self.parsed_data["details"] = parsed_data
        return parsed_data


    def parse_universities(self) -> list:
        text = self.data
        data_path = self.university_path
        
        universities = text[text.index(data_path[0]):text.index(data_path[1])].replace(data_path[0], "").strip()
        data = universities.splitlines()
        
        parsed_data = []
        
        for i in range(len(data)):
            obj = {}
            
            if i%2==0 or i == 0:
                obj["name"] = data[i][1:]
                obj["faculty"] = data[i+1]
                parsed_data.append(obj)
        
        self.parsed_data["universities"] = parsed_data
        return parsed_data
    
    
    def parse_all_data(self) -> dict:
        return self.parse_data(), self.parse_universities()
    
        
data = DataParser("mpdf.pdf")
data.parse_all_data()

print(data.parsed_data)