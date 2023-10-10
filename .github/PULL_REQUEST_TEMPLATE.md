__IMPORTANT:__ Please take note of the below checklist, especially the first two items.

# Pull Request Checklist

- [ ] All pull requests must include the Contributor License Agreement (see below).
- [ ] Code should conform to the following:
    - [ ] pep8 compliant with some exceptions (see pytest.ini)
    - [ ] 100% test coverage with pytest (with valid tests). If you have difficulty
      writing tests for the code, feel free to ask for help or submit the PR without tests.
    - [ ] Complete, correctly-formatted documentation for all classes, functions and methods.
    - [ ] documentation has been rebuilt with ``tox -e docs``
    - [ ] All modules should have (and use) module-level loggers.
    - [ ] **Commit messages** should be meaningful, and reference the Issue number
      if you're working on a GitHub issue (i.e. "issue #x - <message>"). Please
      refrain from using the "fixes #x" notation unless you are *sure* that the
      the issue is fixed in that commit.
    - [ ] Git history is fully intact; please do not squash or rewrite history.
