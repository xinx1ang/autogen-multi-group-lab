import argparse

from .groups.user_proxy_team import UserProxyTeam


DEFAULT_TASK = "Build a Python function add(a, b) and provide tests plus a short implementation note."


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the AutoGen Multi-Group Lab MVP")
    parser.add_argument("--demo", action="store_true", help="Run the built-in demo task")
    parser.add_argument("--task", type=str, default="", help="Custom task text")
    args = parser.parse_args()

    task = DEFAULT_TASK if args.demo or not args.task else args.task

    runner = UserProxyTeam()
    _, output = runner.run(task)
    print(output)


if __name__ == "__main__":
    main()
