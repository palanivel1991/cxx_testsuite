import subprocess
import os

def compile_with_make():
    try:
        # Run the make command
        result = subprocess.run(
            ["make"],  # Command to execute
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE,  # Capture standard error
            text=True,  # Output as text
            check=True  # Raise an exception if the command fails
        )

        # Print success message and output
        print("Compilation Successful!")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # Print error message and output
        print("Compilation Failed!")
        print("Error:", e.stderr)

if __name__ == "__main__":
    # Ensure the script runs in the repository's root directory
    if os.path.exists("Makefile"):
        compile_with_make()
    else:
        print("Makefile not found in the current directory.")
