For more information, please see the official docs at
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

Contributing Code
-----------------
A good pull request:

-  Is clear.
-  Works across all supported versions of Python.
-  Follows the existing style of the code base (see Codestyle section).
-  Has comments included as needed.

-  A test case that demonstrates the previous flaw that now passes with
   the included patch, or demonstrates the newly added feature.
-  If it adds/changes a public API, it must also include documentation
   for those changes.
-  Must be appropriately licensed (Apache 2.0).

Reporting An Issue/Feature
--------------------------
First, check to see if there's an existing issue/pull request for the
bug/feature. All issues are at
https://github.com/boto/boto3/issues and pull reqs are at
https://github.com/boto/boto3/pulls.

If there isn't an existing issue there, please file an issue. The
ideal report includes:

-  A description of the problem/suggestion.
-  How to recreate the bug.
-  If relevant, including the versions of your:

   -  Python interpreter
   -  Boto3
   -  Optionally of the other dependencies involved (e.g. Botocore)

-  If possible, create a pull request with a (failing) test case
   demonstrating what's wrong. This makes the process for fixing bugs
   quicker & gets issues resolved sooner.

Codestyle
---------
This project uses flake8 to enforce codstyle requirements. We've codified this
process using a tool called `pre-commit <https://pre-commit.com/>`__. pre-commit
allows us to specify a config file with all tools required for code linting,
and surfaces either a git commit hook, or single command, for enforcing these.

To validate your PR prior to publishing, you can use the following
`installation guide <https://pre-commit.com/#install>`__ to setup pre-commit.

If you don't want to use the git commit hook, you can run the below command
to automatically perform the codestyle validation:

.. code-block:: bash

    $ pre-commit run

This will automatically perform simple updates (such as white space clean up)
and provide a list of any failing flake8 checks. After these are addressed,
you can commit the changes prior to publishing the PR.
These checks are also included in our CI setup under the "Lint" workflow which
will provide output on Github for anything missed locally.

See the `flake8` section of the
`setup.cfg <https://github.com/boto/boto3/blob/develop/setup.cfg>`__ for the
currently enforced rules.
