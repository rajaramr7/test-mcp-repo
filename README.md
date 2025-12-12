# Test MCP Repository

This repository contains sample MCP (Model Context Protocol) configurations for testing [MCP Audit](https://github.com/apisec/mcp-audit).

## MCP Configurations Found

This repo includes various MCP configurations to test different detection scenarios:

### 1. Root `mcp.json`
- `filesystem` - Anthropic's filesystem server (verified publisher)
- `slack` - Model Context Protocol's Slack server (verified publisher)
- `postgres-db` - Database access server (has secrets in env)
- `custom-shell-tools` - Shell access tools (high risk)
- `local-custom-server` - Local binary (unverified)

### 2. `.mcp/config.json`
- `github-integration` - GitHub API access
- `memory-store` - In-memory storage server

### 3. `package.json` Dependencies
- `@modelcontextprotocol/sdk`
- `@anthropic/mcp-server-filesystem`
- `@modelcontextprotocol/server-slack`
- `mcp-server-github`

### 4. `requirements.txt` (Python)
- `fastmcp`
- `modelcontextprotocol`
- `mcp`

### 5. `docker-compose.yml`
- MCP servers running in Docker containers

## Testing with MCP Audit

```bash
# Scan this repository
mcp-audit scan --path /path/to/this/repo

# Scan with trust checking
mcp-audit scan --path /path/to/this/repo --with-trust

# Export to JSON
mcp-audit scan --path /path/to/this/repo --format json --output results.json

# Validate against policy
mcp-audit policy --policy /path/to/policy.yaml --input results.json
```

## Expected Results

When scanned, MCP Audit should find:
- **5+ MCPs** from various configuration files
- **Risk flags**: `filesystem-access`, `database-access`, `shell-access`, `secrets-in-env`, `local-binary`, `unverified-source`
- **Trust scores**: Mix of HIGH (verified publishers) and LOW (unverified sources)

## Risk Summary

| MCP | Risk Level | Flags |
|-----|------------|-------|
| filesystem | Medium | filesystem-access |
| slack | Low | secrets-in-env |
| postgres-db | Medium | database-access, secrets-in-env |
| custom-shell-tools | High | shell-access, unverified-source |
| local-custom-server | High | local-binary |
