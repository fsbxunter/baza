# Cybersecurity Learning Roadmap
roadmap = {
    "Beginner": [
        {"topic": "Network Basics", "resources": ["TryHackMe Network Rooms"]},
        {"topic": "Web Application Security", "resources": ["OWASP Juice Shop"]},
        {"topic": "Basic Linux Commands", "resources": ["TryHackMe Linux Fundamentals"]}
    ],
    "Intermediate": [
        {"topic": "Vulnerability Scanning", "resources": ["TryHackMe Vulnerability Assessment"]},
        {"topic": "Exploitation Techniques", "resources": ["TryHackMe Exploit Development"]},
        {"topic": "Web Application Penetration Testing", "resources": ["TryHackMe Web Exploitation"]}
    ],
    "Advanced": [
        {"topic": "Privilege Escalation", "resources": ["TryHackMe Privilege Escalation"]},
        {"topic": "Container Security", "resources": ["TryHackMe Docker Security"]},
        {"topic": "Cloud Security", "resources": ["TryHackMe Cloud Rooms"]}
    ]
}

def print_roadmap():
    for level, topics in roadmap.items():
        print(f"\n{level} Level:")
        for topic in topics:
            print(f"- {topic['topic']}: {', '.join(topic['resources'])}")

print_roadmap()