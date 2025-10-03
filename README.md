# agent_v1

Minimal example using `agents` library.

## Run

```bash
# set Kimi (Moonshot) key
export KIMI_API_KEY="sk-xxxx"

uv run agent.py
```

## Notes
- Uses Kimi base URL: https://api.moonshot.cn/v1
- Default model: `moonshot-v1-8k`
- To disable tracing warning, set `OPENAI_AGENTS_TRACING_DISABLED=true`.
