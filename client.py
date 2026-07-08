"""
competitor-ad-parser-skill: Client SDK
Parses rival ad copy to identify core marketing hooks and counter-messages.
"""
from __future__ import annotations
from typing import Optional


class CompetitorAdParserClient:
    """
    SDK for competitive ad analysis.
    """

    def parse_copy(self, ad_copy: str) -> dict:
        copy_lower = ad_copy.lower()
        
        # Hook detection
        if "free" in copy_lower or "shipping" in copy_lower:
            hook = "Value/shipping incentive"
            counter = "Focus on premium product quality and ingredients rather than discount pricing."
        elif "fast" in copy_lower or "quick" in copy_lower:
            hook = "Speed/efficiency"
            counter = "Emphasize durability and long-term results."
        else:
            hook = "Generic brand awareness"
            counter = "Use high-converting direct-response hooks highlighting a specific pain point."

        return {
            "detected_hook": hook,
            "counter_angle": counter
        }
