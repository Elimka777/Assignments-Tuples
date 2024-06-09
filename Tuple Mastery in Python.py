def format_itineraries(flight_list):
    formatted_string = ""
    for index, (traveler_name, origin, destination) in enumerate(flight_list, start=1):
        formatted_string += f"Itinerary {index}: {traveler_name} - From {origin} to {destination}\n"
    return formatted_string.strip()

# Example usage
flight_list = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(format_itineraries(flight_list))
