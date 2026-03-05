$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $projectRoot

if (!(Test-Path "requirements.txt")) {
    throw "requirements.txt not found in $projectRoot"
}

if (Test-Path ".venv") {
    try {
        Remove-Item -Recurse -Force ".venv"
    }
    catch {
        Write-Warning "Could not delete .venv (possibly locked by OneDrive or permissions). Continuing."
    }
}

py -m venv .venv

& ".\.venv\Scripts\Activate.ps1"

python -m pip install --upgrade pip
pip install -r requirements.txt
python -m pytest -q
