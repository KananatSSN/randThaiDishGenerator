def remove_duplicates_from_file(filename):
    """
    Remove duplicates from a text file
    """
    try:
        # Read all lines
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Remove duplicates while preserving order
        seen = set()
        unique_lines = []
        
        for line in lines:
            cleaned_line = line.strip()  # Remove whitespace
            if cleaned_line and cleaned_line not in seen:
                seen.add(cleaned_line)
                unique_lines.append(line)  # Keep original formatting
        
        # Write back to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(unique_lines)
        
        print(f"Removed {len(lines) - len(unique_lines)} duplicates from {filename}")
        print(f"File now contains {len(unique_lines)} unique words")
        
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
    except Exception as e:
        print(f"Error: {e}")

# Usage
if __name__ == "__main__":
    remove_duplicates_from_file('dish.txt')