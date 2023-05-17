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


root = Tk(className='python-PdfReader')
root.geometry("600x780")

pdf_file = None
pdf_reader = None
num_pages = 0
pdfviewer = None
pdfframe = None
load_pdf_btn = None
close_pdf_btn = None
pdf_open = False

def load_pdf():
    global pdfviewer
    global pdfframe
    global pdf_file
    global pdf_reader
    global num_pages
    global pdf_open
    global load_pdf_btn
    global close_pdf_btn

    if pdf_open:
        return

    # 選擇 PDF
    pdf_load = filedialog.askopenfilename(parent=root, filetypes=[("PDF files", "*.pdf"), ("all files", "*.*")])

    pdf_open = True

    if pdf_file:
        pdf_file.close()
    if pdfframe:
        pdfframe.destroy()

    # 讀取PDF
    pdf_file = open(pdf_load, 'rb')
    pdf_reader = pypdf.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    pdfviewer = ShowPdf()
    pdfframe = pdfviewer.pdf_view(root, pdf_location=pdf_load, width=80, height=50)
    pdfframe.pack()

    load_pdf_btn.config(state="normal")
    close_pdf_btn.config(state="normal")

def close_pdf():
    global pdf_file
    global pdfframe
    global pdf_open
    global load_pdf_btn
    global close_pdf_btn

    pdf_open = False

    if pdf_file:
        pdf_file.close()
    if pdfframe:
        pdfframe.destroy()

    close_pdf_btn.config(state="disabled")

    load_pdf_btn.config(state="normal")

# 建立按鈕
load_pdf_btn = Button(root, text="Load PDF file", command=load_pdf)
load_pdf_btn.pack()

close_pdf_btn = Button(root, text="Close PDF file", command=close_pdf)
close_pdf_btn.pack()
close_pdf_btn.config(state="disabled")

Button(root, text="Turn to first page", command=lambda: pdfviewer.goto(1)).pack()
Button(root, text="Turn to last page", command=lambda: pdfviewer.goto(num_pages)).pack()

pdf_open = False

root.mainloop()
