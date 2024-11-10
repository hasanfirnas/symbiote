import os
import subprocess
import sys
import time
import importlib.util

# Loading bar for progress visualization
def loading_bar(iteration, total, prefix='', length=40):
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    percent = (100 * (iteration / total))
    sys.stdout.write(f'\r{prefix} |{bar}| {percent:.1f}% Complete')
    sys.stdout.flush()

# Execute shell command with error handling
def execute_command(command, description):
    try:
        print(f"\n{description}...")
        total_steps = 1
        for i in range(total_steps):
            loading_bar(i + 1, total_steps, description)
            subprocess.run(command, shell=True, check=True)
            time.sleep(1)  # Simulate processing time
        loading_bar(total_steps, total_steps, description)
        print("\nDone.")
    except subprocess.CalledProcessError as e:
        print(f"\nError occurred during {description}: {e}")

# Uninstall the dependencies
def uninstall_dependencies(dependencies):
    print("Removing existing packages...")
    for dep in dependencies:
        execute_command(f"sudo apt remove --purge -y {dep}", f"Removing {dep}")

# Check if a dependency is installed
def is_installed(dependency):
    return importlib.util.find_spec(dependency) is not None

# Install a dependency with error handling and verification
def install_dependency_with_prompt(dependency, message):
    proceed = input(f"\n{message} Do you want to proceed with installing {dependency}? (y/n): ")
    if proceed.lower() == 'y':
        execute_command(f"sudo apt install {dependency} -y", f"Installing {dependency}")
        if is_installed(dependency):
            print(f"{dependency} successfully installed.")
        else:
            print(f"Failed to install {dependency}.")
    else:
        print(f"Skipping {dependency} installation.")

# Thorough installation check
def check_installation(dependencies):
    print("\nChecking installation status of dependencies...")
    for dep, message in dependencies:
        if is_installed(dep):
            print(f"{dep} is installed.")
        else:
            print(f"{dep} is not installed.")

# Self-destruct: Uninstall everything in reverse order of installation
def self_destruct(dependencies):
    print("\nSelf-destruct sequence initiated...")
    for dep in reversed(dependencies):
        execute_command(f"sudo apt remove --purge -y {dep[0]}", f"Uninstalling {dep[0]}")
    print("All dependencies have been removed. Cleaning up...")

# Get user choice for installation type
def get_user_choice():
    print("\nChoose the installation type:")
    print("1. Fresh Install (removes all existing libraries)")
    print("2. Partial Reinstall (removes only specific libraries)")
    print("3. Full Reinstall (removes and reinstalls all libraries with user prompts)")
    print("4. Check Installation Status")
    print("5. Self-Destruct (Uninstall everything in reverse order)")
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
    return choice

# Main function
def main():
    dependencies = [
        ("python3-tk", "Installing tkinter..."),
        ("git", "Installing git..."),
        ("python3", "Installing Python..."),
        ("wget", "Installing wget..."),
        ("php", "Installing PHP..."),
        ("openssh-client", "Installing OpenSSH Client..."),
        ("jq", "Installing jq...")
    ]

    # Get user choice for installation type
    choice = get_user_choice()

    if choice == '1':
        uninstall_dependencies([dep[0] for dep in dependencies])
        for dep, message in dependencies:
            install_dependency_with_prompt(dep, message)
    elif choice == '2':
        partial_dependencies = [
            "python3",  # Only specify libraries you want to remove
            "git"
        ]
        uninstall_dependencies(partial_dependencies)
        for dep, message in dependencies:
            install_dependency_with_prompt(dep, message)
    elif choice == '3':
        uninstall_dependencies([dep[0] for dep in dependencies])
        for dep, message in dependencies:
            install_dependency_with_prompt(dep, message)  # Install each dependency with prompt
    elif choice == '4':
        check_installation(dependencies)
    elif choice == '5':
        confirmation = input("Are you sure you want to self-destruct and remove all installed dependencies? (y/n): ")
        if confirmation.lower() == 'y':
            self_destruct(dependencies)
        else:
            print("Self-destruct canceled.")
    else:
        print("Invalid choice. Exiting.")
        return

    # Ask user for the installation directory
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()  # Hide the root window
    install_dir = filedialog.askdirectory(title="Select Installation Directory")

    if not install_dir:
        print("Installation canceled.")
        return

    os.chdir(install_dir)

    # Commands to execute
    commands = [
        ("sudo ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa <<<y >/dev/null 2>&1", "Generating SSH key"),
        ("git clone https://github.com/hasanfirnas/symbiote", "Cloning symbiote repository"),
        ("cd symbiote && python3 symbiote.py", "Running symbiote.py")
    ]

    # Execute each command
    for command, description in commands:
        try:
            execute_command(command, description)
        except subprocess.CalledProcessError as e:
            print(f"\nError occurred: {e}")
            break

if __name__ == "__main__":
    main()
