import itertools

import numpy as np

import probvis.general.histogram as pvh


def events_plot(save_dir, events, **args):
    '''

    :param save_dir:
    :param events: list of tuple: (t, content, user, metadata)
    :param args:
    :return:
    '''
    name = '{}_'.format(args['name']) if 'name' in args else ''
    close = args['close'] if 'close' in args else 'all'

    ts_per_user_dict = create_ts_per_user_dict(events)
    ts_per_user = list(ts_per_user_dict.values())
    ts_min_per_user = [np.min(ts) for ts in ts_per_user]
    ts_max_per_user = [np.max(ts) for ts in ts_per_user]
    timestamp = list(itertools.chain(*ts_per_user))

    time_span = list(np.array(ts_max_per_user) - np.array(ts_min_per_user))

    pvh.hist_plot(save_dir, timestamp, label=None, density=False, name='ts', alpha=0.7, xlabel=r'Timestamp',
                  fontsize=32, close=close)
    pvh.hist_plot(save_dir, time_span, label=None, density=False, name='ts_span', alpha=0.7, xlabel=r'$\Delta$ timestamp',
                  fontsize=32, close=close)

    d_list = [ts_min_per_user, ts_max_per_user]
    l_list = [r'min', r'max']
    pvh.multi_hist_plot(save_dir, d_list, l_list, name='ts_min_max', color_list=None, xlabel='Timestamp', density=False,
                        alpha=0.7, fontsize=32, close=close, binwidth=None)


# %% Auxiliary functions

def create_ts_per_user_dict(events):
    user_timestamp_dict = dict()
    for ev in events:
        ts, c, u, metadata = ev

        if u in user_timestamp_dict.keys():
            user_timestamp_dict[u].append(ts)
        else:
            user_timestamp_dict[u] = list()
            user_timestamp_dict[u].append(ts)

    return user_timestamp_dict
