import re

# Parse Filenames from Polinas sample from Spjuth lab:

# '181214-KOday7-40X-H2O2-Glu_B02_s1_w12DE5D0E6-1639-40D4-8654-9A6247B4B8CD.tif',
# '181214-KOday7-40X-H2O2-Glu_B02_s1_w1_thumbE7E91F39-2BB5-4B83-B769-5BB151301A34.tif',
# '181214-KOday7-40X-H2O2-Glu_B02_s1_w2426F374B-F2B3-4525-88B9-713CA16427F9.tif',
# '181214-KOday7-40X-H2O2-Glu_B02_s1_w2_thumb0604FB4F-9460-418C-B35D-153E066CFF68.tif',
# '181214-KOday7-40X-H2O2-Glu_B02_s1_w39CC0188A-1F09-4EC4-AEBC-3339DEC7FEE1.tif',

# "KOday7-40X-H2O2-Glu"
# KOday7 is reagent, 40X is magnification, and everything after 40x is PlateID, but for now I think you squashing it into "note" is fine

__pattern = re.compile('^'
                       + '([0-9]{2})([0-9]{2})([0-9]{2})'  # date yymmdd [1,2,3]
                       + '-([^_]+)'  # 40X-H2O2-Glu [4]
                       + '_([A-Za-z]+[0-9]+)'  # Well [5]
                       + '_s([0-9]+)'  # Well Sample [6] "microscope position in the well"
                       + '_w([0-9]+)'  # Channel (color channel?) [7]
                       + '(_thumb)?'  # Thumbnail [8]
                       + '([A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12})'  # Image GUID [9]
                       + '(\.tiff?)?'  # Extension [10]
                       + '$'
                       ,
                       re.IGNORECASE)  # Windows has case-insensitive filenames


def parse_polina_filename(filename):
    # Note: this is for parsing file NAMES not file PATHS.

    match = re.search(__pattern, filename)

    if match is None:
        return None

    metadata = {
        'date_year': int(match.group(1)),
        'date_month': int(match.group(2)),
        'date_day_of_month': int(match.group(3)),
        'note': match.group(4),
        'well': match.group(5).upper(),  # e.g. A1, H12
        'well_sample': int(match.group(6)),
        'color_channel': int(match.group(7)),
        'is_thumbnail': match.group(8) is not None,
        'guid': match.group(9),
        'extension': match.group(10),
    }

    # For compatibility with AZ dataset.:
    metadata['imaging_point_number'] = metadata['well_sample']

    return metadata
