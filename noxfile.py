import nox

nox.needs_version = ">=2023"
nox.options.sessions = ["format", "lint", "type", "tests"]

PYTHON_VERSIONS = [
    "3.9",
    "3.10",
    "3.11",
    "pypy3.9",
    "pypy3.10",
]

@nox.session
def format(session: nox.Session) -> None:
    session.install("black >= 23")
    session.run("black", "pyhash", "tests")
    session.notify("lint")

@nox.session
def lint(session: nox.Session) -> None:
    session.install("flake8")
    session.run("flake8", "pyhash")    

@nox.session
def type(session: nox.Session) -> None:
    session.install("mypy")
    session.install(".")
    session.run("mypy", "pyhash")

@nox.session(python=PYTHON_VERSIONS)
def tests(session: nox.Session) -> None:
    session.install("-r", "tests/requirements.txt")
    session.install(".")
    session.run("pytest", "--benchmark-disable", "--cov=./", "-v")

@nox.session
def bench(session: nox.Session) -> None:
    session.install("-r", "tests/requirements.txt")
    session.install(".")
    session.run("pytest", "-v", "--benchmark-only")