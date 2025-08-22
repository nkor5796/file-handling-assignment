

def read_and_modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, "r") as f:
            lines = f.readlines()

        # Modify content (line numbers + uppercase)
        modified_lines = []
        for i, line in enumerate(lines, start=1):
            modified_lines.append(f"{i}: {line.strip().upper()}\n")

        # Write modified content to the output file
        with open(output_file, "w") as f:
            f.writelines(modified_lines)

        print(f"✅ File '{input_file}' was successfully read and modified.")
        print(f"✅ New file created: '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when accessing '{input_file}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Main Program
if __name__ == "__main__":
    # Ask the user for a filename
    filename = input("Enter the name of the file to read: ")
    output_filename = "modified_" + filename  # New file name

    read_and_modify_file(filename, output_filename)
