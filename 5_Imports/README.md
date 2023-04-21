Python Standards Manifesto
=====================
Imports
======================

Imports are always put at the top of the file, just after any module comments and docstrings and before module globals and constants. 

Imports should be sorted alphabetically starting with import followed by from ... import ...

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