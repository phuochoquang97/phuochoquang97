import requests
import json

def fetch_leetcode_data(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    data = response.json()
    return data

def generate_readme(data):
    readme_content = f"""
    ## LeetCode Stats
    - Total Problems Solved: {data['totalSolved']}
    - Easy Problems Solved: {data['easySolved']}
    - Medium Problems Solved: {data['mediumSolved']}
    - Hard Problems Solved: {data['hardSolved']}
    - Acceptance Rate: {data['acceptanceRate']}%
    """
    with open("README.md", "w") as f:
        f.write(readme_content)

if __name__ == "__main__":
    username = "tokbokki97"
    data = fetch_leetcode_data(username)
    generate_readme(data)
