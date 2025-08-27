import pathlib
from pytorque.models.environment import EnvironmentEacSpec


SAMPLE_PATH = pathlib.Path(__file__).parent / "K7hLJdYVlfWv.yaml"


def test_update_grain_input_adds_defaults_and_round_trips():
    # Load the provided EAC YAML sample
    original_text = SAMPLE_PATH.read_text(encoding="utf-8")
    spec = EnvironmentEacSpec.from_yaml(original_text)

    # Sanity: ensure grain exists in the sample
    grain_name = "Egress"
    grain = spec.get_grain(grain_name)
    assert grain is not None

    cpu_entry = next(item for item in grain.spec.inputs if isinstance(item, dict) and "cpu" in item)
    ram_entry = next(item for item in grain.spec.inputs if isinstance(item, dict) and "ram" in item)
    assert cpu_entry["cpu"] == 2
    assert ram_entry["ram"] == "4Gi"
    # Update two inputs on the grain
    grain.update_grain_input({"cpu": 3, "ram": "6Gi"})

    cpu_entry = next(item for item in grain.spec.inputs if isinstance(item, dict) and "cpu" in item)
    ram_entry = next(item for item in grain.spec.inputs if isinstance(item, dict) and "ram" in item)
    assert cpu_entry["cpu"] == 3
    assert ram_entry["ram"] == "6Gi"

    # Round-trip and ensure change persist
    dumped = spec.to_yaml()
    spec2 = EnvironmentEacSpec.from_yaml(dumped)
    grain2 = spec2.get_grain(grain_name)
    assert grain2 is not None
    cpu2 = next(item for item in grain2.spec.inputs if isinstance(item, dict) and "cpu" in item)
    ram2 = next(item for item in grain2.spec.inputs if isinstance(item, dict) and "ram" in item)
    assert cpu2["cpu"] == 3
    assert ram2["ram"] == "6Gi"


if __name__ == "__main__":
    test_update_grain_input_adds_defaults_and_round_trips()