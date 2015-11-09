SELECT 
	start_station_id, 
	start_station_name,
	CDB_TransformToWebmercator(CDB_LatLng(
      start_station_latitude, 
      start_station_longitude
      )
	) as start_station_location,
	SUM(tripduration) AS trip_count

FROM citibikehw7

WHERE
	ST_DWithin(CDB_LatLng(
      start_station_latitude,
      start_station_longitude
    )::geography,
      CDB_LatLng(40.7307602, -73.9974086)::geography,
      1000)

GROUP BY 
	start_station_id,
	start_station_name,
	start_station_latitude,
	start_station_longitude

ORDER BY trip_count DESC