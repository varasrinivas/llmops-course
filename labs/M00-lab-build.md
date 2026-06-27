# M00 Lab: Build It with AI — Set Up the UCC LLMOps Sandbox

## Objective
Extend the UCC platform skeleton with operational tooling: a 20-query eval suite, Langfuse tracing integration, and a feedback collection endpoint.

## Prerequisites
- UCC platform sandbox from the AI Platform course (or create a basic Claude API wrapper)
- Python 3.10+, `anthropic`, `langfuse` packages
- Claude API key

## The Build (35 min)

### Step 1: Create the Eval Suite (10 min)

Use Claude to generate a golden set:
```
"Generate 20 UCC filing test cases as JSON. Each should have: filing_text (realistic UCC-1 or UCC-3 filing), expected_debtor_name, expected_filing_type, difficulty (easy/medium/hard). Include 5 easy, 10 medium, 5 hard. Hard cases should include truncated names, multiple debtors, and amendment filings. Return ONLY JSON."
```

Save as `evals/golden-set.json`. Create `evals/run_eval.py`:
```python
import json, anthropic

client = anthropic.Anthropic()
golden = json.loads(open("evals/golden-set.json").read())

correct, total = 0, len(golden)
for case in golden:
    response = client.messages.create(
        model="claude-sonnet-4-6", max_tokens=256,
        system="Extract the debtor name from this UCC filing. Return ONLY the name.",
        messages=[{"role": "user", "content": case["filing_text"]}]
    )
    extracted = response.content[0].text.strip()
    match = extracted.lower() == case["expected_debtor_name"].lower()
    correct += match
    if not match:
        print(f"  MISS: expected '{case['expected_debtor_name']}', got '{extracted}'")

print(f"\nBaseline score: {correct}/{total} ({correct/total:.1%})")
```

### Step 2: Add Langfuse Tracing (10 min)

```bash
pip install langfuse
```

Create `monitoring/traced_client.py`:
```python
from langfuse.decorators import observe, langfuse_context
import anthropic

client = anthropic.Anthropic()

@observe(as_type="generation")
def extract_debtor(filing_text: str, model: str = "claude-sonnet-4-6"):
    response = client.messages.create(
        model=model, max_tokens=256,
        system="Extract the debtor name. Return ONLY the name.",
        messages=[{"role": "user", "content": filing_text}]
    )
    result = response.content[0].text.strip()
    langfuse_context.update_current_observation(
        usage={"input": response.usage.input_tokens,
               "output": response.usage.output_tokens}
    )
    return result
```

### Step 3: Add Feedback Collection (10 min)

Create `feedback/collector.py`:
```python
import json, sqlite3
from datetime import datetime

class FeedbackCollector:
    def __init__(self, db_path="feedback/feedback.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY, timestamp TEXT, request_id TEXT,
            extracted TEXT, corrected TEXT, is_correct INTEGER, notes TEXT
        )""")

    def record(self, request_id, extracted, is_correct, corrected=None, notes=None):
        self.conn.execute(
            "INSERT INTO feedback (timestamp, request_id, extracted, corrected, is_correct, notes) VALUES (?,?,?,?,?,?)",
            (datetime.now().isoformat(), request_id, extracted, corrected, is_correct, notes)
        )
        self.conn.commit()

    def stats(self):
        cur = self.conn.execute("SELECT COUNT(*), SUM(is_correct) FROM feedback")
        total, correct = cur.fetchone()
        return {"total": total or 0, "correct": correct or 0,
                "accuracy": (correct/total if total else 0)}
```

### Step 4: Run Baseline (5 min)

```python
# main.py - tie it all together
from evals.run_eval import *  # runs the eval
from feedback.collector import FeedbackCollector

fc = FeedbackCollector()
print(f"\nFeedback stats: {fc.stats()}")
print("LLMOps sandbox ready. Baseline recorded.")
```

## Deliverable
```
ucc-llmops/
├── evals/golden-set.json        # 20 test cases
├── evals/run_eval.py            # Eval runner
├── monitoring/traced_client.py  # Langfuse-traced client
├── feedback/collector.py        # Feedback storage
└── main.py                      # Baseline runner
```

## Connection to Next Module
M01 will use this sandbox to demonstrate how LLMOps differs from MLOps. M04 will expand the eval suite from 20 to 100 queries with proper scoring rubrics.
