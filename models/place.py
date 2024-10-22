from models.base_model import BaseModel

class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        print(f"Initializing Place")
        super().__init__(*args, **kwargs)
        
        # Convert attributes to the correct type
        self.number_rooms = int(getattr(self, 'number_rooms', 0))
        self.number_bathrooms = int(getattr(self, 'number_bathrooms', 0))
        self.max_guest = int(getattr(self, 'max_guest', 0))
        self.price_by_night = int(getattr(self, 'price_by_night', 0))
        self.latitude = float(getattr(self, 'latitude', 0.0))
        self.longitude = float(getattr(self, 'longitude', 0.0))
        
        print(f"Place initialized with attributes: {self.__dict__}")
