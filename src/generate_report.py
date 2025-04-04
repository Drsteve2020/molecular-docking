from fpdf import FPDF

class DockingReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Molecular Docking Parameters Explanation', 0, 1, 'C')
        
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', True)
        self.ln(4)
        
    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 5, body)
        self.ln()

def create_docking_report():
    pdf = DockingReport()
    pdf.add_page()
    
    # Binding Energy Parameters
    pdf.chapter_title("Binding Score")
    pdf.chapter_body("The overall binding affinity between the ligand and receptor. More negative values indicate stronger binding. Measured in kcal/mol.")
    
    pdf.chapter_title("Energy Components")
    
    components = {
        "Van der Waals (vdW) Energy": 
            "Non-covalent interactions between atoms. Important for shape complementarity. Typically ranges from -5 to -1 kcal/mol.",
            
        "Electrostatic Energy":
            "Charge-based interactions between molecules. Critical for ionic and polar interactions. Usually ranges from -3 to -0.5 kcal/mol.",
            
        "Hydrogen Bonds":
            "Specific type of electrostatic interaction between H-bond donors and acceptors. Typically contributes -2 to -0.2 kcal/mol per bond.",
            
        "Desolvation Energy":
            "Energy required to remove water molecules from binding interface. Can be positive or negative.",
            
        "Pi-stacking":
            "Interactions between aromatic rings. Important for drug-receptor binding. Usually ranges from -2 to -0.1 kcal/mol.",
            
        "Hydrophobic Interactions":
            "Favorable interactions between non-polar regions. Typically ranges from -3 to -0.3 kcal/mol.",
            
        "Entropy":
            "Measure of system disorder change upon binding. Can be positive (unfavorable) or negative (favorable)."
    }
    
    for title, body in components.items():
        pdf.chapter_body(f"{title}:\n{body}\n")
    
    pdf.add_page()
    pdf.chapter_title("Molecular Properties")
    
    properties = {
        "Molecular Weight (MW)":
            "Mass of the molecule in g/mol. Important for drug-likeness (typically < 500 for good oral bioavailability).",
            
        "LogP":
            "Measure of lipophilicity (fat solubility). Affects drug absorption and distribution. Optimal range: 0-5.",
            
        "Topological Polar Surface Area (TPSA)":
            "Surface area of all polar atoms. Predicts drug absorption, including blood-brain barrier penetration. Optimal: <140 A^2.",
            
        "Hydrogen Bond Donors (HBD)":
            "Number of -OH and -NH groups. Affects drug absorption. Should be <= 5 for good oral bioavailability.",
            
        "Hydrogen Bond Acceptors (HBA)":
            "Number of oxygen and nitrogen atoms. Should be <= 10 for good oral bioavailability.",
            
        "Rotatable Bonds":
            "Number of flexible bonds. Affects binding entropy and oral bioavailability. Optimal: <= 10."
    }
    
    for title, body in properties.items():
        pdf.chapter_body(f"{title}:\n{body}\n")
    
    pdf.output("data/docking_parameters_explanation.pdf")

if __name__ == "__main__":
    create_docking_report()