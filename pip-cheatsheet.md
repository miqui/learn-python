# Installing Packages
```
pip install <package_name>  
pip install <package_name>==<version>   
pip install -r requirements.txt 
```

# Upgrading Packages
```
pip install --upgrade <package_name>
pip list --outdated | cut -d ' ' -f 1  | xargs -n1 pip install -U
```
# Uninstalling Packages
```
pip uninstall <package_name>
```
# Listing Packages
```
pip list
pip list --outdated
pip freeze > requirements.txt
```

# Searching for Packages
```
pip search <search_term>
```
# Getting Package Information
```
pip show <package_name>
```
# Virtual Environments (recommended)
```
python -m venv <environment_name>  # Create environment
<environment_name>\Scripts\activate.bat  # Activate (Windows)
source <environment_name>/bin/activate  # Activate (macOS/Linux)
```
