import argparse

import joblib
import tensorflow as tf

from rllab.misc.console import query_yes_no
from rllab.sampler.utils import rollout, deterministic_rollout

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
                        help='path to the snapshot file')
    parser.add_argument('--max_path_length', type=int, default=1000,
                        help='Max length of rollout')
    parser.add_argument('--speedup', type=float, default=1,
                        help='Speedup')
    parser.add_argument('--isdeterm', type=bool, default=False)
    args = parser.parse_args()

    import pdb; pdb.set_trace()
    # If the snapshot file use tensorflow, do:
    # import tensorflow as tf
    # with tf.Session():
    #     [rest of the code]
    if args.isdeterm:
        rollout_fn = deterministic_rollout
    else:
        rollout_fn = rollout 

    with tf.Session() as sess:
        data = joblib.load(args.file)
        policy = data['policy']
        env = data['env']
        while True:
            path = rollout_fn(env, policy, max_path_length=args.max_path_length,
                           animated=True, speedup=args.speedup, always_return_paths=True)
            if not query_yes_no('Continue simulation?'):
                break
