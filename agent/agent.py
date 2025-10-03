from agents import Agent, Runner
from agents.run import RunConfig
from agents.models.multi_provider import MultiProvider
import os

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

# 优先读取 Kimi 的密钥，若不存在则回退到 OPENAI_API_KEY
_api_key = os.getenv("KIMI_API_KEY") or os.getenv("OPENAI_API_KEY")
if not _api_key:
    raise RuntimeError(
        "未检测到 KIMI_API_KEY 或 OPENAI_API_KEY，请先导出环境变量再运行。"
    )

run_config = RunConfig(
    model="moonshot-v1-8k",
    model_provider=MultiProvider(
        openai_api_key=_api_key,
        openai_base_url="https://api.moonshot.cn/v1",
        openai_use_responses=False,
    ),
)

result = Runner.run_sync(
    agent,
    "write a haiku about water and cascade",
    run_config=run_config,
)
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.