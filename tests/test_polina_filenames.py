from haste.image_analysis_container2.filenames.polina_sample_filenames import parse_polina_filename


def test_polina_filenames():
    filenames = [
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w12DE5D0E6-1639-40D4-8654-9A6247B4B8CD.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w1_thumbE7E91F39-2BB5-4B83-B769-5BB151301A34.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w2426F374B-F2B3-4525-88B9-713CA16427F9.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w2_thumb0604FB4F-9460-418C-B35D-153E066CFF68.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w39CC0188A-1F09-4EC4-AEBC-3339DEC7FEE1.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w3_thumbAB85F459-31FD-4757-A133-D3252E9BE190.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w4D7668323-7575-4E57-BDE4-056544B410FA.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w4_thumbEF43A4A9-7526-4BD6-9CAB-C58D52F65FC1.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w57AFB89BB-985A-4210-AFE1-EABB40E7BDC0.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s1_w5_thumb450DA673-ADB9-4FC0-A26A-E43B5071B061.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w13014AD26-7BBC-4E53-8DEF-50291BD276ED.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w1_thumb9EC21643-0F30-4462-B436-3A08C434F548.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w27DC1F734-FC38-4EBB-9AAD-CE6440143471.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w2_thumb7322D36E-95E0-4278-BE41-33072A153BD8.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w38BC7ABAB-DAA3-46DB-BDD9-B4618E8948F8.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w3_thumb3D3794B8-B736-449E-9EA1-912310A93A02.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w40EECA426-CD90-4CF6-B434-DA3DABFE5EA7.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w4_thumbA7B460E7-1F87-4934-8F30-323A97E92A4A.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w5A86CB3CD-7EAA-4B6D-87BC-B5CFDE17DB14.tif',
        '181214-KOday7-40X-H2O2-Glu_B02_s2_w5_thumb2F0AD9F9-9F9A-4D29-A0CB-0E0A5500D1E1.tif'
    ]

    # TODO: this is a sanity check
    for f in filenames:
        metadata = parse_polina_filename(f)

        print(metadata)

        assert metadata['date_year'] == 18

        assert metadata['well'] == 'B02'
        assert metadata['color_channel'] in range(1, 6)
        assert metadata['well_sample'] in [1, 2]

# Output:
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 1, 'is_thumbnail': False, 'guid': '2DE5D0E6-1639-40D4-8654-9A6247B4B8CD', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 1, 'is_thumbnail': True, 'guid': 'E7E91F39-2BB5-4B83-B769-5BB151301A34', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 2, 'is_thumbnail': False, 'guid': '426F374B-F2B3-4525-88B9-713CA16427F9', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 2, 'is_thumbnail': True, 'guid': '0604FB4F-9460-418C-B35D-153E066CFF68', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 3, 'is_thumbnail': False, 'guid': '9CC0188A-1F09-4EC4-AEBC-3339DEC7FEE1', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 3, 'is_thumbnail': True, 'guid': 'AB85F459-31FD-4757-A133-D3252E9BE190', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 4, 'is_thumbnail': False, 'guid': 'D7668323-7575-4E57-BDE4-056544B410FA', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 4, 'is_thumbnail': True, 'guid': 'EF43A4A9-7526-4BD6-9CAB-C58D52F65FC1', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 5, 'is_thumbnail': False, 'guid': '7AFB89BB-985A-4210-AFE1-EABB40E7BDC0', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 1, 'color_channel': 5, 'is_thumbnail': True, 'guid': '450DA673-ADB9-4FC0-A26A-E43B5071B061', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 1, 'is_thumbnail': False, 'guid': '3014AD26-7BBC-4E53-8DEF-50291BD276ED', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 1, 'is_thumbnail': True, 'guid': '9EC21643-0F30-4462-B436-3A08C434F548', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 2, 'is_thumbnail': False, 'guid': '7DC1F734-FC38-4EBB-9AAD-CE6440143471', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 2, 'is_thumbnail': True, 'guid': '7322D36E-95E0-4278-BE41-33072A153BD8', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 3, 'is_thumbnail': False, 'guid': '8BC7ABAB-DAA3-46DB-BDD9-B4618E8948F8', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 3, 'is_thumbnail': True, 'guid': '3D3794B8-B736-449E-9EA1-912310A93A02', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 4, 'is_thumbnail': False, 'guid': '0EECA426-CD90-4CF6-B434-DA3DABFE5EA7', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 4, 'is_thumbnail': True, 'guid': 'A7B460E7-1F87-4934-8F30-323A97E92A4A', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 5, 'is_thumbnail': False, 'guid': 'A86CB3CD-7EAA-4B6D-87BC-B5CFDE17DB14', 'extension': '.tif'}
# {'date_year': 18, 'date_month': 12, 'date_day_of_month': 14, 'note': 'KOday7-40X-H2O2-Glu', 'well': 'B02', 'well_sample': 2, 'color_channel': 5, 'is_thumbnail': True, 'guid': '2F0AD9F9-9F9A-4D29-A0CB-0E0A5500D1E1', 'extension': '.tif'}
