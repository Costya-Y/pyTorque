from pytorque.models.environment import Environment, EnvironmentStatus

def test_environment_model():
    env = Environment(id='e1', name='Env1', status=EnvironmentStatus.RUNNING)
    assert env.status == EnvironmentStatus.RUNNING
    assert env.id == 'e1'
