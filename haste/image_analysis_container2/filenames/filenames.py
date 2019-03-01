from haste.image_analysis_container2.filenames.azn_filenames import parse_azn_file_name
from haste.image_analysis_container2.filenames.polina_sample_filenames import parse_polina_filename


def parse_filename(filename):
    for func in [parse_azn_file_name, parse_polina_filename]:
        metadata = func(filename)
        if metadata is not None:
            return metadata