from pytorque.models.environment import EnvironmentEacSpec


def test_from_yaml_with_trailing_commas():
    # Simulate a YAML snippet that incorrectly includes trailing commas after scalar values
    malformed = """
    environment:
      environment_name: demo-env,
      owner_email: user@example.com,
    grains:
      web:
        kind: terraform,
        spec:
          commands: [],
          env-vars: [],
          inputs: [],
          outputs: [],
          source: {}
    inputs: {}
    outputs: {}
    spec_version: 1
    """
    spec = EnvironmentEacSpec.from_yaml(malformed)
    assert spec.meta.environment_name == "demo-env"
    assert "web" in spec.grains
    assert spec.spec_version == 1
