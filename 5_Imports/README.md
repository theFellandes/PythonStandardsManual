Python Standards Manifesto
=====================
Imports
=====================

Imports are always put at the top of the file, just after any module comments and docstrings and before module globals and constants. 

* Imports should be sorted alphabetically starting with import followed by from ... import ...

```
1st Way:

import httplib
import logging
import random
import StringIO
import time
import unittest
from nova.api import openstack
from nova.auth import users
from nova.endpoint import cloud

----------------------------------------------

2nd Way:

import a_standard
import b_standard

import a_third_party
import b_third_party

from a_soc import f
from a_soc import g
from b_soc import d
```

* If import is too long, it should be split into multiple lines with parenthesis.

* It should look as follows:
```
from foo import (
    ALL_USERS,
    Bar,
    Baz,
    Foo,
    lookup_all,
    lookup_foo,
    OTHER_THING,
)
```

* Don't use aliases for imports unless it is commonly used like pandas as pd, numpy as np.
```
import pandas as pd  #  Acceptable

import random as rd  #  Unacceptable
```

* Don't use wildcard imports.
```
from foo import *
```