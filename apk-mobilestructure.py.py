#!/usr/bin/env python3
"""
Project Directory Builder for Flutter and Android Projects

This script creates a standard directory structure for Flutter and Android projects.
It asks for user input for project name and type, then generates the appropriate structure.

Usage:
    python create_project_structure.py
"""

import os
import shutil
import logging
import datetime
import sys
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("project_builder_log.txt"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class ProjectBuilder:
    """Class to create standard project structures for Flutter and Android projects."""

    def __init__(self, project_type, project_name, output_dir=None):
        """
        Initialize the project builder.
        
        Args:
            project_type (str): Type of project ('flutter' or 'android')
            project_name (str): Name of the project
            output_dir (str, optional): Directory to create the project in. Defaults to current directory.
        """
        self.project_type = project_type.lower()
        self.project_name = project_name
        
        # Sanitize project name for directory
        self.sanitized_name = self.project_name.replace(' ', '_').lower()
        
        # Set project path
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            self.output_dir = Path.cwd()
        
        self.project_path = self.output_dir / self.sanitized_name
        self.project_description = f"A new {self.project_type.capitalize()} project."
        
        # Validate project type
        if self.project_type not in ["flutter", "android"]:
            logger.error(f"Unsupported project type: {self.project_type}. Use 'flutter' or 'android'.")
            sys.exit(1)
        
        logger.info(f"Initializing builder for {self.project_type} project: {self.project_name}")

    def ensure_directory_exists(self, directory):
        """Ensure a directory exists, create it if it doesn't."""
        dir_path = self.project_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True)
            logger.info(f"Created directory: {dir_path}")
        return dir_path

    def create_flutter_structure(self):
        """Create standard structure for Flutter projects."""
        # Essential directories
        self.ensure_directory_exists("lib")
        self.ensure_directory_exists("lib/models")
        self.ensure_directory_exists("lib/providers")
        self.ensure_directory_exists("lib/screens")
        self.ensure_directory_exists("lib/widgets")
        self.ensure_directory_exists("lib/utils")
        self.ensure_directory_exists("lib/services")
        
        # Asset directories
        self.ensure_directory_exists("assets")
        self.ensure_directory_exists("assets/images")
        self.ensure_directory_exists("assets/fonts")
        self.ensure_directory_exists("assets/icons")
        
        # Test directories
        self.ensure_directory_exists("test")
        self.ensure_directory_exists("test/unit_test")
        self.ensure_directory_exists("test/widget_test")
        self.ensure_directory_exists("test/integration_test")
        
        # Platform-specific directories
        self.ensure_directory_exists("android")
        self.ensure_directory_exists("ios")
        self.ensure_directory_exists("web")
        
        # GitHub directories
        self.ensure_directory_exists(".github/workflows")
        
        # Scripts directory
        self.ensure_directory_exists("scripts")
        
        # Create basic main.dart
        main_dart_path = self.project_path / "lib" / "main.dart"
        with open(main_dart_path, 'w') as f:
            f.write("""import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '${self.project_name}',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: '${self.project_name} Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
""")
        logger.info(f"Created basic main.dart file")
        
        # Create pubspec.yaml
        pubspec_path = self.project_path / "pubspec.yaml"
        with open(pubspec_path, 'w') as f:
            f.write(f"""name: {self.sanitized_name}
description: {self.project_description}
version: 0.1.0+1
publish_to: 'none'

environment:
  sdk: ">=2.17.0 <3.0.0"
  flutter: ">=2.10.0"

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.5
  provider: ^6.0.5
  http: ^0.13.5
  shared_preferences: ^2.0.15
  path_provider: ^2.0.11
  flutter_lints: ^2.0.1

dev_dependencies:
  flutter_test:
    sdk: flutter

flutter:
  uses-material-design: true
  
  assets:
    - assets/images/
    - assets/icons/
""")
        logger.info(f"Created pubspec.yaml")

    def create_android_structure(self):
        """Create standard structure for Android projects."""
        # Android app directories
        self.ensure_directory_exists("app")
        self.ensure_directory_exists("app/src")
        self.ensure_directory_exists("app/src/main")
        self.ensure_directory_exists("app/src/main/java")
        self.ensure_directory_exists("app/src/main/res")
        self.ensure_directory_exists("app/src/test")
        self.ensure_directory_exists("app/src/androidTest")
        
        # Common Android project directories
        self.ensure_directory_exists("gradle/wrapper")
        
        # Asset directories
        self.ensure_directory_exists("app/src/main/assets")
        self.ensure_directory_exists("app/src/main/res/drawable")
        self.ensure_directory_exists("app/src/main/res/layout")
        self.ensure_directory_exists("app/src/main/res/values")
        
        # GitHub directories
        self.ensure_directory_exists(".github/workflows")
        
        # Scripts directory
        self.ensure_directory_exists("scripts")
        
        # Create basic build.gradle
        build_gradle_path = self.project_path / "build.gradle"
        with open(build_gradle_path, 'w') as f:
            f.write("""// Top-level build file where you can add configuration options common to all sub-projects/modules.
buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:7.2.1'
        classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:1.7.10'

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
""")
        logger.info(f"Created build.gradle")
        
        # Create settings.gradle
        settings_gradle_path = self.project_path / "settings.gradle"
        with open(settings_gradle_path, 'w') as f:
            f.write(f"""rootProject.name = "{self.sanitized_name}"
include ':app'
""")
        logger.info(f"Created settings.gradle")

    def create_documentation_files(self):
        """Create standard documentation files."""
        # README.md
        readme_path = self.project_path / "README.md"
        with open(readme_path, 'w') as f:
            if self.project_type == "flutter":
                f.write(f"""# {self.project_name}

{self.project_description}

## Project Structure

- **lib/**: Contains the main source code
  - **models/**: Data models
  - **providers/**: State management
  - **screens/**: Main screen components
  - **widgets/**: Reusable UI components
  - **services/**: API and backend services
  - **utils/**: Utility functions and helpers
- **assets/**: Contains static resources
  - **images/**: App images
  - **fonts/**: Custom fonts
  - **icons/**: App icons
- **test/**: Testing directory
  - **unit_test/**: Unit tests
  - **widget_test/**: Widget tests
  - **integration_test/**: Integration tests

## Setup

1. Ensure Flutter is installed and set up on your machine
2. Clone this repository
3. Run `flutter pub get` to install dependencies
4. Run `flutter run` to start the app in debug mode
""")
            else:  # Android
                f.write(f"""# {self.project_name}

{self.project_description}

## Project Structure

- **app/src/main/**: Contains the main source code
  - **java/**: Java/Kotlin source files
  - **res/**: Resource files
    - **layout/**: UI layout files
    - **drawable/**: Images and drawables
    - **values/**: Strings, colors, and styles
  - **assets/**: Raw asset files
- **app/src/test/**: Unit tests
- **app/src/androidTest/**: Instrumentation tests

## Setup

1. Ensure Android Studio or appropriate development environment is set up
2. Clone this repository
3. Open the project in Android Studio
4. Sync Gradle and run the app
""")
        logger.info(f"Created README.md")
        
        # .gitignore
        gitignore_path = self.project_path / ".gitignore"
        with open(gitignore_path, 'w') as f:
            if self.project_type == "flutter":
                f.write("""# Miscellaneous
*.class
*.log
*.pyc
*.swp
.DS_Store
.atom/
.buildlog/
.history
.svn/
migrate_working_dir/

# IntelliJ related
*.iml
*.ipr
*.iws
.idea/

# VS Code related
.vscode/

# Flutter/Dart/Pub related
**/doc/api/
**/ios/Flutter/.last_build_id
.dart_tool/
.flutter-plugins
.flutter-plugins-dependencies
.packages
.pub-cache/
.pub/
/build/

# Symbolication related
app.*.symbols

# Obfuscation related
app.*.map.json

# Android Studio will place build artifacts here
/android/app/debug
/android/app/profile
/android/app/release
""")
            else:  # Android
                f.write("""# Built application files
*.apk
*.aar
*.ap_
*.aab

# Files for the ART/Dalvik VM
*.dex

# Java class files
*.class

# Generated files
bin/
gen/
out/

# Gradle files
.gradle/
build/

# Local configuration file (sdk path, etc)
local.properties

# Log Files
*.log

# Android Studio Navigation editor temp files
.navigation/

# Android Studio captures folder
captures/

# IntelliJ
*.iml
.idea/

# External native build folder generated in Android Studio 2.2 and later
.externalNativeBuild
.cxx/

# MacOS
.DS_Store
""")
        logger.info(f"Created .gitignore")

    def create_project(self):
        """Create the project structure."""
        try:
            # Create the project directory
            if self.project_path.exists():
                logger.warning(f"Directory {self.project_path} already exists. Files may be overwritten.")
            else:
                self.project_path.mkdir(parents=True)
                logger.info(f"Created project directory: {self.project_path}")
            
            # Create appropriate structure based on project type
            if self.project_type == "flutter":
                self.create_flutter_structure()
            elif self.project_type == "android":
                self.create_android_structure()
            
            # Create documentation files
            self.create_documentation_files()
            
            logger.info(f"Project creation complete! Your {self.project_type} project has been created at {self.project_path}")
            print(f"\nProject created successfully at {self.project_path}")
            
        except Exception as e:
            logger.error(f"An error occurred during project creation: {e}")
            import traceback
            logger.error(traceback.format_exc())
            print(f"Error creating project: {e}")
            sys.exit(1)


def get_user_input():
    """Get project details from user input."""
    print("===== Android/Flutter Project Directory Builder =====")
    
    # Get project name with validation
    while True:
        project_name = input("\nEnter project name: ").strip()
        if project_name:
            break
        print("Error: Project name cannot be empty.")
    
    # Get project type with validation
    while True:
        project_type = input("\nEnter project type (flutter/android): ").strip().lower()
        if project_type in ['flutter', 'android']:
            break
        print("Error: Project type must be 'flutter' or 'android'.")
    
    # Optional output directory
    output_dir = input("\nEnter output directory (press Enter for current directory): ").strip()
    if not output_dir:
        output_dir = None
    
    return project_name, project_type, output_dir


def main():
    """Main entry point for the script."""
    try:
        # Get user input
        project_name, project_type, output_dir = get_user_input()
        
        # Create project
        builder = ProjectBuilder(project_type, project_name, output_dir)
        builder.create_project()
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 