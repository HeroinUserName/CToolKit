# CToolKit

This script is a modular project designed to demonstrate core cybersecurity concepts such as encryption, access control, and threat detection in multiple programming languages. It loads configuration from a JSON file and runs specific scripts depending on the category (encryption, access control, or threat detection) and the programming language specified in the configuration file.

The project structure is organized into various folders for each category, containing language-specific implementations of these concepts. The main script serves as the entry point, calling the necessary scripts based on the configuration.


# Project Structure:

CToolKit
├── encryption
│   ├── python
│   │   └── aes_cbc.py
│   ├── cpp
│   │   └── rsa_encryption.cpp
│   ├── javascript
│   │   └── aes_gcm.js
│   └── go
│       └── xchacha20.go
├── access_control
│   ├── python
│   │   └── rbac.py
│   ├── java
│   │   └── oauth2_example.java
│   ├── php
│   │   └── session_auth.php
│   └── csharp
│       └── api_key_authentication.cs
├── threat_detection
│   ├── python
│   │   └── intrusion_detection.py
│   ├── java
│   │   └── anomaly_detection.java
│   └── go
│       └── network_traffic.go
├── config
│   └── config.json
└── main.py

This structure separates the project into categories (encryption, access control, and threat detection), with each category containing language-specific implementations (e.g., Python, Java, C++, etc.).

