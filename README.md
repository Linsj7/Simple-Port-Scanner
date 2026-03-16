Simple Port Scanner 🔎
A lightweight Python-based port scanner that checks for open ports on a target host. This project demonstrates basic socket programming, networking, and multithreading in Python.

The scanner attempts to connect to a range of ports on a given host and reports which ports are open.

📌 Features
Scan a custom range of ports
Multi-threaded scanning for faster performance
Supports IP addresses and domain names
Displays open ports in real time
Simple and beginner‑friendly implementation
🛠 Technologies Used
Python 3
Socket Programming
Threading
Queue
📂 Project Structure
simple-port-scanner/
│
├── scanner.py
├── README.md
├── requirements.txt
└── LICENSE
⚙️ Installation
Clone the repository:

git clone https://github.com/yourusername/simple-port-scanner.git
Navigate into the project folder:

cd simple-port-scanner
No external dependencies are required.

🚀 Usage
Run the scanner:

python scanner.py
You will be prompted to enter:

Target host (IP or domain)
Start port
End port
Example:

Enter target IP or hostname: scanme.nmap.org
Start port: 20
End port: 100
🖥 Example Output
[OPEN] Port 22
[OPEN] Port 80

Scan complete.
Open ports: [22, 80]
📚 What You Can Learn From This Project
Basics of network port scanning
How TCP connections work
Python socket programming
Multithreading for faster execution
Building command-line tools
⚠️ Disclaimer
This project is intended for educational purposes only.

Do not scan networks, systems, or servers without permission. Unauthorized port scanning may be illegal in some regions.

🔧 Future Improvements
Possible upgrades:

Command-line arguments (argparse)
Banner grabbing
Service detection
Async scanning using asyncio
Export results to JSON or CSV
Progress indicator
📜 License
This project is licensed under the MIT License.

⭐ If you found this project useful, consider starring the repository.
