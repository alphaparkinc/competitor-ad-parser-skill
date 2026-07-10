# genpark-competitor-ad-parser-skill

> **GenPark AI Agent Skill** -- Competitor ad text analyzer and hook compiler.

## Quick Start

```python
from client import CompetitorAdParserClient
client = CompetitorAdParserClient()
res = client.parse_copy("Cheapest pricing available")
print(res["detected_hook"])
```
