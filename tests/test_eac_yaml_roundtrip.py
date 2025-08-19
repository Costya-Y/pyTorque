import pathlib
from pytorque.models.environment import EnvironmentEacSpec

SAMPLE_PATH = pathlib.Path(__file__).parent.parent / "K7hLJdYVlfWv.yaml"


def test_eac_round_trip():
    original_text = SAMPLE_PATH.read_text(encoding="utf-8")
    spec = EnvironmentEacSpec.from_yaml(original_text)
    dumped = spec.to_yaml()
    # Parse again to ensure dumped version is valid and equivalent structurally
    spec2 = EnvironmentEacSpec.from_yaml(dumped)

    # Compare key structural components
    assert spec.meta == spec2.meta
    assert set(spec.grain_names()) == set(spec2.grain_names())
    for name in spec.grain_names():
        g1 = spec.get_grain(name)
        g2 = spec2.get_grain(name)
        assert g1 is not None and g2 is not None
        assert g1.depends_on == g2.depends_on
        assert g1.kind == g2.kind
        assert g1.spec.model_dump(by_alias=True) == g2.spec.model_dump(by_alias=True)

    assert spec.inputs == spec2.inputs
    assert spec.outputs == spec2.outputs
    assert spec.spec_version == spec2.spec_version
