import argparse

from .groups.user_proxy_team import UserProxyTeam
from .runtime.backend import BackendManager


DEFAULT_TASK = "Build a Python function add(a, b) and provide tests plus a short implementation note."


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the AutoGen Multi-Group Lab MVP")
    parser.add_argument("--demo", action="store_true", help="Run the built-in demo task")
    parser.add_argument("--task", type=str, default="", help="Custom task text")
    parser.add_argument(
        "--backend",
        type=str,
        default="heuristic",
        choices=["heuristic", "autogen"],
        help="Execution backend. autogen uses a placeholder adapter with graceful fallback unless dependencies are installed.",
    )
    args = parser.parse_args()

    task = DEFAULT_TASK if args.demo or not args.task else args.task

    backend = BackendManager()
    backend.requested = args.backend
    print(f"[system] backend={backend.describe()}")

    runner = UserProxyTeam(backend=backend)
    _, output = runner.run(task)
    print(output)


if __name__ == "__main__":
    main()
