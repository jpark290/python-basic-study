# Importing a module inside a package
import travel.thailand

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# Note:
# You cannot import a class or function directly using:
#   import travel.thailand.ThailandPackage ❌
# Only modules or packages can be imported directly this way.

# Correct way to import a class
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()


# Another module in the same package
from travel import vietnam
trip_to2 = vietnam.VietnamPackage()
trip_to2.detail()


# What is __all__?

from travel import *
trip_to3 = vietnam.VietnamPackage()
trip_to3.detail()

# If __all__ is not defined in travel/__init__.py, the wildcard import (*) won’t expose submodules.
# Only the ones listed in __all__ will be accessible when using `from travel import *`.
# For example, if __all__ = ["vietnam"], trying to import thailand will raise an error.


# If the thailand module prints this:
# "Thailand travel module is being imported from another file."
# That line is executed only when the module is imported, not when run directly.


# Checking module location with inspect
import inspect
import random

print(inspect.getfile(random))           # Location of the built-in random module
print(inspect.getfile(travel.thailand))  # Location of our own thailand module
