# Using the module: theater_module

# 1. Basic import
import theater_module
theater_module.price(3)            # 3 people - regular movie price
theater_module.price_morning(4)    # 4 people - morning discount price
theater_module.price_military(5)   # 5 people - military discount price

# 2. Import with alias
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_military(5)

# 3. Import all functions (not recommended for large modules)
from theater_module import *
price(3)
price_morning(4)
price_military(5)

# 4. Import specific functions only
from theater_module import price, price_morning
price(3)
price_morning(4)
# price_military(5)  # This will raise an error since it's not imported

# 5. Import with alias for specific function
from theater_module import price_military as price
price(2)  # Executes price_military function with alias 'price'
