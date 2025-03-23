#!/usr/bin/env python3
"""
Requirements Installer for APK-MobileStructure

This script checks and installs any required dependencies for the APK-MobileStructure tool.
Since the tool primarily uses standard libraries, this script mainly validates
the Python version and ensures a proper environment.

Run with: python requirements.py
"""

import sys
import os
import subprocess
import platform

def check_python_version():
    """Check if Python version is compatible (3.6+)"""
    print("Checking Python version...")
    
    if sys.version_info < (3, 6):
        print("ERROR: APK-MobileStructure requires Python 3.6 or newer")
        print(f"Current Python version: {platform.python_version()}")
        print("Please update your Python installation.")
        return False
    
    print(f"✓ Python version OK: {platform.python_version()}")
    return True

def ensure_executable_permissions():
    """Ensure the main script is executable on Unix-based systems"""
    if os.name != 'nt':  # Not Windows
        print("Setting executable permissions on scripts...")
        
        try:
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'project_standardizer.py')
            if os.path.exists(script_path):
                os.chmod(script_path, 0o755)
                print(f"✓ Set executable permissions on {script_path}")
            else:
                print(f"! Warning: Could not find {script_path}")
        except Exception as e:
            print(f"! Warning: Could not set executable permissions: {e}")

def check_optional_deps():
    """Check for optional dependencies and offer to install them"""
    try:
        import colorama
        print("✓ colorama module found (optional, for colored console output)")
    except ImportError:
        choice = input("Optional: Install colorama for colored console output? (y/n): ")
        if choice.lower() == 'y':
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
                print("✓ colorama installed successfully")
            except Exception as e:
                print(f"! Warning: Could not install colorama: {e}")
                print("This is optional and won't affect core functionality.")

def create_test_environment():
    """Offer to create a test sample project"""
    choice = input("\nWould you like to create a sample test directory to try APK-MobileStructure? (y/n): ")
    if choice.lower() == 'y':
        test_dir = input("Enter a path for the test directory (or press Enter for './test_project'): ")
        if not test_dir:
            test_dir = './test_project'
        
        try:
            if not os.path.exists(test_dir):
                os.makedirs(test_dir)
            
            # Create a basic messy structure for demo purposes
            if not os.path.exists(os.path.join(test_dir, 'nested_project')):
                os.makedirs(os.path.join(test_dir, 'nested_project'))
            
            # For Flutter demo
            if not os.path.exists(os.path.join(test_dir, 'nested_project', 'lib')):
                os.makedirs(os.path.join(test_dir, 'nested_project', 'lib'))
                with open(os.path.join(test_dir, 'nested_project', 'pubspec.yaml'), 'w') as f:
                    f.write("name: test_app\ndescription: A test Flutter application.\n")
                with open(os.path.join(test_dir, 'nested_project', 'lib', 'main.dart'), 'w') as f:
                    f.write("void main() {\n  print('Hello, world!');\n}\n")
            
            print(f"\n✓ Created test directory at {test_dir}")
            print("You can use it as follows:")
            print(f"  python project_standardizer.py --type flutter --path {test_dir}")
        except Exception as e:
            print(f"! Error creating test environment: {e}")

def main():
    """Main function to check and install dependencies"""
    print("==================================================")
    print("APK-MobileStructure - Setup and Requirements Installer")
    print("==================================================\n")
    
    # Validate environment
    if not check_python_version():
        sys.exit(1)
    
    # No external dependencies are required, as the tool uses only standard libraries
    print("\n✓ All required dependencies are satisfied (uses standard libraries)")
    
    # Set permissions
    ensure_executable_permissions()
    
    # Check optional improvements
    check_optional_deps()
    
    # Offer to create test environment
    create_test_environment()
    
    print("\n✅ Setup complete! APK-MobileStructure is ready to use.")
    print("   Usage: python project_standardizer.py --type [flutter|android] --path [project_path]")
    print("==================================================")

if __name__ == "__main__":
    main() 