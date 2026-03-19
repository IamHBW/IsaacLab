Changelog
---------

0.0.3 (2026-04-06)
~~~~~~~~~~~~~~~~~~

Fixed
^^^^^

* Fixed :class:`~isaaclab_experimental.envs.direct_rl_env_warp.DirectRLEnvWarp`
  creating a Kit UI window for headless visualizer-only runs. The warp environment
  now only instantiates the UI window when GUI support is actually available, while
  continuing to render through :attr:`~isaaclab.sim.SimulationContext.is_rendering`.


0.0.2 (2026-03-16)
~~~~~~~~~~~~~~~~~~

Fixed
^^^^^

* Fixed :class:`~isaaclab_experimental.envs.DirectRLEnvWarp` not being recognized by
  RL library wrappers (e.g. :class:`~isaaclab_rl.rl_games.RlGamesVecEnvWrapper`) that
  check for :class:`~isaaclab.envs.DirectRLEnv` via ``isinstance``. Changed base class
  from :class:`gym.Env` to :class:`~isaaclab.envs.DirectRLEnv`; all methods are
  overridden so behavior is unchanged.


0.0.1 (2026-01-01)
~~~~~~~~~~~~~~~~~~

Added
^^^^^

* Initial release of the ``isaaclab_experimental`` package.
