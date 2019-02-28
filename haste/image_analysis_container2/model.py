import time

import pymongo
import scipy.stats


class KendallTauInterestingnessModel:

    def __init__(self, window_length):
        """
        :param window_length: how many images in the window for each well/color/etc
        """
        self.self.window_length = self.window_length

    def interestingness(self,
                        stream_id=None,
                        timestamp=None,
                        location=None,
                        substream_id=None,
                        metadata=None,
                        mongo_collection=None):
        """
        :param stream_id (str): ID for the stream session - used to group all the data for that streaming session.
        :param timestamp (numeric): should come from the cloud edge (eg. microscope). integer or floating point.
            *Uniquely identifies the document within the streaming session*.
        :param location (tuple): spatial information (eg. (x,y)).
        :param substream_id (string): ID for grouping of documents in stream (eg. microscopy well ID), or 'None'.
        :param metadata (dict): extracted metadata (eg. image features).
        :param mongo_collection: collection in mongoDB allowing custom queries (this is a hack - best avoided!)
        """

        # Since we go in ascending timestamp order, this will get us all the data

        t_start_query = time.time()
        # TODO: only get some fields
        results = list(mongo_collection.find({
            'metadata.well': metadata['well'],
            'metadata.color_channel': metadata['color_channel'],
            'metadata.imaging_point_number': metadata['imaging_point_number']
        },
            sort=[('timestamp', pymongo.ASCENDING)],
            projection=['timestamp', 'metadata.extracted_features'],
            limit=self.window_length
        ))

        t_end_query = time.time()
        metadata['duration_interestingness_query'] = t_end_query - t_start_query

        #     'sum_of_intensities': int(np.sum(image)),
        #     'correlation': __corr(image),

        if len(results) == 0:
            return {'interestingness': 1}

        taus = list()

        t_start_taus = time.time()

        for i, key in enumerate(['sum_of_intensities', 'correlation']):
            X = list(map(lambda r: r['timestamp'], results))
            Y = list(map(lambda r: r['metadata']['extracted_features'][key], results))

            X.append(timestamp)
            Y.append(metadata['extracted_features'][key])

            ktau, pvalue = scipy.stats.kendalltau(X, Y)

            taus.append(ktau)

        t_end_taus = time.time()
        metadata['duration_interestingness_taus_calc'] = t_end_taus - t_start_taus

        metadata['interestingness_calcs'] = {}
        metadata['interestingness_calcs']['kendal_tau'] = taus

        interestingness = max(map(lambda tau: abs(tau), taus))

        metadata['interestingness_calcs']['max_of_abs'] = interestingness

        if timestamp % 10 == 0:
            interestingness = 1
        elif len(results) < self.window_length:
            interestingness = 1

        # TODO: add sampling/interlacing over window

        return {'interestingness': interestingness}
