Changelog
---------

0.0.2 (2026-03-19)
~~~~~~~~~~~~~~~~~~

Fixed
^^^^^

* Fixed :class:`~isaaclab_experimental.envs.direct_rl_env_warp.DirectRLEnvWarp`
  creating a Kit UI window for headless visualizer-only runs. The warp environment
  now only instantiates the UI window when GUI support is actually available, while
  continuing to render through :attr:`~isaaclab.sim.SimulationContext.is_rendering`.
