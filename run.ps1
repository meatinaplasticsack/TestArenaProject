# Get the version of Python installed 
Write-Host "Python Version:"
python --version

# Get the version of Python PIP installed 
Write-Host "PIP Version:"
pip --version

# Update the version of Python PIP 
Write-Host "Updating PIP..."
python -m pip install --upgrade pip

# Create virtual environment
Write-Host "Creating virtual environment..."
python -m venv .venv

# Activate virtual environment
Write-Host "Activating virtual environment..."
.venv\Scripts\Activate.ps1  # Use .ps1 extension for PowerShell

# Installing dependencies in virtual environment
Write-Host "Installing dependencies..."
try {
    pip install -r .\requirements.txt
}
catch {
    Write-Error "Error installing requirements: $_"
    exit 1  # Exit with an error code
}

# Running only tests marked as smoke.
Write-Host "Running smoke tests..."
pytest -s -v -m "smoke" --html .\reports\report.html

# Running only tests marked as regression. Uncomment to run.
# Write-Host "Running regression tests..."
# pytest -s -v -m "regression" --html .\reports\report.html

# Running all tests. Uncomment to run.
# Write-Host "Running all tests..."
# pytest -s -v -m "smoke and regression" --html .\reports\report.html


# Deactivate virtual environment
Write-Host "Deactivating virtual environment..."
deactivate