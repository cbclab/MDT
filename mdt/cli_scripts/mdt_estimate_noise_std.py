#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
"""Estimate the noise standard deviation of the Gaussian noise in the original complex image domain.

The result is a single floating point number with the noise std. for every voxel. It uses the estimation routines
from the components folders for the estimation. The estimation is the same as the one used in mdt-model-fit, but
since the noise std estimation depends on the mask used, it is better to call this function beforehand with a
complete brain mask. Later, the mdt-model-fit routine can be called on smaller masks with as noise std the value
from this function.
"""
import argparse
import os
import mdt
from argcomplete.completers import FilesCompleter
from mdt.shell_utils import BasicShellApplication
from mot import cl_environments
import textwrap


__author__ = 'Robbert Harms'
__date__ = "2015-08-18"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class NoiseStdEstimation(BasicShellApplication):

    def __init__(self):
        super(NoiseStdEstimation, self).__init__()
        self.available_devices = list((ind for ind, env in
                                       enumerate(cl_environments.CLEnvironmentFactory.smart_device_selection())))

    def _get_arg_parser(self, doc_parser=False):
        description = textwrap.dedent(__doc__)
        description += mdt.shell_utils.get_citation_message()

        epilog = textwrap.dedent("""
            Examples of use:
                mdt-estimate-noise-std data.nii.gz data.prtcl full_mask.nii.gz
        """)

        parser = argparse.ArgumentParser(description=description, epilog=epilog,
                                         formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('dwi',
                            action=mdt.shell_utils.get_argparse_extension_checker(['.nii', '.nii.gz', '.hdr', '.img']),
                            help='the diffusion weighted image').completer = FilesCompleter(['nii', 'gz', 'hdr', 'img'],
                                                                                            directories=False)
        parser.add_argument(
            'protocol', action=mdt.shell_utils.get_argparse_extension_checker(['.prtcl']),
            help='the protocol file, see mdt-generate-protocol').completer = FilesCompleter(['prtcl'],
                                                                                            directories=False)
        parser.add_argument('mask',
                            action=mdt.shell_utils.get_argparse_extension_checker(['.nii', '.nii.gz', '.hdr', '.img']),
                            help='the (brain) mask to use').completer = FilesCompleter(['nii', 'gz', 'hdr', 'img'],
                                                                               directories=False)

        parser.add_argument('--estimator', '-e', type=str, help='The name of the estimation routine to use')

        return parser

    def run(self, args):
        problem_data = mdt.load_problem_data(os.path.realpath(args.dwi),
                                             os.path.realpath(args.protocol),
                                             os.path.realpath(args.mask))

        estimator = None
        if args.estimator:
            estimator = mdt.load_component('noise_std_estimators', args.estimator)

        with mdt.disable_logging_context():
            noise_std = mdt.estimate_noise_std(problem_data, estimator=estimator)
            print(noise_std)


if __name__ == '__main__':
    NoiseStdEstimation().start()
