# Setup AutoGen / OpenAI Environment

This document records the exact commands to finish the local environment setup for `autogen-multi-group-lab`.

## Goal

Make the following command runnable:

```bash
python3 -m src.autogen_multi_group_lab.main --demo --backend autogen
```

## 1. Enter the repository

```bash
cd /root/.openclaw/workspace/github-ops/autogen-multi-group-lab
```

## 2. Ensure `uv` is on PATH

```bash
export PATH="$HOME/.local/bin:$PATH"
uv --version
```

## 3. Create / activate virtualenv

If `.venv` already exists:

```bash
source .venv/bin/activate
```

If it does not exist yet:

```bash
uv venv .venv
source .venv/bin/activate
```

## 4. Install the minimal dependency first

Install `openai` first so the lighter path can be verified before attempting the heavier AutoGen packages.

```bash
uv pip install --index-url https://pypi.org/simple openai
```

Verify:

```bash
python -c "import openai; print(openai.__version__)"
```

## 5. Install AutoGen packages

```bash
uv pip install --index-url https://pypi.org/simple autogen-agentchat autogen-core
```

Verify:

```bash
python - <<'PY'
import importlib.util
for m in ['openai', 'autogen_agentchat', 'autogen_core']:
    print(m, bool(importlib.util.find_spec(m)))
PY
```

## 6. Configure API key

```bash
export OPENAI_API_KEY='your_openai_key'
```

Verify:

```bash
python - <<'PY'
import os
print('OPENAI_API_KEY', bool(os.getenv('OPENAI_API_KEY')))
PY
```

## 7. Run the demo

```bash
python3 -m src.autogen_multi_group_lab.main --demo --backend autogen
```

## One-shot command sequence

```bash
cd /root/.openclaw/workspace/github-ops/autogen-multi-group-lab
export PATH="$HOME/.local/bin:$PATH"
uv --version
uv venv .venv
source .venv/bin/activate
uv pip install --index-url https://pypi.org/simple openai
python -c "import openai; print(openai.__version__)"
uv pip install --index-url https://pypi.org/simple autogen-agentchat autogen-core
python - <<'PY'
import importlib.util
for m in ['openai', 'autogen_agentchat', 'autogen_core']:
    print(m, bool(importlib.util.find_spec(m)))
PY
export OPENAI_API_KEY='your_openai_key'
python - <<'PY'
import os
print('OPENAI_API_KEY', bool(os.getenv('OPENAI_API_KEY')))
PY
python3 -m src.autogen_multi_group_lab.main --demo --backend autogen
```

## Notes

- This machine previously lacked system `pip`, so local `uv` + `.venv` is the preferred path.
- If `autogen-agentchat` / `autogen-core` are slow to install on riscv64, check whether `openai` alone installed successfully first.
- If the final run still falls back, inspect:
  - whether `openai`, `autogen_agentchat`, `autogen_core` import successfully
  - whether `OPENAI_API_KEY` is present in the shell environment
