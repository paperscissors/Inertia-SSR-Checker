# InertiaSSRPrepper

![PyPI](https://img.shields.io/pypi/v/inertiassrprepper)
![Python](https://img.shields.io/pypi/pyversions/inertiassrprepper)
![License](https://img.shields.io/pypi/l/inertiassrprepper)
![Downloads](https://img.shields.io/pypi/dm/inertiassrprepper)

A modern Python CLI tool that scans Laravel applications using Inertia.js and Vue 3 to identify potential Server-Side Rendering (SSR) compatibility issues.

<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/inertiassrprepper/main/docs/images/demo.gif" alt="InertiaSSRPrepper Demo" width="700">
</p>

## 📋 Table of Contents

- [✨ Features](#-features)
- [💡 Why InertiaSSRPrepper?](#-why-inertiassrprepper)
- [🚀 Installation](#-installation)
- [🏃‍♂️ Quick Start](#️-quick-start)
- [📊 Examples](#-examples)
- [📘 Usage](#-usage)
- [🔍 Issue Categories](#-issue-categories)
- [📤 Output Formats](#-output-formats)
- [🛠️ Development](#️-development)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

## ✨ Features

- 🔍 Scans your entire Laravel + Inertia.js + Vue 3 codebase for SSR compatibility issues
- 🚫 Identifies 25+ common SSR problems with detailed pattern matching
- 🎨 Generates colorful, interactive reports in terminal, HTML, or JSON formats
- 🧠 Uses Claude 3.7 AI to provide tailored, contextual solutions for each issue
- ⚡ Shows real-time progress with detailed statistics while scanning large codebases
- 🚦 Categorizes issues by severity (critical, major, medium, minor) for prioritization
- 🔧 Customizable ignore patterns and detection rules
- 🔍 Supports interactive search and filtering in HTML reports

## 💡 Why InertiaSSRPrepper?

Implementing Server-Side Rendering in an existing Laravel Inertia.js application can be challenging due to numerous client-side dependencies and browser-specific code patterns. InertiaSSRPrepper helps you:

- **Identify SSR issues before they break your production app** - Catch all potential SSR problems early
- **Save hours of debugging time** - Automatically find issues that would take days to discover manually
- **Get expert solutions** - Receive AI-powered suggestions for fixing each issue
- **Plan your SSR migration** - Prioritize fixes based on severity
- **Improve overall code quality** - Many SSR issues are also general best practices problems

## 🚀 Installation

### From source

```bash
# Clone this repository
git clone https://github.com/yourusername/inertiassrprepper.git
cd inertiassrprepper

# Install with uv
uv pip install -e .

# Or install with pip
pip install -e .
```

## 🏃‍♂️ Quick Start

Scan your Laravel Inertia.js application in just one step:

```bash
# Basic scan with terminal output
inertiassr scan /path/to/your/laravel/app

# Generate HTML report with Claude AI suggestions
inertiassr scan /path/to/your/laravel/app --output report.html --api-key $ANTHROPIC_API_KEY
```

## 📊 Examples

### Generate HTML Report

```bash
inertiassr scan /path/to/app --output report.html --api-key your-anthropic-key
```

### Generate JSON Report

```bash
inertiassr scan /path/to/app --output report.json
```

### Scan with Custom Ignore Patterns

```bash
inertiassr scan /path/to/app --ignore "*.test.js,*.spec.js,legacy/*"
```

### Scan with Verbose Output

```bash
inertiassr scan /path/to/app --verbose
```

## 📘 Usage

### Command-line Options

| Option | Description |
|--------|-------------|
| `path` | Path to your Laravel + Inertia.js application (required) |
| `--api-key`, `-k` | Anthropic API key for Claude (can also use `ANTHROPIC_API_KEY` env var) |
| `--output`, `-o` | Output file path for report (defaults to stdout) |
| `--format`, `-f` | Report format: 'json' or 'html' (defaults to using file extension) |
| `--ignore`, `-i` | Additional glob patterns to ignore (already ignores .git, node_modules, vendor, public, storage, etc.) |
| `--verbose`, `-v` | Enable verbose output |
| `--no-verify` | Skip verification of Laravel Inertia app |
| `--max-files` | Maximum number of files to scan (for testing) |
| `--version` | Show version information and exit |

### Environment Variables

- `ANTHROPIC_API_KEY`: Your Anthropic API key for Claude integration

## 🔍 Issue Categories

<details>
<summary>Click to expand issue categories</summary>

Issues are categorized by severity to help you prioritize fixes:

| Severity | Description |
|----------|-------------|
| Critical | Issues that will completely break SSR functionality |
| Major | Issues likely to cause SSR rendering failures |
| Medium | Issues that may cause inconsistent SSR behavior |
| Minor | Issues that could cause subtle differences between SSR and client rendering |

### Critical Issues
- Browser API usage (`window`, `document`, `navigator`, etc.)
- Direct DOM manipulation (`document.getElementById`, etc.)
- Client-side only libraries (jQuery, etc.)

### Major Issues
- Incorrect lifecycle hooks (Vue 2 style instead of Vue 3 Composition API)
- Improper Inertia.js imports
- Legacy Vue instance creation
- Direct event listener attachment
- Dynamic component loading without proper handling

### Medium Issues
- Incorrect Inertia props access
- Meta tag manipulation
- Timer functions without proper cleanup
- Missing key attributes on v-for loops
- Component registration issues

### Minor Issues
- Import path case sensitivity issues
- Browser-specific CSS features
- Inline scripts in templates
- Third-party script tags

</details>

## 📤 Output Formats

### Terminal Output
- Colorful, interactive report in the terminal
- Tables showing issues grouped by file
- Issues are color-coded by severity
- Syntax-highlighted code snippets

### HTML Report
- Interactive HTML report with filters and search
- Collapsible file sections
- Color-coded severities
- Syntax highlighting for code snippets
- Statistics and charts
- Browser-compatible simplified HTML report for maximum compatibility

### JSON Report
- Structured JSON data for further processing
- Includes full issue details, file paths, line numbers, and solutions
- Compatible with other tools and integrations

### Example Terminal Report

```
╭─── SSR Compatibility Scan Summary ────────────────────────────────────╮
│                                                                       │
│ SSR Compatibility Scan Complete                                       │
│ Found 24 potential issues in 8 files                                  │
│                                                                       │
│ ┌────────────┬───────┐                                                │
│ │ Total Issues│ 24    │                                                │
│ │ Files with Issues│ 8     │                                                │
│ │ Issue Types│ 12    │                                                │
│ └────────────┴───────┘                                                │
│                                                                       │
│ ┌─────── Issues by Severity ────────┐                                 │
│ │ Severity  │ Count │ Percentage    │ Distribution                    │
│ │ Critical  │ 8     │ 33.3%         │ ████████████████                │
│ │ Major     │ 10    │ 41.7%         │ ████████████████████            │
│ │ Medium    │ 4     │ 16.7%         │ ████████                        │
│ │ Minor     │ 2     │ 8.3%          │ ████                            │
│ └───────────┴───────┴───────────────┴──────────────────────────────────┘
╰───────────────────────────────────────────────────────────────────────╯
```

## 🛠️ Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/inertiassrprepper.git
cd inertiassrprepper

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
uv pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Linting

```bash
ruff check
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Laravel](https://laravel.com/)
- [Inertia.js](https://inertiajs.com/)
- [Vue.js](https://vuejs.org/)
- [Anthropic Claude](https://www.anthropic.com/claude)
- [Rich](https://github.com/Textualize/rich)
- [Typer](https://github.com/tiangolo/typer)

---

<p align="center">
  Made with ❤️ for the Laravel and Inertia.js community
</p>
