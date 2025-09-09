# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python fundamentals learning repository containing educational Python scripts that demonstrate core programming concepts. The codebase is structured as a series of numbered lesson files, each focusing on a specific Python fundamental topic.

## Architecture & Structure

- **Sequential Learning Structure**: Files are numbered (1.*, 2.*, etc.) to indicate lesson progression
- **Single-Topic Focus**: Each file demonstrates one core Python concept with comprehensive examples
- **Educational Examples**: Code includes print statements for learning visualization and extensive comments explaining concepts

## Key Files

- `1.hello-world.py` - Basic Python print statements
- `2.variables.py` - Variable creation, casting, and type checking
- `3.datatype.py` - All Python data types with examples (text, numeric, sequence, mapping, set, boolean, binary, None)
- `4.string.py` - String operations, methods, formatting, and manipulation
- `5.boolean_explained.py` - Comprehensive boolean logic, truthiness, conditionals, and practical examples
- `6.operator.py` - All Python operators (arithmetic, comparison, logical, assignment, identity, membership, bitwise)

## Development Commands

Since this is an educational Python repository without a build system:

- **Run individual lessons**: `python [filename].py` (e.g., `python 1.hello-world.py`)
- **Run all files**: `python *.py` or iterate through files manually
- **Check syntax**: `python -m py_compile [filename].py`

## Code Patterns

- Print statements are used extensively for educational output
- Variable names are descriptive for learning purposes
- Each topic includes multiple examples progressing from basic to advanced
- Comments explain concepts rather than implementation details
- F-string formatting is preferred for output formatting