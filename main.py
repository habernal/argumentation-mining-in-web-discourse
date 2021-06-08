import os
import random
from typing import List

from cassis import load_typesystem, TypeSystem, load_cas_from_xmi, Cas


def process_xmi_file(xmi_file_name: str, type_system: TypeSystem):
    with open(xmi_file_name, 'rb') as f:
        cas: Cas = load_cas_from_xmi(f, type_system)

    argument_components = cas.select('de.tudarmstadt.ukp.dkpro.argumentation.types.ArgumentComponent')

    claims = cas.select('de.tudarmstadt.ukp.dkpro.argumentation.types.Claim')
    premises = 'de.tudarmstadt.ukp.dkpro.argumentation.types.Premise'
    rebuttals = 'de.tudarmstadt.ukp.dkpro.argumentation.types.Rebuttal'
    refutations = 'de.tudarmstadt.ukp.dkpro.argumentation.types.Refutation'
    backings = 'de.tudarmstadt.ukp.dkpro.argumentation.types.Backing'

    # print the first claim
    claim = claims[0]
    print(claim)
    print(claim.get_covered_text())
    # tokens of the claim
    tokens = cas.select_covered('de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token', claim)
    for token in tokens:
        print(token)
        print(token.get_covered_text())


if __name__ == '__main__':
    data_path: str = 'habernal.gurevych.2017.argumentation.mining.CL.data/data/gold.data.toulmin/'

    type_system_file: str = os.path.join(data_path, 'TypeSystem.xml')

    with open(type_system_file, 'rb') as f:
        type_system: TypeSystem = load_typesystem(f)

    # list all XMI files
    xmi_file_names: List[str] = [os.path.join(data_path, file_name) for file_name in os.listdir(data_path)
                                 if file_name.endswith('.xmi')]

    # there are 340 files
    assert len(xmi_file_names) == 340

    # open a random file
    random_xmi_file_name: str = random.Random(1234).choice(xmi_file_names)

    process_xmi_file(random_xmi_file_name, type_system)

