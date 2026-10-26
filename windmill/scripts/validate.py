"""Kazene Windmill v1.0 synthetic conformance; Python standard library only."""
import json
import sys
from pathlib import Path

FIXTURES = Path(__file__).resolve().parents[1] / "examples/v1.0/policy-cases.json"

def decide(signal):
    """Return a guarded mode and capture permission, not a running process."""
    if (
        signal["core_heartbeat"] is False or signal["common_failure"] is True
        or signal["multi_blade_failure"] is True or signal["pressure"] >= 95
    ):
        return "P", False
    if (
        signal["pressure"] >= 85 or signal["blade_signature_ok"] is False
        or signal["role_ok"] is False or signal["least_privilege_ok"] is False
        or signal["trace_chain_ok"] is False or signal["swap_race"] is True
        or signal["detection_delayed"] is True or signal["recovery_verified"] is False
        or signal["blade_failed"] is True
    ):
        return "N", False
    if signal["command"] == "R":
        return "R", False
    if signal["command"] == "D":
        return "D", True
    return "N", False

def main():
    doc = json.loads(FIXTURES.read_text(encoding="utf-8"))
    assert doc["version"] == "1.0.0"
    assert len(doc["cases"]) >= 20
    count = 0
    for case in doc["cases"]:
        signals = dict(doc["defaults"])
        signals.update(case["patch"])
        mode, capture = decide(signals)
        correct = mode == case["expected"] and capture == (mode == "D")
        print(f"{'PASS' if correct else 'FAIL'} {case['id']} expected={case['expected']} actual={mode}")
        count += correct
    # Safety precedence regression: simultaneous faults must choose most conservative mode.
    base = doc["defaults"]
    for command in ("D", "R", "N", "unknown"):
        for pressure in (0, 84, 85, 94, 95, 100):
            state = dict(base, command=command, pressure=pressure)
            mode, capture = decide(state)
            assert mode == ("P" if pressure >= 95 else "N" if pressure >= 85 else command if command in ("D", "R") else "N")
            assert capture == (mode == "D")
            assert decide(dict(state, core_heartbeat=False))[0] == "P"
            assert decide(dict(state, blade_signature_ok=False))[0] in ("N", "P")
    print(f"Matched {count}/{len(doc['cases'])} synthetic cases")
    return 0 if count == len(doc["cases"]) else 1

if __name__ == "__main__":
    sys.exit(main())
