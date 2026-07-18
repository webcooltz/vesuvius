import os
import sys

def check_agreement():
    install_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    agreement_file_path = os.path.join(install_path, 'vesuvius', 'setup', 'agreement.txt')

    current_script = os.path.abspath(sys.argv[0])

    if not os.path.exists(agreement_file_path):
        if "accept_terms" not in current_script:
            raise ImportError(
                "You must accept the terms and conditions before using this package. "
                "Run `vesuvius.accept_terms --yes` or `python -m vesuvius_accept_terms --yes`."
            )
    else:   
        with open(agreement_file_path, 'r') as file:
            content = file.read().strip()
            if content != 'yes':
                raise ImportError(
                    "The agreement file is corrupted or incorrect. "
                    "Please run `vesuvius.accept_terms --yes` again."
                )

check_agreement()

from .volume import Volume, Cube
from .paths.utils import list_files
from .paths.utils import list_cubes as cubes
from .paths.utils import is_aws_ec2_instance

__all__ = ["Volume", "Cube", "list_files", "cubes", "is_aws_ec2_instance"]