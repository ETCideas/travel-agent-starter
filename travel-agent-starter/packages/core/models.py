from typing import List, Optional, Literal, Dict
from pydantic import BaseModel, Field

Currency = Literal["USD", "EUR", "INR", "GBP", "AUD"]

class UserPreferences(BaseModel):
    hotel_style: Optional[str] = None
    neighborhoods: Optional[List[str]] = None
    amenities: Optional[List[str]] = None
    loyalty_ids: Optional[Dict[str, str]] = None
    avoid_redeye: bool = True
    max_stops: int = 1

class Passenger(BaseModel):
    first_name: str
    last_name: str
    age: Optional[int] = None

class TripRequest(BaseModel):
    origin: str
    destination: str
    depart_date: str  # ISO date
    return_date: Optional[str] = None
    pax: List[Passenger] = Field(default_factory=list)
    budget: Optional[float] = None
    currency: Currency = "USD"

class Price(BaseModel):
    amount: float
    currency: Currency = "USD"
    refundable: bool = False

class FlightOption(BaseModel):
    id: str
    carrier: str
    segments: List[Dict]
    total_duration_min: int
    bags_included: int
    price: Price
    fare_rules: Optional[str] = None

class HotelOption(BaseModel):
    id: str
    name: str
    address: str
    rating: Optional[float] = None
    amenities: List[str] = Field(default_factory=list)
    refundable_until: Optional[str] = None
    price: Price

class ExperienceOption(BaseModel):
    id: str
    name: str
    provider: str  # viator/tripadvisor/...
    when: str
    duration_min: int
    link: Optional[str] = None
    price: Price

class ItineraryDay(BaseModel):
    date: str
    items: List[Dict]

class Itinerary(BaseModel):
    days: List[ItineraryDay] = Field(default_factory=list)

class BookingOrder(BaseModel):
    id: str
    component: Literal["flight", "hotel", "experience"]
    status: Literal["planned", "held", "booked", "failed"] = "planned"
    details: Dict = Field(default_factory=dict)

class TripState(BaseModel):
    req: TripRequest
    prefs: UserPreferences = Field(default_factory=UserPreferences)
    flights: List[FlightOption] = Field(default_factory=list)
    hotels: List[HotelOption] = Field(default_factory=list)
    activities: List[ExperienceOption] = Field(default_factory=list)
    itinerary: Itinerary = Field(default_factory=Itinerary)
    orders: List[BookingOrder] = Field(default_factory=list)
    approvals: Dict = Field(default_factory=dict)
