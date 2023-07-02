import os
from os.path import join

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
    session.install("-v", ".")
    session.install("mypy")
    session.run("mypy", "pyhash")


@nox.session(python=PYTHON_VERSIONS)
def tests(session: nox.Session) -> None:
    session.install("-v", ".")
    session.install("-r", "tests/requirements.txt")
    session.run("pytest", "-v", "--benchmark-disable")


@nox.session
def coverage(session: nox.Session) -> None:
    session.install("-v", ".", env=dict(COVERAGE="on"))
    session.install("-r", "tests/requirements.txt")
    try:
        session.run(
            "pytest", "-v", "--benchmark-disable", "--cov=./", "--cov-report=xml"
        )
    finally:
        session.run(
            "lcov",
            "--capture",
            "--directory",
            ".",
            "--output-file",
            "coverage.info",
            external=True,
        )

        with os.scandir("./src/") as it:
            args = [
                f"src/{entry.name}/*"                 
                for entry in it
                if not entry.name.startswith(".") and entry.is_dir()
            ]

        session.run(
            "lcov",
            "-o",
            "coverage_filtered.info",
            "--remove",
            "coverage.info",
            "/usr/*",
            *args,
            external=True
        )
        session.run(
            "genhtml",
            "--legend",
            "--prefix",
            "src",
            "coverage_filtered.info",
            "--output-directory",
            ".",
            external=True,
        )


@nox.session
def bench(session: nox.Session) -> None:
    session.install("-v", ".")
    session.install("-r", "tests/requirements.txt")
    session.run("pytest", "-v", "--benchmark-only")
