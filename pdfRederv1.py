from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Button, filedialog
import PyPDF2 as pypdf

class ShowPdf(pdf.ShowPdf):
    def goto(self, page):
        try:
            self.text.see(self.img_object_li[page - 1])
        except IndexError:
            if self.img_object_li:
                self.text.see(self.img_object_li[-1])


#filename = filedialog.askopenfilename()
root = Tk(className='python-PdfReader',)
root.geometry("600x780")
#root.title="Pdf Viewer"
pdfviewer = ShowPdf()

#pdf_load=input("input pdf file:\n>>")
pdf_load = filedialog.askopenfilename(parent=root,
                filetypes = (("PDF files","*.pdf"),("all files","*.*")))

pdf_file = open(pdf_load, 'rb')
pdf_reader = pypdf.PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)

#pdf_load="/Users/allen/Documents/2023ZZshStudy/中正高中101歷史作業-大甲西社事件.pdf"


#pdf_load=filename

# Add your pdf location and width and height.
pdfframe = pdfviewer.pdf_view(root, pdf_location=pdf_load, width=80, height=50)
pdfframe.pack()

print(num_pages)

Button(root, text="Turn to first page", command=lambda: pdfviewer.goto(1)).pack()
Button(root, text="Turn to last page", command=lambda: pdfviewer.goto(num_pages)).pack()

pdf_file.close()
root.mainloop()