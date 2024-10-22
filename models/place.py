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
        if not kwargs:
            for attr, value in self.__class__.__dict__.items():
                if not attr.startswith("__") and not callable(getattr(self.__class__, attr)):
                    setattr(self, attr, value)
        print(f"Place initialized with attributes: {self.__dict__}")
