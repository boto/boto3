.. _guide_new:

What's New
==========
Boto 3 is a ground-up rewrite of Boto. It uses a data-driven approach to
generate classes at runtime from JSON description files that are shared
between SDKs in various languages. This includes descriptions for a
high level, object oriented interface similar to those availabe in
previous versions of Boto.

Because Boto 3 is generated from these shared JSON files, we get
fast updates to the latest services and features and a consistent
API across services. Community contributions to JSON description
files in other SDKs also benefit Boto 3, just as contributions to
Boto 3 benefit the other SDKs.

Major Features
--------------
Boto 3 consists of the following major features:

* **Resources**: a high level, object oriented interface
* **Collections**: a tool to iterate and manipulate groups of resources
* **Clients**: low level service connections
* **Paginators**: automatic paging of responses
* **Waiters**: a way to block until a certain state has been reached

Along with these major features, Boto 3 also provides *sessions* and
per-session *credentials* & *configuration*, as well as basic
components like *authentication*, *parameter* & *response* handling,
an *event system* for customizations and logic to *retry* failed
requests.

Botocore
~~~~~~~~
Boto 3 is built atop of a library called
`Botocore <https://pypi.python.org/pypi/botocore>`_, which is shared by the
`AWS CLI <http://aws.amazon.com/cli/>`_. Botocore provides the low level
clients, session, and credential & configuration data. Boto 3 builds on top
of Botocore by providing its own session, resources and collections.
