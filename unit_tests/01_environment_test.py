import sys
import os
import subprocess

def check_python_version():
    version = sys.version_info
    if version.major == 3 and version.minor >= 6:
        return True, f"Python version is {version.major}.{version.minor}.{version.micro}"
    else:
        return False, f"Python version is {version.major}.{version.minor}.{version.micro}. Python 3.6+ is required."

def check_project_structure():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    plant_care_dir = os.path.join(base_dir, 'plant_care_dashboard')
    backend_dir = os.path.join(plant_care_dir, 'backend')
    frontend_dir = os.path.join(plant_care_dir, 'frontend')
    missing = []
    if not os.path.isdir(plant_care_dir):
        missing.append("plant_care_dashboard directory is missing")
    if not os.path.isdir(backend_dir):
        missing.append("backend directory is missing inside plant_care_dashboard")
    if not os.path.isdir(frontend_dir):
        missing.append("frontend directory is missing inside plant_care_dashboard")
    if missing:
        return False, "; ".join(missing)
    return True, "Project directory structure is correct"

def check_virtualenv():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    venv_path = os.path.join(base_dir, 'plant_care_dashboard', 'backend', 'venv')
    if not os.path.isdir(venv_path):
        return False, "Python virtual environment directory 'venv' is missing in backend"
    # Check if pip exists in venv
    pip_path = os.path.join(venv_path, 'bin', 'pip')
    if not os.path.isfile(pip_path):
        return False, "pip executable is missing in the virtual environment"
    return True, "Python virtual environment is set up correctly"

def check_flask_installation():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    pip_path = os.path.join(base_dir, 'plant_care_dashboard', 'backend', 'venv', 'bin', 'pip')
    try:
        result = subprocess.run([pip_path, 'show', 'Flask'], capture_output=True, text=True)
        if "Name: Flask" in result.stdout:
            return True, "Flask is installed in the virtual environment"
        else:
            return False, "Flask is not installed in the virtual environment"
    except Exception as e:
        return False, f"Error checking Flask installation: {str(e)}"

def check_flask_sqlalchemy_installation():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    pip_path = os.path.join(base_dir, 'plant_care_dashboard', 'backend', 'venv', 'bin', 'pip')
    try:
        result = subprocess.run([pip_path, 'show', 'Flask-SQLAlchemy'], capture_output=True, text=True)
        if "Name: Flask-SQLAlchemy" in result.stdout:
            return True, "Flask-SQLAlchemy is installed in the virtual environment"
        else:
            return False, "Flask-SQLAlchemy is not installed in the virtual environment"
    except Exception as e:
        return False, f"Error checking Flask-SQLAlchemy installation: {str(e)}"

def main():
    checks = [
        ("Python Version", check_python_version),
        ("Project Structure", check_project_structure),
        ("Virtual Environment", check_virtualenv),
        ("Flask Installation", check_flask_installation),
        ("Flask-SQLAlchemy Installation", check_flask_sqlalchemy_installation),
    ]

    all_passed = True
    for name, check_func in checks:
        passed, message = check_func()
        if passed:
            print(f"[PASS] {name}: {message}")
        else:
            print(f"[FAIL] {name}: {message}")
            all_passed = False

    if all_passed:
        print("\nEnvironment setup is correct.")
    else:
        print("\nEnvironment setup has issues. Please address the above failures.")

if __name__ == "__main__":
    main()
