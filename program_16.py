
import traceback

# Custom exception hierarchy
class FileProcessingError(Exception):
    """Base exception for file processing errors."""
    pass

class InvalidFileFormatError(FileProcessingError):
    """Raised when file format is invalid."""
    pass

class EmptyFileError(FileProcessingError):
    """Raised when the file is empty."""
    pass


def process_file(filename):
    file = None

    try:
        # Open the file
        file = open(filename, "r")

        print("File opened successfully.")

        # Read file contents
        data = file.read()

        if not data.strip():
            raise EmptyFileError("The file is empty.")

        if not filename.endswith(".txt"):
            raise InvalidFileFormatError(
                "Invalid file format. Only .txt files are allowed."
            )

    except FileNotFoundError:
        print("Error: File not found.")

    except InvalidFileFormatError as e:
        print("Format Error:", e)
        print("Traceback:")
        traceback.print_exc()

    except EmptyFileError as e:
        print("Empty File Error:", e)
        traceback.print_exc()

    except Exception as e:
        print("Unexpected Error:", e)
        traceback.print_exc()

    else:
        print("\nFile processed successfully!")
        print("File Contents:")
        print(data)

    finally:
        if file is not None:
            file.close()
            print("\nFile closed safely.")
        else:
            print("\nNo open file to close.")


# Main program
filename = input("Enter file name: ")
process_file(filename)
