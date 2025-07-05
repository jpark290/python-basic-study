# Real Estate Listing Program (Canada version - Toronto area)

class House:
    # Initialize listing details
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # Show listing details
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# Create listings
house_list = []

house1 = House("Downtown Toronto", "Condo", "For Sale", "$950,000", 2015)
house2 = House("North York", "Apartment", "For Rent", "$2,400/month", 2010)
house3 = House("Scarborough", "Detached House", "For Lease", "$3,200/month", 2005)

# Add listings to list
house_list.append(house1)
house_list.append(house2)
house_list.append(house3)

# Display listings
print("There are {} real estate listings available in the GTA.".format(len(house_list)))
for house in house_list:
    house.show_detail()
