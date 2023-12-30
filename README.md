# Skeeshup

## Overview

Utility to quickly startup your desktop on windows 10. 
Software downloads and installs manually by the given references to download from.
Software list by SKEESH.
Built-in tweaks and other operating systems featured soon.

## Setup

### Requirements

1. python3.11

### Installation

Clone the repository:

```bash
git clone https://github.com/skeesh24/skeeshup.git
```

### Install dependencies:

```bash
python3.11 -m venv venv && venv/Script/activate && pip install -r requirements.txt
```

## Environment

Create an .env file to set the application configuration. You need to add the following fields to it:

1. "CONFIGURATION_PATH" to specify the location of the configuration.json file
2. "PACKAGE" is used by the logger as the name of the main package
3. "SYNC" to select whether the configuration method is local (LOCAL) or cloud-based (REMOTE) 4. "TEMP_FOLDER" to specify the name of a folder in Local/Temp dir to store downloaded files
4. "MONGO_USER" secret data for accessing the mongodb instance (profile name)
5. "MONGO_HOST" secret data for accessing the mongodb instance (uri to locate db)
6. "MONGO_DATABASE" secret data to access the mongodb instance (database name)
7. "MONGO_COLLECTION" secret data to access the mongodb instance (collection name)
8. "MONGO_PASSWORD" secret data for accessing the mongodb instance (password to access db)

## Configuration

Method 1: Configuration JSON File

Navigate to the root directory.
Modify the configuration.json file according to your preferences. Ensure to fill in the required fields such as:
1. DOWNLOAD_ARGS [] - list of references to install
Save the changes.

Method 2: MongoDB Document

Access your MongoDB instance.
Locate the relevant collection/document for configuration (e.g., config collection).
Update the necessary fields within the document to match your configuration requirements.
Save the changes.

## Running the Software

1. Navigate to the root directory.
2. Specify the references to download from. 
3. Execute the software:
```bash
venv/Script/python src/main.py
```
