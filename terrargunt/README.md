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

## Example
```
live
├── non-prod
│   ├── account.yaml
│   ├── eu-west-1
│   │   ├── dev
│   │   │   └── env.yaml
│   │   ├── prod
│   │   │   └── env.yaml
│   │   ├── region.yaml
│   │   └── stg
│   │       └── env.yaml
│   └── us-east-1
│       ├── dev
│       │   └── env.yaml
│       ├── prod
│       │   └── env.yaml
│       ├── region.yaml
│       └── stg
│           └── env.yaml
├── prod
│   ├── account.yaml
│   ├── eu-west-1
│   │   ├── dev
│   │   │   └── env.yaml
│   │   ├── prod
│   │   │   └── env.yaml
│   │   ├── region.yaml
│   │   └── stg
│   │       └── env.yaml
│   └── us-east-1
│       ├── dev
│       │   └── env.yaml
│       ├── prod
│       │   └── env.yaml
│       ├── region.yaml
│       └── stg
│           └── env.yaml
├── staging
│   ├── account.yaml
│   ├── eu-west-1
│   │   ├── dev
│   │   │   └── env.yaml
│   │   ├── prod
│   │   │   └── env.yaml
│   │   ├── region.yaml
│   │   └── stg
│   │       └── env.yaml
│   └── us-east-1
│       ├── dev
│       │   └── env.yaml
│       ├── prod
│       │   └── env.yaml
│       ├── region.yaml
│       └── stg
│           └── env.yaml
└── terragrunt.hcl
```