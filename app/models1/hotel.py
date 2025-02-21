from app.models import db, Hotel

def add_hotel(hotel_name, location, description, price):
    new_hotel = Hotel(
        hotel_name=hotel_name,
        location=location,
        description=description,
        price=price
    )
    db.session.add(new_hotel)
    db.session.commit()
    return new_hotel

def get_all_hotels():
    return Hotel.query.all()

def get_hotel_by_id(hotel_id):
    return Hotel.query.get(hotel_id)

def update_hotel(hotel_id, hotel_name=None, location=None, description=None, price=None):
    hotel = Hotel.query.get(hotel_id)
    if hotel:
        if hotel_name:
            hotel.hotel_name = hotel_name
        if location:
            hotel.location = location
        if description:
            hotel.description = description
        if price is not None:
            hotel.price = price
        db.session.commit()
    return hotel

def delete_hotel(hotel_id):
    hotel = Hotel.query.get(hotel_id)
    if hotel:
        db.session.delete(hotel)
        db.session.commit()
        return True
    return False
