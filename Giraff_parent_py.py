class Giraffe:
    # For growth parameter, use only "young" or "mature"
    def __init__(self, growth):
        self.__species = "Giraffa"
        self.__avglifespan = "20-27 years"
        self.__maturity = growth

    def stature(self):
        """Provides information about the giraffe's height and weight based on maturity."""
        try: 
            if self.__maturity.lower() == "young":
                print("A young giraffe is 1-5 years old. They're about 6 ft tall. They weigh between 100 and 200 lbs.")
            elif self.__maturity.lower() == "mature":
                print("A mature giraffe is around 15-20 years old. They're about 14-18 ft tall. They can weigh between 2600 to 4200 lbs.")
        except:
            print("Make sure growth parameter is either 'young' or 'mature'.")

    def average_height(self):
        """Provides the average height of giraffes."""
        print("The average height of a giraffe is 16-18 feet for mature adults, with males being slightly taller than females.")

    def average_speed(self):
        """Describes the average speed of giraffes."""
        print("Giraffes can run at speeds of up to 35 miles per hour over short distances and maintain about 10 miles per hour over longer distances.")

    def diet(self):
        """Describes the diet of giraffes."""
        print("Giraffes are herbivores, primarily feeding on leaves, fruits, and flowers of woody plants, particularly acacia species.")

    def neck_length(self):
        """Provides information about the giraffe's neck length."""
        print("The average neck length of a giraffe is around 6 feet, with some exceeding 8 feet.")

    def social_behavior(self):
        """Describes the social behavior of giraffes."""
        print("Giraffes are social animals and typically live in groups called towers, consisting of 10-20 individuals.")

    def conservation_status(self):
        """Shares the conservation status of giraffes."""
        print("Giraffes are currently listed as 'Vulnerable' by the IUCN, with certain subspecies considered endangered due to habitat loss and poaching.")

    def unique_features(self):
        """Highlights unique features of giraffes."""
        print("Giraffes have unique coat patterns, and no two giraffes have the same markings. They also have a specialized cardiovascular system to pump blood to their brain.")
        

