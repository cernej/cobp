from fastapi import FastAPI, HTTPException
from models import Flight


app = FastAPI()


flights_db: list[Flight] = []


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Flight API"}


@app.get("/flights", response_model=list[Flight], tags=["Flights"])
def read_flights():
    return flights_db


@app.post("/flights", response_model=Flight, tags=["Flights"])
def create_flight(flight: Flight):
    flights_db.append(flight)
    return flight


@app.delete("/flights/{flight_id}", tags=["Flights"])
def delete_flight(flight_id: int):
    for index, flight in enumerate(flights_db):
        if flight.id == flight_id:
            del flights_db[index]
            return {"message": "Flight deleted successfully"}
    raise HTTPException(status_code=404, detail="Flight not found")