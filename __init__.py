from gym.envs.registration import register

register(
    id='TheRealFufi-v0',
    entry_point='gym_TheRealFufi.envs:TheRealFufiEnv',
    max_episode_steps=1200,
)
