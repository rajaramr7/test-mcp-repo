#!/usr/bin/env python3
"""
Custom MCP Server for testing
This is a sample MCP server implementation
"""

import json
import sys

def main():
    """Main entry point for the MCP server"""
    print(json.dumps({
        "name": "custom-mcp-server",
        "version": "1.0.0",
        "capabilities": ["file-read", "file-write", "execute"]
    }))

if __name__ == "__main__":
    main()
