# 🛗 ILSCS: Intelligent Lift & Smart Control System

The inefficiency of traditional elevator systems—characterized by unnecessary stops, ghost calls, and heavy campus crowd bottlenecks—poses a major operational challenge, requiring smarter computational and automated control methods. In this project, we develop ILSCS, an intelligent, Python-based elevator control and telemetry framework designed to optimize passenger flow and system energy efficiency.

Instead of operating on standard first-come-first-served rules, the system integrates a presence-verification window to validate actual boarding demand before queueing floor calls. The software processes these operational constraints through an autonomous decision engine and streams real-time system telemetry into a local SQLite database alongside asynchronous WebSocket broadcasting.

---

## 🚀 Features

* **Smart Boarding Zone Verification**: Uses real-time presence checks to prevent empty car runs and ghost calls by validating passenger intent before queueing.
* **Autonomous Decision Engine (`state_machine.py`)**: Manages dynamic floor call interrupts, priority evaluation, and optimized dispatch/skip logic.
* **SQLite Telemetry & Logging (`db_logger.py`)**: Automatically records live event logs, timestamps, verification statuses, and system metrics into a local database (`ilscs_telemetry.db`).
* **Asynchronous WebSocket Streaming (`websocket_server.py`)**: Broadcasts real-time system states and event payloads over port `8765` for dashboard monitoring.
* **Modular Architecture**: Cleanly separated script modules allowing multi-developer collaboration across the project team.

---

## 🛠️ Tech Stack

* **Core Language**: Python 3
* **Asynchronous & Network Libraries**: `asyncio`, `websockets`
* **Database Engine**: SQLite3 (`sqlite3`)
* **Development Environment**: VS Code, Virtual Environment (`env`)

---

## 📂 Project Structure

    ILSCS/
    │
    ├── env/                     # Python virtual environment
    ├── db_logger.py             # SQLite database initialization and event logger
    ├── state_machine.py         # Core decision engine and queue management
    ├── websocket_server.py      # Asynchronous WebSocket streaming server
    ├── ilscs_telemetry.db       # Local SQLite telemetry database
    └── README.md                # Project documentation

---

## ⚙️ Installation & Setup

Follow these steps to run the simulation locally on your machine:

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YourUsername/ILSCS.git](https://github.com/YourUsername/ILSCS.git)
   cd ILSCS

2. Activate the Virtual Environment
   ```bash
   .\env\Scripts\activate

3. Run the Database Logger
   ```bash
   python db_logger.py

4. Run the State Machine Decision Engine
   ```bash
   python state_machine.py

5. Launch the Live WebSocket Server
   ```bash
   python websocket_server.py

---

# 👥 Team ILSCS

* Anushreya Satish (CSE)
* Kartik Kumar Jain (AI/ML)
* Jeevan Teja Reddy (AI/ML)
* Siddhant Jaiswal (Electrical)
* Varsha Das (Mechanical)

---

# 📜 License

This project is open-source and available under the [MIT License](LISCENSE). Feel free to fork, modify, and use it!
