#!/usr/bin/env python
"""
Test script to generate a sample report using the original HTML template with simplified interface
"""
import os
from pathlib import Path
from typing import List, Optional, Dict, Any

from inertiassrprepper.scanner.scanner import SSRIssue
from inertiassrprepper.templates.html_report import generate_html_report

# Create sample issues for testing
sample_issues = [
    SSRIssue(
        file_path=Path('/path/to/file1.vue'),
        line_number=10,
        line_content="const browserWidth = window.innerWidth;",
        issue_type="Browser API",
        message="Accessing window API directly can cause SSR errors",
        solution="Wrap in onMounted() or check if window is defined: if (typeof window !== 'undefined') { ... }"
    ),
    SSRIssue(
        file_path=Path('/path/to/file1.vue'),
        line_number=15,
        line_content="document.getElementById('app').style.display = 'block';",
        issue_type="DOM Manipulation",
        message="Direct DOM manipulation will fail during SSR",
        solution="Use refs and template bindings instead: <div ref=\"appRef\" :style=\"{ display: 'block' }\"></div>"
    ),
    SSRIssue(
        file_path=Path('/path/to/file2.js'),
        line_number=25,
        line_content="localStorage.setItem('user', JSON.stringify(user));",
        issue_type="Browser Storage",
        message="localStorage is not available during SSR",
        solution="Use Vuex/Pinia state or wrap in client-only code: if (typeof window !== 'undefined') { localStorage.setItem(...) }"
    ),
    SSRIssue(
        file_path=Path('/path/to/helper.js'),
        line_number=42,
        line_content="navigator.language.substring(0, 2)",
        issue_type="Browser API",
        message="navigator is not available during SSR",
        solution="Provide a fallback value or make the code conditional: typeof navigator !== 'undefined' ? navigator.language.substring(0, 2) : 'en'"
    ),
    SSRIssue(
        file_path=Path('/path/to/component.vue'),
        line_number=100,
        line_content="mounted() { this.initializePlugin(); }",
        issue_type="Lifecycle Hook",
        message="mounted() is not called during SSR, use onMounted() with composition API",
        solution="Replace with composition API: import { onMounted } from 'vue'; ... setup() { onMounted(() => { initializePlugin(); }); }"
    ),
]

# Generate a test report
def generate_test_report():
    output_path = Path("test_html_report.html")
    generate_html_report(sample_issues, output_path)
    print(f"Test report generated at {output_path.absolute()}")

if __name__ == "__main__":
    generate_test_report()