# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture

This is a minimal Python project demonstrating the Anthropic Claude API. The codebase consists of:

- `quickstart.py` - A simple script that creates an Anthropic client and sends a message to Claude Sonnet 4
- `requirements.txt` - Python dependencies, primarily the `anthropic` library

## Commands

### Running the application
```bash
python quickstart.py
```

### Installing dependencies
```bash
pip install -r requirements.txt
```

## Environment Setup

The script expects the Anthropic API key to be available as an environment variable (likely `ANTHROPIC_API_KEY`) as per the Anthropic SDK's default behavior.