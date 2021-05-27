**### This is a README file for Implementation Details for coding question asked and comments are in line to the questions below.
**
# Bond Challenge

## Coding Question

Write an interface for a data structure that can provide the moving average of the last N elements added, add elements to the structure and get access to the elements. Provide an efficient implementation of the interface for the data structure.

For your submission, please submit a PR to the `main` branch of this repository.

### Minimum Requirements

1. Provide a separate interface (i.e. `interface`/`trait`) with documentation for the data structure
### Sangeetha:
   detailed Comments are updated in the code (elements-watcher.py) to go over the interface or data structure. Please review.

2. Provide an implementation for the interface
### Sangeetha:
   below are the implementation details:
   
   a. Deploy to Azure
      Prerequisites:
      Install Python 3.6+
      Install Functions Core Tools
      Install Docker
      Steps:
      Deploy through Azure CLI
      Open AZ CLI and run az group create -l [region] -n [resourceGroupName] to create a resource group in your Azure subscription (i.e. [region] could be westus2, eastus,       etc.)
      Run az group deployment create --name [deploymentName] --resource-group [resourceGroupName] --template-file azuredeploy.json

   b. Deploy Function App
      elements-watcher.py contains a main() Python function that's triggered according to the configuration in function.json.
      Create supporting Azure resources for this function to run:
      sign in to Azure: az login
      Create a resource group named AzureFunctionsTest-rg in the lets say canada-central region:
      az group create --name AzureFunctionsTest-rg --location canadacentral
      Create a general-purpose storage account in your resource group and region:
      az storage account create --name TestSTA --location canadacentral --resource-group AzureFunctionsTest-rg --sku Standard_LRS
      Create the function app in Azure: az functionapp create --resource-group AzureFunctionsTest-rg --consumption-plan-location canadacentral --runtime python --runtime-version 3.8 --functions-version 3 --name elements-watcher --storage-account TestSTA --os-type linux
      Deploy the function project to Azure:
      func azure functionapp publish elements-watcher
      Invoke the function on Azure:
      Copy the complete Invoke URL shown in the output of the publish command into a browser address bar, appending the query parameter &name=Functions. or run curl command      for the same.
      Run func azure functionapp publish elements-watcher --build-native-deps

   c. Test:
       Copy the complete Invoke URL shown in the output of the publish command into a browser address bar, appending the query parameter &name=Functions. or run curl comman      d for the same.  Watch event grid trigger the elements-watcher function and produce its content on streaming logs and same is available in application insights. or we      can write to a file as well.
      Another implementation can be done as below for this function app in azure:
      Configure Event grid to trigger this function app so that events are captured by function app and processed, emitted as the desired output like file or in applicatio       insights.
      for this, Upload test.csv file into c1raw container.
      Watch event grid trigger the elements-watcher function and produce its content on streaming logs and same is available in application insights. or we can write to a f      ile as well.

3. Provide any additional explanation about the interface and implementation in a README file.
### Sangeetha:
   Yes, README file is updated.
   
