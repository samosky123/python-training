# Duration: 4 Days
# Course Learning Objectives:

* Understanding of language data types and methods
* Ability to write simple scripts
* Ability to understand complex scripts
* Appreciation of Object Orientated Programming
* Install and use modules to interact with network devices
* ACI programming examples

# Itinerary

## Introduction

* Why Python for Network Automation
* Python Tools for Networking Engineers

* IPython
* Pycharm
* PIP

* Exploring the interactive shell

## Python Fundamentals

* Data Types and Objects
* Using REST to communicate with Network Devices and Tools
* Parsing data returned from the Network
* Manipulating the network
* Writing Parsed Data
* Reading Data
* The essentials of Flow Control and dealing with exceptions.
* Increase the functionality of the Core Python Runtime with Import.


## Python Modules for the Network Engineer
### Parsing Data

Most Network devices/Tools will return and accept data in a serialised data format, the most common of which are XML and JSON.

* json
* xmltodict
* pyYAML
* ipaddr

### Connecting to the Network

Connectivity to networking devices is almost exclusively through SSH, therefore a robust SSH programming environment is required.
Most API calls to either orchestration platforms and networking devices (although not exclusively) are made through REST (Representational State Transfer).  An understanding of REST operations and the ability to program against it is an essential requirement of the Network Engineers toolbox.

* paramiko
* netmiko
* requests

### Storing Data/Retrieving Data

* openpyxl
* pymongo
* argparse

### Templates

* jinja2

## Optional Topics

### Cisco ACI
* Exploring the ACI Object Model with Visore (Object Browser)
* Easily create new API calls to ACI with API inspector
* Querying and configuring ACI using REST from Python scripts

### NetConf/YANG
* Why NetConf/YANG - A paradigm shift in Network Management
* What is a Data Model – Explain the YANG Data Model (rfc6020) and why Data models are important
* YANG Explorer – a DevOp tool for exploring models and coding against them
* NetConf Operation – The mechanics of the NetConf protocol
* Ncclient – Enable device level operation of NetConf from your Python script
* NSO – An introduction to Network Service Orchestration – A tool for creating and deploying YANG Service Models.
* NSO use cases – Demonstrate the power of NSO.

### Arista
* Query and configure Arista switches using EAPI.
* Using Cloud Vision Portal (CVP) API

### Ansible
* Basic priciples
* Playbooks, tasks, modules, variables, templates

