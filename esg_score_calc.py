# ESG Score Calculator – Simple Example
# Author: Seyeon Lee
# Purpose: Demonstration for OMSCS application (Python practice)

# Dummy ESG dataset
companies = [
    {"name": "Company A", "E": 70, "S": 65, "G": 80},
    {"name": "Company B", "E": 55, "S": 60, "G": 50},
    {"name": "Company C", "E": 90, "S": 85, "G": 95}
]

# Calculate weighted ESG score
def calculate_esg(company, weights={"E":0.4, "S":0.3, "G":0.3}):
    score = (company["E"] * weights["E"] +
             company["S"] * weights["S"] +
             company["G"] * weights["G"])
    return round(score, 2)

# Print results
for c in companies:
    esg_score = calculate_esg(c)
    print(f"{c['name']} – ESG Score: {esg_score}")
