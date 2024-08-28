import logging
import time
from soil_module import list_soils, rank_soils

def test_soil_location():
    test_locations = [
        {"PrimaryKey": "16071614480694232016-09-01", "lon": -119.788100, "lat": 41.658230, "plot_id": 2, "pSlope": 1.700000, "pElev": 1693.000000},
        {"PrimaryKey": "16071711301954552016-09-01", "lon": -119.530500, "lat": 41.287620, "plot_id": 3, "pSlope": 8.800000, "pElev": 1956.000000},
        {"PrimaryKey": "16071811395989392016-09-01", "lon": -119.749700, "lat": 41.270760, "plot_id": 4, "pSlope": 5.200000, "pElev": 1783.000000},
        {"PrimaryKey": "16071418204862092016-09-01", "lon": -119.704100, "lat": 41.596130, "plot_id": 5, "pSlope": 1.700000, "pElev": 1735.000000},
        {"PrimaryKey": "16072008373278452016-09-01", "lon": -119.790300, "lat": 41.750320, "plot_id": 6, "pSlope": 3.500000, "pElev": 1687.000000},
        {"PrimaryKey": "16091513063030982016-09-01", "lon": -119.636600, "lat": 41.809090, "plot_id": 7, "pSlope": 17.600000, "pElev": 2046.000000},
        {"PrimaryKey": "16091610123736882016-09-01", "lon": -119.285400, "lat": 41.493790, "plot_id": 8, "pSlope": 8.700000, "pElev": 1793.000000},
        {"PrimaryKey": "16061713532998252016-09-01", "lon": -117.395400, "lat": 41.980950, "plot_id": 9, "pSlope": 3.000000, "pElev": 1884.000000},
        {"PrimaryKey": "16071208365442016-09-01", "lon": -115.682200, "lat": 41.953570, "plot_id": 10, "pSlope": 47.000000, "pElev": 1638.830000},
        {"PrimaryKey": "16031113172661072016-09-01", "lon": -116.606200, "lat": 36.639850, "plot_id": 11, "pSlope": 3.000000, "pElev": 752.000000},
        {"PrimaryKey": "16031113195284292016-09-01", "lon": -116.454200, "lat": 36.447690, "plot_id": 12, "pSlope": 7.000000, "pElev": 687.000000},
        {"PrimaryKey": "16031113205718272016-09-01", "lon": -116.550700, "lat": 36.832330, "plot_id": 13, "pSlope": 7.000000, "pElev": 1055.000000},
        {"PrimaryKey": "160311132137362016-09-01", "lon": -116.327800, "lat": 36.542440, "plot_id": 14, "pSlope": 4.000000, "pElev": 773.000000},
        {"PrimaryKey": "16032410223545672016-09-01", "lon": -116.046800, "lat": 36.584970, "plot_id": 15, "pSlope": 4.000000, "pElev": 960.000000},
    ]

    soil_profiles = {
        "10092315213026782016-09-01": {
            "soilHorizon": ["SILT LOAM", "CLAY LOAM"],
            "horizonDepthUpper": [0, 6],
            "horizonDepthLower": [6, 28]
        },
        "11042011045429962016-09-01": {
            "soilHorizon": ["LOAM", "CLAY LOAM", "CLAY"],
            "horizonDepthUpper": [0, 20, 34],
            "horizonDepthLower": [20, 34, 42]
        },
        "11051715272976692011-09-01": {
            "soilHorizon": ["SILTY CLAY", "SILTY CLAY"],
            "horizonDepthUpper": [0, 10.16],
            "horizonDepthLower": [11, 61]
        },
        "12050210581436242012-09-01": {
            "soilHorizon": ["CLAY LOAM"],
            "horizonDepthUpper": [4],
            "horizonDepthLower": [10]
        },
        "12050210581436242013-09-01": {
            "soilHorizon": ["CLAY LOAM"],
            "horizonDepthUpper": [4],
            "horizonDepthLower": [10]
        },
        "12050210581436242014-09-01": {
            "soilHorizon": ["CLAY LOAM"],
            "horizonDepthUpper": [4],
            "horizonDepthLower": [10]
        },
        "12050210581436242015-09-01": {
            "soilHorizon": ["CLAY LOAM"],
            "horizonDepthUpper": [4],
            "horizonDepthLower": [10]
        },
        "12050213062675882015-09-01": {
            "soilHorizon": ["CLAY LOAM", "CLAY"],
            "horizonDepthUpper": [0, 7.62],
            "horizonDepthLower": [8, 51]
        },
        "1205021310244002015-09-01": {
            "soilHorizon": ["LOAM", "CLAY LOAM", "CLAY"],
            "horizonDepthUpper": [0, 7.62, 45.72],
            "horizonDepthLower": [8, 46, 61]
        },
    }

    site_calc = False

    for item in test_locations:
        try:
            logging.info(f"Testing {item['lon']}, {item['lat']}, {item['plot_id']}")
            start_time = time.perf_counter()
            result_list = list_soils(item["lon"], item["lat"], None, site_calc)
            logging.info(f"...time: {(time.perf_counter()-start_time):.2f}s")
            if site_calc:
                profile = soil_profiles[item["PrimaryKey"]]
                result_rank = rank_soils(
                    item["lon"],
                    item["lat"],
                    profile["soilHorizon"],
                    profile["horizonDepthUpper"],
                    profile["horizonDepthLower"],
                    item["pSlope"],
                    item["pElev"],
                    plot_id=None
                )
            print(result_list)
            if site_calc:
                print(result_rank)
        except Exception as e:
            logging.error(f"Error processing {item['PrimaryKey']}: {e}")
    soil_id.config.TEMP_DIR.cleanup()
