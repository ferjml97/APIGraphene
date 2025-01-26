SELECT * FROM metrobus_stoptime WHERE trip_id NOT IN (SELECT id FROM metrobus_trip);
