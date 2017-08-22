class DatabaseManager:

    def __init__(self, df_engine_keys: pd.DataFrame, date_from: datetime.date=datetime.date(2012, 1, 1),
                 database_converter: DatabaseConverter=DatabaseConverter()):
        self.date_from = date_from
        self.df_engine_keys = df_engine_keys
        self.database_converter = database_converter

    class _Decorators(object):
        @classmethod
        def _catcher_decorator(cls, func):
            def catch_wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except EXCEPTION as e:
                    return catch(e, func)

            return catch_wrapper

        @classmethod
        def _read_decorator(cls, func):
            def log_wrapper(*args, rail_id, meas_id_from):
                Logger().info('Retrieving data from DB for rail_id: %s from measure_id: %d' % (rail_id, meas_id_from))
                t_start = time.time()
                df_result = func(*args, rail_id, meas_id_from)
                Logger().info('Retrieved %d rows (%2.2f MB) from DB for rail_id: %s from measure_id: %d took: %2.1fs' % (df_result[0].shape[0], sys.getsizeof(df_result[0])/ (1024*1024), rail_id, meas_id_from, time.time()-t_start))

                return df_result

            return log_wrapper

    @_Decorators._catcher_decorator
    @_Decorators._read_decorator
    def read(self, rail_id: str, meas_id_from: int) -> List:
	pass
