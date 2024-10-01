# AirBnB Clone: A Comfy Command-Line Adventure

Welcome to our humble abode (in the terminal)! This is a simplified clone of the AirBnB platform, built with love, sweat, and a sprinkle of Python magic. 

## Table of Contents

* [Description](#description)
* [Installation/Setup](#installationsetup)
* [Command Interpreter](#command-interpreter-your-terminal-travel-agent)
* [Usage Examples](#usage-examples)
* [Features](#features)
* [Project Structure](#project-structure)
* [Testing](#testing)
* [Limitations](#limitations)
* [Future Work](#future-work)
* [A Note on Our "Database"](#a-note-on-our-database)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments) 

## Description

Imagine AirBnB, but instead of fancy pictures and endless scrolling, you get the raw, unadulterated power of the command line. No need to worry about your browser crashing – this baby runs smoothly in your terminal, even on a potato-powered machine.

This project focuses on the core functionalities of AirBnB:

* **Managing Users:** Because every great vacation rental needs a guest (and someone to pay for it).
* **Handling Places:** From cozy cabins to luxurious lofts, we've got you covered (virtually, of course).
* **Storing Data (the old-school way):**  Forget fancy databases! We're saving everything in a trusty JSON file. Think of it as a digital scrapbook for your vacation memories.

## Installation/Setup

* **Dependencies:**  Just a sprinkle of Python magic (and maybe a few standard libraries).
* **Instructions:**
    1. Clone this repository from the mystical realm of GitHub.
    2. Open your terminal and navigate to the project directory.
    3. Run the `console.py` script (if you dare!).

## Command Interpreter: Your Terminal Travel Agent

* **Starting the Adventure:** `./console.py`
* **Usage:** Enter commands at the `(hbnb)` prompt. It's like having a conversation with a travel agent who speaks only in code, so its almost impossible to get anything done. 
* **Available Spells (Commands):**
    * `help`: Your trusty guidebook. Lists available commands and their mystical powers.
    * `quit`:  End your adventure (for now).
    * `create <class>`:  Summon a new entity into existence (e.g., `create User`, `create Place`).
    * `show <class> <id>`:  Reveal the secrets of a specific entity (e.g., `show User 1234-5678`).
    * `destroy <class> <id>`: Banish an entity from existence (use with caution!).
    * `all [class]` :  Unveil all entities or those of a specific class.
    * `update <class> <id> <attribute> "<value>"`:  Modify the properties of an entity (e.g., `update User 1234-5678 name "John Doe"`).

## Usage Examples

**Creating a User and a Place:**

```bash
(hbnb) create User
1234-5678  # (Example ID)
(hbnb) create Place
abcd-efgh  # (Example ID)
(hbnb) update Place abcd-efgh user_id "1234-5678"
(hbnb) show Place abcd-efgh
[Place] (abcd-efgh) {'user_id': '1234-5678', ...}

**Listing All Users:**

Bash
(hbnb) all User
["[User] (1234-5678) {...}", "[User] (9876-5432) {...}"]

**Features**
* User Management: Create, update, delete, and display users.
* Place Management: Create, update, delete, and display places.
* (More to come!) We're still working on adding more exciting features to this magical console.

**Project Structure**
├── models
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine
│       ├── __init__.py
│       └── file_storage.py
├── console.py
└── tests
    └── ... (test files)

	**Testing**

Running Tests: We've got a whole suite of tests to ensure this console doesn't go haywire. Run them using python3 -m unittest discover tests.

**Limitations**

No GUI (Yet) We're still working on conjuring up a graphical user interface. For now, you will have to embrace the retro charm of the command line.

Limited Features: This is a simplified clone, so some of the more advanced AirBnB features might be missing (but hey, we are getting there!)

**Limitations**

GUI Development: A magical graphical user interface is in the works.
More Features: We plan to add more commands and functionalities to make this console truly enchanting.
World Domination (Maybe): We're not ruling anything out.

"A Note on Our "Database"
We're keeping things simple (and nostalgic) by storing all data in a JSON file. Think of it as a vintage travel journal, but instead of handwritten notes, it's filled with neatly formatted data.

**Contributing**
*Nathan Wilson: The code wizard.
*Ariel Lopez: The testing guru and other wizard

**License**
The license of knowledge and nihilism.

**Acknowledgments**
We'd like to thank the Python community for their endless support and magical spells (libraries).
A special thanks to coffee for keeping us fueled during those late-night coding sessions.
