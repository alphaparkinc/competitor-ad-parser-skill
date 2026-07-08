"""
example_usage.py -- Demonstrates CompetitorAdParserClient
"""
from client import CompetitorAdParserClient

def main():
    client = CompetitorAdParserClient()
    result = client.parse_copy("Get free shipping on all products today only!")
    print("[Competitor Ad Analysis]")
    print(f"Hook: {result['detected_hook']}")
    print(f"Counter Strategy: {result['counter_angle']}")

if __name__ == "__main__":
    main()
