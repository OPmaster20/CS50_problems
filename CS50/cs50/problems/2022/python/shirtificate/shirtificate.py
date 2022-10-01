from fpdf import FPDF
class PDF(FPDF):
    def __init__(self,name):
        if not name:
            raise ValueError("Invalid name")
        self.name=name
        self.image('shirtificate.png')
    def c_pdf(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font("helvetica", "B", 16)
        pdf.cell(40, 10, f"{self.name} took cs50")
        pdf.output("test1.pdf")

def main():
    get_name=input("Name: ")
    fg=FPDF(get_name)
if __name__=='__main__':
    main()