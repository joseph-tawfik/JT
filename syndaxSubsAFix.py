import subprocess

# Base Java command
base_java_command_prefix = "java -jar VaultDataLoader.jar -move /SubmissionsArchive/IND064722/"
base_java_command_suffix = " /SubmissionsArchive/IND064722 -overwrite -username mig.admin@sb-syndax.com -dns https://sb-syndax-rim-sbx.veevavault.com -p mBxTkZ5L"

# Set the starting value for the incremental parameter
start_value = 143

# Set the number of times you want to run the Java command
num_iterations = 406

# Loop through the specified number of iterations
for i in range(num_iterations):
    # Incremental value for each iteration, padded with zeros
    incremental_value = str(start_value + i).zfill(4)

    # Construct the Java command for the current iteration
    current_java_command = f"{base_java_command_prefix}{incremental_value}/{incremental_value}{base_java_command_suffix}"

    try:
        # Run the Java command
        subprocess.run(current_java_command, shell=True, check=True)
        
        # Print a message indicating successful execution
        print(f"Iteration {incremental_value}: Java command executed successfully.")
    except subprocess.CalledProcessError as e:
        # Handle any errors that may occur during execution
        print(f"Error in iteration {incremental_value}: {e}")

print("Loop completed.")