from PyPDF2 import PdfReader
print("""
 ______   _  __   _          _            _     _____                           _            
| ___ \ | |/ _| | |        | |          | |   /  __ \                         | |           
| |_/ /_| | |_  | |_ ___   | |_ _____  _| |_  | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __ 
|  __/ _` |  _| | __/ _ \  | __/ _ \ \/ / __| | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| | | (_| | |   | || (_) | | ||  __/>  <| |_  | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |   
\_|  \__,_|_|    \__\___/   \__\___/_/\_\\__|  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|   
                                                                                            
                                                                                            
                                                                                              
                                                                                              
""")
#reader = PdfReader("/Users/allen/Desktop/10134-MiniProject.pdf")
reader = PdfReader(input("Input PDF Files:\n>"))
i=1
num_pages = len(reader.pages)
while(i<num_pages):
    page = reader.pages[i]
    print(page.extract_text((0, 90)))
    print("\n")
    i=i+1
