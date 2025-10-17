# Schema CSV/YAML
- sample_map.csv: edge_id:int, u:int, v:int, weight:float (>=0)
- sample_coords.csv: node_id:int, x:float, y:float
- sample_lights.csv: intersection_id:int, cycle_s:float, green_ratio:float(0..1)
- sample_vehicles.csv: t:float, origin:int, dest:int, count:int>=1
- YAML keys: graph / lights / vehicles / simulation / astar
