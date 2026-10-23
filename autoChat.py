"""
prompt_sender.py

Automates sending prompts to a text input (e.g., ChatGPT in Chrome)
using clipboard + keyboard automation.

Requirements:
- pyautogui
- pyperclip
"""

import time
import platform
import pyautogui
import pyperclip
from dataclasses import dataclass
from typing import List, Dict


# ==============================
# CONFIGURATION MODULE
# ==============================

@dataclass
class AutomationConfig:
    # Timing (seconds)
    initial_switch_delay: int = 5
    paste_delay: float = 1.0
    response_wait_time: int = 50

    # Keyboard config
    paste_hotkey: tuple = None
    send_key: str = "enter"

    # Prompt prefixes
    prompt_prefixes: Dict[str, str] = None

    @staticmethod
    def get_paste_hotkey():
        system = platform.system()
        if system == "Darwin":      # macOS
            return ("command", "v")
        else:                       # Windows / Linux
            return ("ctrl", "v")

    def __post_init__(self):
        if self.paste_hotkey is None:
            self.paste_hotkey = self.get_paste_hotkey()

        if self.prompt_prefixes is None:
            self.prompt_prefixes = {
                "concept": (
                    "I am mastering DSA for coding interviews. "
                    "Explain this topic in a clear, structured way using "
                    "(skip any part if not applicable): "
                    "Intuition (real-world analogy), "
                    "Core definition, "
                    "What is it?, "
                    "Why this?, "
                    "Clear explanation, "
                    "Common mistakes, "
                    "Interview insight, "
                    "One-line learning outcome and trigger on "
                ),
                "problem": (
                    "I am preparing for DSA coding interviews. "
                    "Explain the following LeetCode problem using: "
                    "Intuition, "
                    "Core idea, "
                    "Step-by-step logic, "
                    "Dry run, "
                    "Edge cases, "
                    "Common mistakes, "
                    "Time & space complexity, "
                    "Interview takeaway. "
                    "Problem: "
                ),
                "hybrid": (
                    "I am mastering advanced DSA patterns for interviews. "
                    "Explain this hybrid concept clearly using: "
                    "Intuition, "
                    "Binary Search perspective, "
                    "Greedy feasibility logic, "
                    "Why binary search on answer works, "
                    "Common mistakes, "
                    "Interview insight, "
                    "One-line trigger. "
                    "Topic: "
                )
            }


# ==============================
# PROMPT LOADER MODULE
# ==============================

def load_prompts(multiline_text: str) -> List[str]:
    """
    Converts a multiline string into a clean list of prompts.
    Each non-empty line becomes one prompt.
    """
    return [
        line.strip()
        for line in multiline_text.strip().splitlines()
        if line.strip()
    ]


# ==============================
# AUTOMATION MODULE
# ==============================

def send_prompt(prompt: str, config: AutomationConfig, send: bool = True):
    """
    Copies prompt to clipboard and pastes it into active window.
    """
    pyperclip.copy(prompt)
    time.sleep(config.paste_delay)

    pyautogui.hotkey(*config.paste_hotkey)
    time.sleep(config.paste_delay)

    if send:
        pyautogui.press(config.send_key)


def wait_with_dots(seconds: int, interval: int = 5):
    print("⏳ Waiting", end="", flush=True)
    for i in range(1, seconds + 1):
        if i % interval == 0:
            print(".", end="", flush=True)
        time.sleep(1)
    print(" done.")


def run_automation(
    prompts: List[str],
    config: AutomationConfig,
    prefix_type: str,
    send_first_prompt: bool = True
):
    """
    Main runner that sends all prompts sequentially.
    """
    print(f"Loaded {len(prompts)} prompts")
    print(f"⏳ You have {config.initial_switch_delay} seconds to switch to Chrome...")
    time.sleep(config.initial_switch_delay)

    prefix = config.prompt_prefixes.get(
        prefix_type,
        config.prompt_prefixes["concept"]
    )

    for index, raw_prompt in enumerate(prompts, start=1):
        full_prompt = prefix + raw_prompt

        print(f"➡ Sending prompt {index}/{len(prompts)}")
        print(f"   Preview: {full_prompt[:120]}...")

        send_prompt(
            prompt=full_prompt,
            config=config,
            send=(send_first_prompt or index != 1)
        )

        if index != len(prompts):
            wait_with_dots(config.response_wait_time)

    print("✅ All prompts sent successfully")


# ==============================
# MAIN ENTRY POINT
# ==============================

def main():
    # SAFETY: move mouse to top-left corner to abort
    pyautogui.FAILSAFE = True

    PROMPTS = """
Binary Search (LC 704) – Find target in sorted array
Search Insert Position (LC 35) – Lower bound logic
First Bad Version (LC 278) – Binary search on condition
Guess Number Higher or Lower (LC 374) – Direction-based narrowing
Sqrt(x) (LC 69) – Binary search on integers
"""

    config = AutomationConfig(
        initial_switch_delay=5,
        response_wait_time=50
    )

    prompts = load_prompts(PROMPTS)

    run_automation(
        prompts=prompts,
        config=config,
        prefix_type="problem",
        send_first_prompt=True
    )


if __name__ == "__main__":
    main()
