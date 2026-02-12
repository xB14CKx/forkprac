import os
import subprocess
import sys
import platform

def run(command, cwd=None):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd)
    if result.returncode != 0:
        sys.exit(result.returncode)

def create_venv():
    print("\nSetting up Python virtual environment...")
    venv_path = os.path.join("api", ".venv")

    if not os.path.exists(venv_path):
        run([sys.executable, "-m", "venv", venv_path])
    else:
        print("Virtual environment already exists.")

    # Determine activation path
    if platform.system() == "Windows":
        python_exec = os.path.join(venv_path, "Scripts", "python.exe")
    else:
        python_exec = os.path.join(venv_path, "bin", "python")

    requirements = os.path.join("api", "requirements.txt")
    if os.path.exists(requirements):
        run([python_exec, "-m", "pip", "install", "-r", requirements])
    else:
        print("No requirements.txt found.")

def install_frontend():
    print("\nInstalling frontend dependencies...")
    if os.path.exists("frontend/package.json"):
        run(["npm", "install"], cwd="frontend")
    else:
        print("No frontend found.")

def main():
    print("====================================")
    print(" Project Setup Script")
    print("====================================")

    if not os.path.exists("api") or not os.path.exists("frontend"):
        print("Error: Run this from the project root directory.")
        sys.exit(1)

    create_venv()
    install_frontend()

    print("\nSetup complete!")
    print("\nTo run the project:")
    if platform.system() == "Windows":
        print("Backend:")
        print("  api\\.venv\\Scripts\\activate")
        print("  uvicorn main:app --reload")
    else:
        print("Backend:")
        print("  source api/.venv/bin/activate")
        print("  uvicorn main:app --reload")

    print("\nFrontend:")
    print("  cd frontend && npm run dev")

if __name__ == "__main__":
    main()

