# Terragrunt New Package Onboarding  

## Overview  
the script will create a new package in the terragrunt directory, according to best practices.
```config.yaml``` will includes the following:   

- AWS Accounts (list)   
- AWS Regions (list)   
- AWS Environments (list)   
- terragrunt config (dict)

## Usage  
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python script.py
```
