# QC Machine Learning



## Requirements

- [ ] In requirements.txt
- [ ] Other
    - [ ] PortableGit or Git installed
    - [ ] MUST be on VPN

## Clone and Configure (using Git)

```
>>> git clone https://gccode.ssc-spc.gc.ca/harschnena/qc-machine-learning
```

## Set Up

create a virtual environment and download the necessary libraries
Note: if you are using PortableGit, in order to be able to pip install you need to open the command prompt git-cmd.exe

```
>>> cd qc-machine-learning
>>> py -3 -m venv {name of your venv}
>>> cd {name of your venv}
>>> cd Scripts
>>> activate.bat
>>> # install all the libraries from requirements.txt
>>> pip install -r requirements.txt

```

## Confirming Installation
You can make use of pip freeze to see what libraries you have installed in your virtual environment
If using PortableGit, in order to be able to pip you need to open the command prompt git-cmd.exe

```
>>> cd qc-machine-learning
>>> cd {name of your venv}
>>> cd Scripts
>>> activate.bat
>>> cat pip freeze 
```


## Files Included
- [ ] Generate
    - [ ] Generates data query, model building, and predictions
- [ ] Query
    - [ ] Handles all the data query from ARKEON
- [ ] Add Elements
    - [ ] Uses Query to get the data based on station, year, month, date, meas given
- [ ] Model
    - [ ] Handles everything that relates to the machine learning model
- [ ] Other: Accuracy
    - [ ] Pulled information from the phase 3 pivot tables
- [ ] requirements.txt
    - [ ] The library requirements to be imported
- [ ] SOG_model_x.joblib
    - [ ] These are the different models that can be imported to make predictions
- [ ] Excel files
    - [ ] Examples of Phase 3 and Phase 4&5
- [ ] SOG_Analysis
    - [ ] The analysis of the different models

## How to Run
- [ ] With Python
```
>>> cd qc-machine-learning
>>> cd {name of the venv}
>>> cd Scripts
>>> activate.bat
>>> # You can verify that the virtual environment is running by seeing (.venv) in front of your command line
>>> cd ..
>>> cd ..
>>> py Generate.py
>>> # Once done, deactivate the venv. You can verify that the virtual environment is not running by not seeing (.venv) in front of your command line
>>> cd {name of the venv}
>>> cd Scripts
>>> deactivate.bat
```
