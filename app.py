import os
from pypdf import PdfReader, PdfWriter

# Folder containing the original PDFs
input_folder = r"C:\Users\USER\Downloads\Zone 5 Demand"  # Change this

# Folder where last-page PDFs will be saved
output_folder = r"C:\Users\USER\Downloads\Zone 5 Demand\lastpage"  # Change this

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pdf"):
        input_path = os.path.join(input_folder, filename)

        try:
            reader = PdfReader(input_path)

            if len(reader.pages) == 0:
                print(f"Skipped (empty): {filename}")
                continue

            writer = PdfWriter()
            writer.add_page(reader.pages[-1])

            # Save with "_LastPage" appended to the filename
            output_name = os.path.splitext(filename)[0] + "_LastPage.pdf"
            output_path = os.path.join(output_folder, output_name)

            with open(output_path, "wb") as output_file:
                writer.write(output_file)

            print(f"Created: {output_name}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("\nDone! All last-page PDFs have been created.")