# Contributing

Contributions are welcome and are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs through Github

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" is
open to whoever wants to implement it. Ideally you would come up with a test case which is currently failing because of the bug and that will pass after fixing the bug. It will help prevent regressions.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"feature" is open to whoever wants to implement it.

We've created the operators, hooks, macros and executors we needed, but we
made sure that this part of Airflow is extensible. New operators,
hooks and operators are very welcomed!

### Documentation

Airflow could always use better documentation,
whether as part of the official Airflow docs,
in docstrings, `docs/*.rst` or even on the web as blog posts or
articles.

### Submit Feedback

The best way to send feedback is to file an issue on Github.

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

## Latest Documentation

[API Documentation](http://pythonhosted.com/airflow)

You can also generate the documentation yourself with:

    cd docs && ./build.sh

## Testing and Continuous Integration

Continuous integration is setup through [Travis CI](https://travis-ci.org/airbnb/airflow) on the Airflow repository. It will run the current set of tests on pull requests, to try to ensure that we do not introduce regressions while adding new features.

Some tests are currently disabled in Travis until we find a way to run them in the build environment provided. Any help in that regard would be greatly appreciated. In the mean time, you can take a look at the [Running unit tests](#running-unit-tests) section below to setup your environment for running groups of tests or individual tests.

## Pull Request Guidelines

Before you submit a pull request from your forked repo, check that it
meets these guidelines:

1. The pull request should include tests, either as doctests, unit tests, or both.
1. If the pull request adds functionality, the docs should be updated as part of the same PR. Doc string are often sufficient, make sure to follow the sphinx compatible standards.
1. The pull request should work for Python 2.7 and 3.4. Support for 3.5 is experimental for now. Support for Python 2.6 support has been dropped, please consider upgrading to 2.7 if you want to use Airflow. If you need help writing code that works in both Python 2 and 3, see the documentation at the [Python-Future project](http://python-future.org) (the future package is an Airflow requirement and should be used where possible).
1.  Code will be reviewed by re running the unittests, flake8 and syntax should be as rigorous as the core Python project.
1.  Please rebase and resolve all conflicts before submitting.

## Running unit tests

Here are loose guidelines on how to get your environment to run the unit tests.
We do understand that no one out there can run the full test suite since Airflow is meant to connect to virtually any external system and that you 
most likely have only a subset of these in your environment. You should run the CoreTests and tests related to things you touched in your PR.

The best way to ensure consistent testing is to install airflow with the correct extras in a [virtual environment](https://virtualenv.readthedocs.org/en/latest/). You could create one in your airflow directory:

    cd /path/to/airflow/repository
    virtualenv env
    source env/bin/activate

Then install the airflow development requirements:

    pip install -r requirements.txt

Finally you can install airflow
    pip install git+file://.#egg=airflow[async,celery,crypto,hive,mysql,s3,webhdfs]
    python setup.py develop

Tests can then be run with (see also the [Running unit tests](#running-unit-tests) section below):

    ./run_unit_tests.sh

Lint the project with:

    flake8 changes tests




To set up a unit test environment, first take a look at `run_unit_tests.sh` and
understand that your ``AIRFLOW_CONFIG`` points to an alternate config file
while running the tests. You shouldn't have to alter this config file but
you may if need be.

From that point, you can actually export these same environment variables in
your shell, start an Airflow webserver ``airflow webserver -d`` and go and
configure your connection. Default connections that are used in the tests
should already have been created, you just need to point them to the systems
where you want your tests to run.

Once your unit test environment is setup, you should be able to simply run
``./run_unit_tests.sh`` at will. 

For example, in order to just execute the "core" unit tests, run the following: 

```
./run_unit_tests.sh tests.core:CoreTest
```

or a single test method: 

``` 
./run_unit_tests.sh tests.core:CoreTest.test_check_operators
```

For more information on how to run a subset of the tests, take a look at the nosetests docs.

See also the the list of test classes and methods in `tests/code.py`.

