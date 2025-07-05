class ThailandPackage:
    def detail(self):
        print("[Thailand Package - 5 Days] Bangkok & Pattaya (Night Market Tour) - CA$1,300")



# Code below runs only when this file is executed directly (not imported as a module)
if __name__ == "__main__":
    print("Thailand travel module is being run directly.")
    print("This code runs only when the module is executed on its own.")
    trip_to_thailand = ThailandPackage()
    trip_to_thailand.detail()
else:
    print("Thailand travel module has been imported.")
    print("This code runs only when the module is imported by another script.")
