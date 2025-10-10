hotel_diccionary = {
    'name' : 'Hotel Tipton',
    'stars' : 'Five Star',
    'rooms' : [
        {
            'room_number' : 1,
            'floor' : "first floor",
            'price' : "100"
        },
        {
            'room_number' : 2,
            'floor' : "second floor",
            'price' : "150"
        },
        {
            'room_number' : 3,
            'floor' : 'third floor',
            'price' : '300'
        }
    ]
}

print(f'{hotel_diccionary['name']} {hotel_diccionary['rooms'][1]}')